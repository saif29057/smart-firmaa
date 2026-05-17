from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'role', 'phone', 'is_active', 'created_at']
    list_filter = ['role', 'is_active', 'is_staff', 'created_at']
    search_fields = ['username', 'email', 'first_name', 'last_name', 'phone']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Informations personnelles', {
            'fields': ('username', 'password', 'first_name', 'last_name', 'email', 'phone')
        }),
        ('Rôle et permissions', {
            'fields': ('role', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Avatar', {
            'fields': ('avatar',)
        }),
        ('Dates', {
            'fields': ('created_at', 'updated_at', 'last_login', 'date_joined')
        }),
    )
    
    add_fieldsets = (
        ('Informations personnelles', {
            'fields': ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        }),
        ('Rôle', {
            'fields': ('role', 'phone')
        }),
    )
    
    ordering = ['-created_at']
    date_hierarchy = 'created_at'
