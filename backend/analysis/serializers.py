from rest_framework import serializers
from .models import AnalysisLog


class AnalysisLogSerializer(serializers.ModelSerializer):
    # Returns a full absolute URL like http://localhost:8000/media/analysis_images/photo.jpg
    image_url = serializers.SerializerMethodField()
    user_username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = AnalysisLog
        fields = (
            'id', 'user', 'user_username',
            'image', 'image_url',
            'result', 'confidence', 'processing_time', 'created_at'
        )
        read_only_fields = ('id', 'user', 'user_username', 'confidence', 'processing_time', 'created_at')

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None
