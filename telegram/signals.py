from django.db.models.signals import (
    pre_save, post_save, pre_delete, post_delete,
)
from django.dispatch import receiver

from social_media_analyzer.globals import logger
from telegram import models

# @receiver(pre_save, sender=models.AddChannelRequest)
# def handle_presave(sender, **kwargs):
#     logger.info(f'\npresave: {str(sender)} : {kwargs}')
from utils.utils import prettify


@receiver(post_save, sender=models.AddChannelRequest)
def handle_postsave(sender, instance, created, update_fields, raw, **kwargs):
    # def handle_postsave(sender,**kwargs):
    logger.info(f"\npostsave: {str(sender)} : <{str(instance)}> : {kwargs}")


@receiver(pre_save, sender=models.Message)
def handle_presave(sender, instance, **kwargs):
    logger.info(f"\npresave: {str(sender)} : <{prettify(instance.__dict__)}> : {kwargs}")


@receiver(pre_delete, sender=models.Chat)
def handle_predelete(sender, instance, **kwargs):
    logger.info(f"\npre_delete: {str(sender)} : <{prettify(instance.__dict__)}> : {kwargs}")
    messages = models.Message.objects.filter(
        forward_from_chat=instance,
    )
    if messages:
        for message in messages:
            logger.info(message)
    # db_chat = models.Chat.objects.get(chat_id=instance.chat_id)
    # logger.info(db_chat.messages)
