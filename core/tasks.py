from celery import shared_task
from django.core.mail import EmailMessage


@shared_task
def send_email(email_subject, html_content, email_from, email_to, headers):
    # enviar siempre texto con html juntos
    email = EmailMessage(
        email_subject,
        html_content,
        email_from,
        [email_to],
    )
    email.content_subtype = "html"
    email.send()

    return True


@shared_task
def send_request(verb, url, data, headers):

    return True
