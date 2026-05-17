from django.contrib import admin
from django.utils.html import format_html
from .models import AnalysisLog

@admin.register(AnalysisLog)
class AnalysisLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'image_thumbnail', 'diagnosis', 'confidence_percentage', 'processing_time', 'created_at']
    list_filter = ['created_at', 'user']
    search_fields = ['user__username', 'result__top_prediction__plant', 'result__top_prediction__disease']
    readonly_fields = ['user', 'image', 'result', 'confidence', 'processing_time', 'created_at', 'image_preview']
    
    fieldsets = (
        ('Informations générales', {
            'fields': ('user', 'created_at', 'processing_time')
        }),
        ('Image', {
            'fields': ('image', 'image_preview')
        }),
        ('Résultats de l\'analyse', {
            'fields': ('confidence', 'result')
        }),
    )
    
    ordering = ['-created_at']
    date_hierarchy = 'created_at'
    
    def image_thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 5px;" />', obj.image.url)
        return "Pas d'image"
    image_thumbnail.short_description = 'Image'
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width: 400px; max-height: 400px; object-fit: contain; border-radius: 10px;" />', obj.image.url)
        return "Pas d'image"
    image_preview.short_description = 'Aperçu'
    
    def diagnosis(self, obj):
        if obj.result and 'top_prediction' in obj.result:
            top = obj.result['top_prediction']
            plant = top.get('plant', 'Inconnu')
            disease = top.get('disease', 'Inconnu')
            return f"{plant} - {disease}"
        return "Non analysé"
    diagnosis.short_description = 'Diagnostic'
    
    def confidence_percentage(self, obj):
        return f"{obj.confidence * 100:.1f}%"
    confidence_percentage.short_description = 'Confiance'
    
    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
