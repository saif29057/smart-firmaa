from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy as _
from authentication.models import User
from analysis.models import AnalysisLog
from chatbot.models import ChatMessage
from messaging.models import Message
from django.db.models import Count, Avg, Q
from django.utils import timezone
from datetime import timedelta

class SmartFirmaAdminSite(AdminSite):
    site_header = 'Smart Firma Administration'
    site_title = 'Smart Firma Admin'
    index_title = 'Tableau de bord'
    
    def index(self, request, extra_context=None):
        # Calculer les statistiques
        stats = {}
        
        # Statistiques utilisateurs
        stats['total_users'] = User.objects.count()
        stats['active_users'] = User.objects.filter(is_active=True).count()
        last_user = User.objects.order_by('-created_at').first()
        stats['last_user'] = last_user.username if last_user else None
        
        # Statistiques analyses
        stats['total_analyses'] = AnalysisLog.objects.count()
        today = timezone.now().date()
        stats['analyses_today'] = AnalysisLog.objects.filter(created_at__date=today).count()
        last_analysis = AnalysisLog.objects.order_by('-created_at').first()
        stats['last_analysis'] = last_analysis.created_at.strftime('%d/%m/%Y %H:%M') if last_analysis else None
        
        # Statistiques messages
        stats['total_messages'] = Message.objects.count()
        stats['unread_messages'] = Message.objects.filter(is_read=False).count()
        last_message = Message.objects.order_by('-created_at').first()
        stats['last_message'] = last_message.created_at.strftime('%d/%m/%Y %H:%M') if last_message else None
        
        # Statistiques chatbot
        stats['total_chats'] = ChatMessage.objects.count()
        stats['chats_today'] = ChatMessage.objects.filter(created_at__date=today).count()
        last_chat = ChatMessage.objects.order_by('-created_at').first()
        stats['last_chat'] = last_chat.created_at.strftime('%d/%m/%Y %H:%M') if last_chat else None
        
        # Statistiques cultures (estimation basée sur les analyses)
        stats['crop_recommendations'] = AnalysisLog.objects.count()
        
        # Confiance moyenne des analyses
        avg_conf = AnalysisLog.objects.aggregate(avg_conf=Avg('confidence'))['avg_conf']
        stats['avg_confidence'] = f"{avg_conf * 100:.1f}" if avg_conf else "0.0"
        
        if extra_context is None:
            extra_context = {}
        extra_context['stats'] = stats
        
        return super().index(request, extra_context)

# Créer l'instance de l'admin site personnalisé
smartfirma_admin = SmartFirmaAdminSite(name='smartfirma_admin')

# Enregistrer les modèles avec l'admin personnalisé
from authentication.admin import UserAdmin
from analysis.admin import AnalysisLogAdmin
from chatbot.admin import ChatMessageAdmin
from messaging.admin import MessageAdmin

smartfirma_admin.register(User, UserAdmin)
smartfirma_admin.register(AnalysisLog, AnalysisLogAdmin)
smartfirma_admin.register(ChatMessage, ChatMessageAdmin)
smartfirma_admin.register(Message, MessageAdmin)
