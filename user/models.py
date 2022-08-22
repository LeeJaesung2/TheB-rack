from django.db import models

class User(models.Model):
    social_id = models.CharField(max_length=100, primary_key=True, unique=True, verbose_name='소셜사용자_id')
    social_type = models.CharField(max_length=20, verbose_name='소셜 타입')
    email = models.EmailField(max_length=100, null=True, verbose_name='이메일')
    def __str__(self):
        return self.social_id