from django.contrib import admin
from .models import Module, CoreUser, Phone
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .forms import CoreUserCreationForm, CoreUserChangeForm
from django.utils.translation import gettext_lazy as _


class CoreUserAdmin(UserAdmin):
    add_form = CoreUserCreationForm
    form = CoreUserChangeForm
    model = CoreUser
    list_display = [
        "email",
        "username",
        "country",
    ]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "country", "tz"),
            },
        ),
    )
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            _("Personal info"),
            {"fields": ("first_name", "last_name", "email", "country", "tz")},
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )


class PhoneAdmin(admin.ModelAdmin):
    list_display = ("number", "user", "date_created", "is_active")
    list_editable = ("is_active",)


admin.site.register(Module)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(CoreUser, CoreUserAdmin)
