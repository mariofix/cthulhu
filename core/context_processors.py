from django.conf import settings
from django.apps import apps
from os.path import isfile
import logging

logger = logging.getLogger("django")


def cthulhu(request):
    modulos = []
    for app in apps.get_app_configs():
        try:
            is_module = app.is_module
        except AttributeError:
            logger.debug(f"{app.name} is not a Cthulhu Module")
        else:
            del is_module
            app_menu = f"{app.name}/templates/{app.name}/menu.html"
            if isfile(app_menu):
                modulos.append({"name": app.name, "menu": f"{app.name}/menu.html"})

    context = {
        "app_name": settings.BATON["SITE_HEADER"],
        "app_modules": modulos,
    }
    return context
