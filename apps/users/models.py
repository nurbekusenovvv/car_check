from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    profile_image = models.ImageField(
        upload_to='profile_image/',
        verbose_name='Фотография профиля',
        blank=True, null=True
    )
    
    phone_number = models.CharField(
        max_length=100,
        verbose_name='Телефонный номер'
    )
    verify = models.BooleanField(
        default=False,
        verbose_name='Верификация подьзователя',
    )
    
    def __str__(self):
        return self.username    
    
    class Meta:
        verbose_name = "Пользователь",
        verbose_name_plural = 'Пользователи'