from django.db import models


class Modules(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.name