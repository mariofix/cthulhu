from celery import shared_task
from django.core.mail import EmailMultiAlternatives
import logging
import requests

logger = logging.getLogger("django")


@shared_task
def send_email(
    email_subject: str,
    txt_content: str,
    html_content: str,
    email_to: str,
    headers: dict,
):
    logger.info(f"Trying to send an email to: {email_to}")
    email = EmailMultiAlternatives(
        subject=f"{email_subject}",
        body=txt_content,
        to=[f"{email_to}"],
        headers=headers,
    )
    email.attach_alternative(html_content, "text/html")
    try:
        email.send(fail_silently=False)
    except Exception as e:
        logger.warn(f"Unable to send the email: {e}")
        return False
    else:
        logger.info(f"Email Sent!")
        return True


@shared_task
def send_request(verb: str, url: str, data: dict, headers: dict):
    logger.info(f"Requesting {verb}: {url}")
    webcall = requests.request(verb, url, data=data, headers=headers)
    return [webcall.status_code, webcall.text]
