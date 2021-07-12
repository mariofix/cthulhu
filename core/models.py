from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CoreUser(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)

    def __str__(self):
        return self.email


class Module(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.name
