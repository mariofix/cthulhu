from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from thankyou import give_thanks
from .forms import CoreUserCreationForm
from django_registration.backends.activation.views import RegistrationView


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
        html_content = render_to_string(
            template_name=self.email_body_template_html,
            context=context,
            request=self.request,
        )
        email = EmailMessage(
            subject,
            html_content,
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            [settings.ADMINS[0][1]],
            headers={"X-Activation-Url": self.get_activation_link(context)},
        )
        email.content_subtype = "html"
        email.send()

    def get_activation_link(self, context):
        return f"{context['scheme']}://{context['site']}/accounts/activate/{context['activation_key']}"


def index(request):
    return render(request, "hello.html", {"thanks": give_thanks()})


def postlogin(request):
    # Verificamos si es primer login para ir a buscar su informacion a API
    if request.user != "AnonymousUser":
        print(request.user.email)
        print(request.user.is_active)
        return redirect("/dashboard")
    else:
        return redirect("/login")


def dashboard(request):
    # traemos toda la informacion adicional
    # crear clients ids y esas cosas
    if request.user != "AnonymousUser":
        print(request.user.email)
        print(request.user.is_active)
    return render(request, "core/dashboard.html")


def profile(request):
    return render(request, "core/profile.html")


def help(request):
    return render(request, "core/help.html")
