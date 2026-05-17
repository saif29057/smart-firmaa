from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.conf import settings
from openai import OpenAI
from .models import ChatMessage

client = OpenAI(api_key=settings.OPENAI_API_KEY)

AGRICULTURAL_CONTEXT = """
Tu es un assistant expert en agriculture pour Smart Firma, une plateforme intelligente pour les agriculteurs tunisiens.
Ton domaine d'expertise inclut:
- Les cultures adaptées au climat tunisien (oliviers, céréales, agrumes, légumes, dattes)
- Les pratiques agricoles durables et biologiques
- La gestion de l'irrigation et des ressources en eau
- Les prévisions météorologiques et leur impact sur l'agriculture
- Les maladies des plantes et les traitements biologiques
- Les calendriers de plantation et de récolte
- Les techniques de modernisation agricole
- Les subventions et programmes gouvernementaux agricoles en Tunisie

Sois concis, pratique et donne des conseils spécifiques à l'agriculture tunisienne.
"""

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def chat_with_ai(request):
    try:
        user_message = request.data.get('message', '').strip()

        if not user_message:
            return Response(
                {'error': 'Le message ne peut pas être vide'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Vérification que la clé API est bien configurée
        if not settings.OPENAI_API_KEY:
            return Response(
                {'error': 'Clé API OpenAI non configurée'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        messages = [
            {"role": "system", "content": AGRICULTURAL_CONTEXT},
            {"role": "user", "content": user_message}
        ]

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_completion_tokens=500,
            temperature=0.7
        )

        ai_response = response.choices[0].message.content.strip()

        chat_message = ChatMessage.objects.create(
            user=request.user,
            message=user_message,
            response=ai_response
        )

        return Response({
            'response': ai_response,
            'timestamp': chat_message.created_at
        })

    except Exception as e:
        return Response(
            {'error': f'Erreur lors du traitement: {str(e)}'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def chat_history(request):
    try:
        messages = ChatMessage.objects.filter(
            user=request.user
        ).order_by('-created_at')[:50]

        history = [
            {
                'id': msg.id,
                'message': msg.message,
                'response': msg.response,
                'created_at': msg.created_at
            }
            for msg in messages
        ]

        return Response({'history': history})

    except Exception as e:
        return Response(
            {'error': f"Erreur lors de la récupération de l'historique: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
def clear_chat_history(request):
    try:
        ChatMessage.objects.filter(user=request.user).delete()
        return Response({'message': 'Historique de conversation effacé avec succès'})

    except Exception as e:
        return Response(
            {'error': f"Erreur lors de l'effacement de l'historique: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )