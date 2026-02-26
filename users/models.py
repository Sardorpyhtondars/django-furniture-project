from django.db import models
from shared.models import BaseModel

class User(BaseModel):
    first_name = models.CharField(max_length=32, default='')
    last_name = models.CharField(max_length=32, default='')
    username = models.CharField(max_length=32, unique=True, default='')
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=16)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name, self.last_name

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'