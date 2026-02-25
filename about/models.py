from django.db import models
from shared.models import BaseModel

class TeamMember(BaseModel):
    full_name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    info = models.TextField()

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'team_members'
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'