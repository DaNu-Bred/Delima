from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Role(models.TextChoices):
        CLIENT = 'client', 'клиент'
        COMPANY = 'company', 'компания'
        COURIER = 'courier', 'курьер'

    role = models.CharField("Роль", max_length=20, choices=Role.choices, default=Role.CLIENT)
