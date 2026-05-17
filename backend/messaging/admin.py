from django.contrib import admin
from django.utils.html import format_html
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'recipient', 'subject_preview', 'is_read_badge', 'created_at']
    list_filter = ['is_read', 'created_at', 'sender', 'recipient']
    search_fields = ['subject', 'content', 'sender__username', 'recipient__username']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Informations générales', {
            'fields': ('sender', 'recipient', 'subject')
        }),
        ('Contenu', {
            'fields': ('content',)
        }),
        ('Statut', {
            'fields': ('is_read', 'created_at', 'updated_at')
        }),
    )
    
    ordering = ['-created_at']
    date_hierarchy = 'created_at'
    
    def subject_preview(self, obj):
        return obj.subject[:50] + '...' if len(obj.subject) > 50 else obj.subject
    subject_preview.short_description = 'Sujet'
    
    def is_read_badge(self, obj):
        if obj.is_read:
            return format_html('<span style="background-color: #22c55e; color: white; padding: 3px 8px; border-radius: 12px; font-size: 11px;">Lu</span>')
        return format_html('<span style="background-color: #ef4444; color: white; padding: 3px 8px; border-radius: 12px; font-size: 11px;">Non lu</span>')
    is_read_badge.short_description = 'Statut'
