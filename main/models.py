from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .manager import UserManager



class User(AbstractBaseUser,PermissionsMixin):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='main_user_set',
        blank=True,
        verbose_name='группы',
        help_text='Группы, к которым принадлежит пользователь.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='main_user_permissions_set',
        blank=True,
        verbose_name='права доступа',
        help_text='Права, предоставленные пользователю.'
    )

    class Role(models.TextChoices):
        ADMIN = "admin", "Админ"
        MODERATOR = "moderator", "Модератор"
        USER = "user", "Пользователь"
       

    email=models.EmailField(unique=True)
    first_name=models.CharField(max_length=30, blank=True)
    last_name=models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=20, blank=True)

class Meta:
    verbose_name = "Пользователь"
    verbose_name_plural = "Пользователи"
