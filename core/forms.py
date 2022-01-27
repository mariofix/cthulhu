from django_registration.forms import RegistrationForm
from django.contrib.auth.forms import UserChangeForm
from core.models import CoreUser


class CoreUserCreationForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = CoreUser
        fields = ("username", "email", "phone")


class CoreUserChangeForm(UserChangeForm):
    class Meta:
        model = CoreUser
        fields = ("username", "email", "phone")
