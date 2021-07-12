from django.contrib import admin
from .models import Module, CoreUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .forms import CoreUserCreationForm, CoreUserChangeForm


class CoreUserAdmin(UserAdmin):
    add_form = CoreUserCreationForm
    form = CoreUserChangeForm
    model = CoreUser
    list_display = [
        "email",
        "username",
    ]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )


admin.site.register(Module)
admin.site.register(CoreUser, CoreUserAdmin)
