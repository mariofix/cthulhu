from baton.autodiscover import admin
from django.urls import path, include
import debug_toolbar

urlpatterns = [
    path("admin.site/", admin.site.urls),
    path("baton/", include("baton.urls")),
    path("", include("core.urls")),
    path("__debug__/", include(debug_toolbar.urls)),
]
