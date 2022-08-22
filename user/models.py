from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    social_type = models.CharField(max_length=20, verbose_name='소셜 타입')
    def __str__(self):
        return self.username