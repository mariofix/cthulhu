from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext as _
from core.forms import CoreUserCreationForm, CoreUserChangeForm
from core.models import CoreUser


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
            _("Personal info"),
            {"fields": ("first_name", "last_name")},
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


admin.site.register(CoreUser, CoreUserAdmin)
