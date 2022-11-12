from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from core.models import Message
from django.utils import timezone
import logging
import requests

logger = logging.getLogger("django")


@shared_task
def send_email(msg_id: int = None) -> dict:
    """
    Sends an email using django.core.mail
    """
    if not msg_id:
        raise Exception(f"{msg_id=}")

    msg = Message.objects.filter(id=msg_id)
    if msg:
        msg = msg.get()

    if msg.status != "not_sent":
        raise Exception(f"Message with {msg.status}, exiting.")

    msg.status = "sending"
    msg.save()
    logger.info(f"Sending email to: {msg.to}")
    email = EmailMultiAlternatives(
        subject=f"{settings.EMAIL_SUBJECT_PREFIX}{msg.subject}",
        body=msg.text,
        to=[msg.to],
        headers=msg.headers,
    )
    email.attach_alternative(msg.html, "text/html")
    try:
        email.send(fail_silently=False)
    except Exception as e:
        msg.status = "rejected"
        msg.sent_at = timezone.now()
        msg.result = e
        msg.save()
        raise Exception(f"Unable to send the email: {e}")
    else:
        logger.info(f"Correo Enviado!")
        msg.status = "sent"
        msg.sent_at = timezone.now()
        msg.result = f"{email=}"
        msg.save()
        return {"type": msg.type, "to": msg.to, "sent_at": msg.sent_at}


@shared_task
def send_https_request(msg_id: int = None) -> dict:
    """
    Sends an HTTP/S request
    """
    if not msg_id:
        raise Exception(f"{msg_id=}")

    msg = Message.objects.filter(id=msg_id)
    if msg:
        msg = msg.get()

    if msg.status != "not_sent":
        raise Exception(f"Message with {msg.status}, exiting.")

    msg.status = "sending"
    msg.save()
    params = json.loads(msg.text.replace("'", '"')) if msg.text else None
    data = json.loads(msg.html.replace("'", '"')) if msg.html else None

    logger.info(f"{msg.subject=} {msg.to=} {params=} {data=} {msg.headers=}")
    call = requests.request(
        msg.subject,
        msg.to,
        params=params,
        data=data,
        headers=msg.headers,
    )
    msg.status = "sent" if call.status_code in [200, 201] else "rejected"
    msg.fecha_envio = timezone.now()
    msg.result = {
        "status": call.status_code,
        "headers": call.headers,
        "data": call.text,
    }
    msg.save()
    return {
        "verb": msg.subject,
        "url": call.url,
        "status_code": call.status_code,
    }


def send_msg(msg: Message) -> bool:
    """
    process the message send
    """
    if msg.type == "email":
        logger.info(f"send_email.apply_async(kwargs={{msg_id: {msg.id}}}, countdown=5)")
        send_email.apply_async(kwargs={"msg_id": msg.id}, countdown=5)
        return True
    if msg.type == "url":
        logger.info(
            f"send_https_request.apply_async(kwargs={{msg_id: {msg.id}}}, countdown=5)"
        )
        send_https_request.apply_async(kwargs={"msg_id": msg.id}, countdown=5)
        return True
    elif msg.type == "email_sync":
        logger.info(f"return send_email(msg_id={msg.id})")
        send_email(msg_id=msg.id)
        return True
    elif msg.type == "sms":
        pass
    elif msg.type == "voz":
        pass
    elif msg.type == "whatsapp":
        pass
    elif msg.type == "telegram":
        pass
    elif msg.type == "webpush":
        pass
    return False
