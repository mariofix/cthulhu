from django.db import models
from django.contrib.auth.models import AbstractUser


class CoreUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=150, null=True, unique=True, default=None)

    def __str__(self) -> str:
        return self.username
