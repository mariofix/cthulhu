from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from core.models import Message
from core.tasks import send_msg
import logging

logger = logging.getLogger("django")


@receiver(post_save, sender=Message)
def post_save_mensaje(sender, instance, created, **kwargs):
    if created and instance.status == "not_sent":
        logger.debug(f"send_msg(msg={instance})")
        return send_msg(msg=instance)
        # return True
