from typing import Optional

from django.db import transaction

from db.scaffold import Scaffold
from telegram import models as tg_models
from pyrogram import types


class GetUpdatedMessage(Scaffold):

    def get_updated_message(
            self,
            *,
            db_chat: 'tg_models.Chat',
            raw_message: types.Message,
            logger_account: "tg_models.TelegramAccount",
            create_entities: bool = True
    ) -> Optional['tg_models.Message']:
        if db_chat is None or raw_message is None or logger_account is None:
            return None

        with transaction.atomic():
            db_message = self.tg_models.Message.objects.update_or_create_from_raw(
                db_chat=db_chat,
                raw_message=raw_message,
                logger_account=logger_account,
            )

            if create_entities and db_message is not None:
                self.get_updated_message_entities(
                    db_message=db_message,
                    raw_message=raw_message,
                )
                self.get_updated_message_entity_types(
                    db_message=db_message,
                    raw_message=raw_message,
                )

            return db_message
