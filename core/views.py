from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from django_registration.backends.activation.views import RegistrationView
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.forms import CoreUserCreationForm
from core.models import CoreUser
from core.tasks import send_email
from thankyou import give_thanks
import logging

logger = logging.getLogger("django")


class CustomRegistrationView(RegistrationView):
    # From https://github.com/ubernostrum/django-registration/issues/208
    template_name = "django_registration/registration_form.html"
    form_class = CoreUserCreationForm
    email_subject_template = "django_registration/activation_email_subject.txt"
    email_body_template_txt = "django_registration/activation_email_body.txt"
    email_body_template_html = "django_registration/activation_email_body.html"
    success_url = reverse_lazy("django_registration_complete")

    def send_activation_email(self, user):
        """
        Custom method to enable HTML activation emails.
        """
        activation_key = self.get_activation_key(user)
        context = self.get_email_context(activation_key)
        context["user"] = user
        subject = render_to_string(
            template_name=self.email_subject_template,
            context=context,
            request=self.request,
        )
        # Force subject to a single line to avoid header-injection
        # issues.
        subject = "".join(subject.splitlines())
        txt_content = render_to_string(
            template_name=self.email_body_template_txt,
            context=context,
            request=self.request,
        )
        html_content = render_to_string(
            template_name=self.email_body_template_html,
            context=context,
            request=self.request,
        )
        send_email.apply_async(
            args=[
                subject,
                txt_content,
                html_content,
                user.email,
                {"X-Activation-Url": self.get_activation_link(context)},
            ]
        )

    def get_activation_link(self, context):
        return f"{context['scheme']}://{context['site']}/accounts/activate/{context['activation_key']}"


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model = CoreUser
    fields = ["username", "first_name", "last_name", "email", "phone"]
    template_name = "core/profile.html"
    success_url = reverse_lazy("profile")

    def get_object(self, queryset=None):
        return self.request.user


class HelpView(TemplateView):
    template_name = "core/help.html"


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "core/dashboard.html"


def index(request):
    return render(request, "hello.html", {"thanks": give_thanks()})


@login_required
def postlogin(request):
    # Pre-flight checks
    logger.info("postlogin")
    bye = "/dashboard"
    return redirect(bye)
