from django.contrib import admin
from users.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'email', 'is_active', 'created_at']
    search_fields = ['username', 'first_name', 'last_name', 'email']
    list_filter = ['created_at', 'is_active']