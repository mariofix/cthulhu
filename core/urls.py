from django.urls import path, include
from core import views
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.conf.urls import handler400, handler403, handler404, handler500

urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
    path("profile/", views.UpdateProfileView.as_view(), name="profile"),
    path("help/", views.HelpView.as_view(), name="help"),
    path("accounts/postlogin/", views.postlogin, name="postlogin"),
    path(
        "accounts/register/",
        views.CustomRegistrationView.as_view(),
        name="django_registration_register",
    ),
    path(
        "accounts/password_reset/",
        PasswordResetView.as_view(
            template_name="registration/password_reset_form.html",
            html_email_template_name="registration/new_password_reset_email.html",
        ),
        name="password_reset",
    ),
    path(
        "accounts/password_reset/done/",
        PasswordResetDoneView.as_view(
            template_name="registration/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "accounts/reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="registration/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "accounts/reset/done/",
        PasswordResetCompleteView.as_view(
            template_name="registration/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path("accounts/", include("django_registration.backends.activation.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
]

handler400 = "core.errorviews.handle400"
handler403 = "core.errorviews.handle403"
handler404 = "core.errorviews.handle404"
handler500 = "core.errorviews.handle500"
