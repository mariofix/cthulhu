from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext as _
from core.forms import CoreUserCreationForm, CoreUserChangeForm
from core.models import CoreUser, Message
from core.tasks import send_msg
import logging

logger = logging.getLogger("django")


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


class MessageFilter(admin.ModelAdmin):
    list_display = ("to", "type", "status", "subject")
    readonly_fields = (
        "sent_at",
        "modified_at",
        "created_at",
    )
    list_per_page = 20
    actions = ["resend_message"]

    @admin.action(description=_("Resend selected messages"))
    def resend_message(self, request, queryset):
        for msg in queryset.all():
            logger.info(f"Changing {msg.status=} to not_sent")
            msg.status = "not_sent"
            msg.save()
            if send_msg(msg):
                self.message_user(
                    request, _("Message succesfully queued"), messages.SUCCESS
                )
            else:
                self.message_user(request, _("An error has ocurred"), messages.ERROR)
        return True


admin.site.register(CoreUser, CoreUserAdmin)
admin.site.register(Message, MessageFilter)
