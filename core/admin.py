from django.contrib import admin
from .models import CoreUser
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
        "phone",
    ]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "phone", "password1", "password2"),
            },
        ),
    )
    fieldsets = (
        (None, {"fields": ("username", "password", "email", "phone")}),
        (
            "Personal info",
            {"fields": ("first_name", "last_name")},
        ),
        (
            "Permissions",
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
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )


admin.site.register(CoreUser, CoreUserAdmin)
