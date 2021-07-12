from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

COUNTRIES = (
    ("CL", "Chile"),
    ("AR", "Argentina"),
    ("PE", "Peru"),
    ("EC", "Ecuador"),
    ("MX", "Mexico"),
    ("CO", "Colombia"),
    ("US", "USA"),
)
TIMEZONES = (
    ("America/Santiago", "America/Santiago"),
    ("America/Buenos_Aires", "America/Buenos_Aires"),
    ("America/Lima", "America/Lima"),
    ("America/Guayaquil", "America/Guayaquil"),
    ("America/Mexico_City", "America/Mexico_City"),
    ("America/Bogota", "America/Bogota"),
    ("America/New_York", "America/New_York"),
    ("America/Los_Angeles", "America/Los_Angeles"),
    ("America/Chicago", "America/Chicago"),
)


class CoreUser(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    country = models.CharField(
        _("country"), max_length=3, null=False, default="CL", choices=COUNTRIES
    )
    tz = models.CharField(
        _("timezone"),
        max_length=255,
        null=False,
        default="America/Santiago",
        choices=TIMEZONES,
    )

    def __str__(self) -> str:
        return self.email


class Phone(models.Model):
    number = models.CharField(max_length=16, unique=True)
    date_created = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(CoreUser, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.number


class Module(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.name
