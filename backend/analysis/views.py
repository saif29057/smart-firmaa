import os
import time
import numpy as np
from PIL import Image
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import AnalysisLog
from .serializers import AnalysisLogSerializer
from .recommendations import get_recommendations

# ─── Model configuration ──────────────────────────────────────────────────────

# Place plant_disease_cnn.h5 in backend/ folder (same level as manage.py)
MODEL_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'plant_disease_cnn.h5')

# 38 classes from vipoooool/new-plant-diseases-dataset — sorted alphabetically
CLASS_NAMES = [
    'Apple___Apple_scab',
    'Apple___Black_rot',
    'Apple___Cedar_apple_rust',
    'Apple___healthy',
    'Blueberry___healthy',
    'Cherry_(including_sour)___Powdery_mildew',
    'Cherry_(including_sour)___healthy',
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
    'Corn_(maize)___Common_rust_',
    'Corn_(maize)___Northern_Leaf_Blight',
    'Corn_(maize)___healthy',
    'Grape___Black_rot',
    'Grape___Esca_(Black_Measles)',
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
    'Grape___healthy',
    'Orange___Haunglongbing_(Citrus_greening)',
    'Peach___Bacterial_spot',
    'Peach___healthy',
    'Pepper,_bell___Bacterial_spot',
    'Pepper,_bell___healthy',
    'Potato___Early_blight',
    'Potato___Late_blight',
    'Potato___healthy',
    'Raspberry___healthy',
    'Soybean___healthy',
    'Squash___Powdery_mildew',
    'Strawberry___Leaf_scorch',
    'Strawberry___healthy',
    'Tomato___Bacterial_spot',
    'Tomato___Early_blight',
    'Tomato___Late_blight',
    'Tomato___Leaf_Mold',
    'Tomato___Septoria_leaf_spot',
    'Tomato___Spider_mites Two-spotted_spider_mite',
    'Tomato___Target_Spot',
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
    'Tomato___Tomato_mosaic_virus',
    'Tomato___healthy',
]

# ─── Lazy model loading ───────────────────────────────────────────────────────

_model = None

def load_model():
    global _model
    if _model is not None:
        return _model
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            f"Fichier modèle introuvable: {MODEL_PATH}\n"
            "Placez plant_disease_cnn.h5 dans le dossier backend/."
        )
    try:
        import tensorflow as tf
        _model = tf.keras.models.load_model(MODEL_PATH)
        return _model
    except ImportError:
        raise RuntimeError("TensorFlow non installé. Lancez: pip install tensorflow==2.15.0")
    except Exception as e:
        raise RuntimeError(f"Échec du chargement du modèle: {e}")

# ─── Image preprocessing ─────────────────────────────────────────────────────

def preprocess_image(image_path):
    try:
        image = Image.open(image_path).resize((224, 224))
        if image.mode != 'RGB':
            image = image.convert('RGB')
        arr = np.array(image, dtype=np.float32) / 255.0
        return np.expand_dims(arr, axis=0)
    except Exception as e:
        raise Exception(f"Erreur de prétraitement: {str(e)}")

# ─── Prediction ───────────────────────────────────────────────────────────────

def predict_disease(image_array, model):
    raw_probs = model.predict(image_array, verbose=0)[0]
    top_indices = np.argsort(raw_probs)[-3:][::-1]
    predictions = []
    for rank, idx in enumerate(top_indices, start=1):
        raw_label = CLASS_NAMES[idx]
        parts = raw_label.split('___')
        plant = parts[0].replace('_', ' ')
        disease = parts[1].replace('_', ' ') if len(parts) > 1 else 'Inconnu'
        is_healthy = 'healthy' in disease.lower()
        predictions.append({
            'rank': rank,
            'class': raw_label,
            'plant': plant,
            'disease': disease,
            'is_healthy': is_healthy,
            'confidence': float(raw_probs[idx]),
        })
    return predictions

# ─── Views ───────────────────────────────────────────────────────────────────

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_image(request):
    if 'image' not in request.FILES:
        return Response({'error': 'Aucune image fournie.'}, status=status.HTTP_400_BAD_REQUEST)
    image_file = request.FILES['image']
    if not image_file.content_type.startswith('image/'):
        return Response({'error': 'Le fichier doit être une image.'}, status=status.HTTP_400_BAD_REQUEST)
    if image_file.size > 10 * 1024 * 1024:
        return Response({'error': "L'image ne doit pas dépasser 10 MB."}, status=status.HTTP_400_BAD_REQUEST)

    analysis = None
    try:
        start_time = time.time()
        analysis = AnalysisLog.objects.create(
            user=request.user, image=image_file, result={}, confidence=0.0, processing_time=0.0,
        )
        image_array = preprocess_image(analysis.image.path)
        model = load_model()
        predictions = predict_disease(image_array, model)
        top = predictions[0]
        recommendations = get_recommendations(top['class'])
        analysis.result = {
            'predictions': predictions,
            'top_prediction': top,
            'recommendations': recommendations,
            'summary': (
                f"{'Plante saine' if top['is_healthy'] else 'Maladie détectée'}: "
                f"{top['plant']} — {top['disease']} ({top['confidence']*100:.1f}% de confiance)"
            ),
        }
        analysis.confidence = top['confidence']
        analysis.processing_time = time.time() - start_time
        analysis.save()
        serializer = AnalysisLogSerializer(analysis, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except (FileNotFoundError, RuntimeError) as e:
        if analysis: analysis.delete()
        return Response({'error': str(e)}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
    except Exception as e:
        if analysis: analysis.delete()
        return Response({'error': f"Erreur lors de l'analyse: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def analysis_history(request):
    analyses = AnalysisLog.objects.filter(user=request.user)
    serializer = AnalysisLogSerializer(analyses, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def analysis_detail(request, analysis_id):
    analysis = get_object_or_404(AnalysisLog, id=analysis_id)
    if analysis.user != request.user and not request.user.is_staff:
        return Response({'error': 'Accès non autorisé.'}, status=status.HTTP_403_FORBIDDEN)
    serializer = AnalysisLogSerializer(analysis, context={'request': request})
    return Response(serializer.data)
