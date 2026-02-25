from django.contrib import admin
from about.models import TeamMember

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'profession']
    search_fields = ['full_name', 'profession']