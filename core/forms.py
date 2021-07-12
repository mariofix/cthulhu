from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CoreUser


class CoreUserCreationForm(UserCreationForm):
    class Meta:
        model = CoreUser
        fields = ("username", "email")


class CoreUserChangeForm(UserChangeForm):
    class Meta:
        model = CoreUser
        fields = ("username", "email")
