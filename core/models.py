from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import (
    CharField,
    TextField,
    DateTimeField,
    EmailField,
)
from jsonfield import JSONField
from django.utils.translation import gettext as _


class TimeStampMixin(models.Model):
    created_at = DateTimeField(auto_now_add=True)
    modified_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CoreUser(AbstractUser):
    email = EmailField(unique=True)
    phone = CharField(max_length=150, null=True, unique=True, default=None)

    def __str__(self) -> str:
        return self.username


MSG_TYPES = (
    ("email", _("Email")),
    ("sms", _("SMS")),
    ("voice", _("Voice")),
    ("whatsapp", _("Whatsapp")),
    ("telegram", _("Telegram")),
    ("email_sync", _("Email (Sync)")),
    ("webpush", _("Browser Push")),
    ("url", _("HTTP/S")),
)
MSG_STATUSES = (
    ("not_sent", _("Not Sent")),
    ("sending", _("Sending")),
    ("sent", _("Sent")),
    ("rejected", _("Rejected")),
)


class Message(TimeStampMixin):
    sent_at = DateTimeField(null=True, default=None, blank=True)
    type = CharField(max_length=10, default="email", choices=MSG_TYPES)
    status = CharField(max_length=10, default="not_sent", choices=MSG_STATUSES)
    to = CharField(max_length=2048, null=False)
    orig = CharField(max_length=255, null=False)
    subject = CharField(max_length=180, null=False)
    text = TextField(null=True, blank=True, default=None)
    html = TextField(null=True, blank=True, default=None)
    headers = JSONField(null=True, default=None, blank=True)
    result = TextField(null=True, blank=True, default=None)

    def __str__(self) -> str:
        return self.to

    class Meta:
        verbose_name_plural = "Messages"
