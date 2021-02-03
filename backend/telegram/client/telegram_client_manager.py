import multiprocessing as mp
import threading
from typing import List, Union

import arrow

import pyrogram
from core.globals import logger
from db.database_manager import DataBaseManager
from pyrogram import raw, idle
from pyrogram import types
#############################################
from pyrogram.handlers import DisconnectHandler, MessageHandler, RawUpdateHandler
#############################################
from telegram.client.client_manager import *

clients_lock = threading.RLock()

_update = Union[
    raw.types.UpdateBotCallbackQuery, raw.types.UpdateBotInlineQuery, raw.types.UpdateBotInlineSend,
    raw.types.UpdateBotPrecheckoutQuery, raw.types.UpdateBotShippingQuery, raw.types.UpdateBotWebhookJSON,
    raw.types.UpdateBotWebhookJSONQuery, raw.types.UpdateChannel, raw.types.UpdateChannelAvailableMessages,
    raw.types.UpdateChannelMessageForwards, raw.types.UpdateChannelMessageViews, raw.types.UpdateChannelParticipant,
    raw.types.UpdateChannelReadMessagesContents, raw.types.UpdateChannelTooLong, raw.types.UpdateChannelUserTyping,
    raw.types.UpdateChannelWebPage, raw.types.UpdateChat, raw.types.UpdateChatDefaultBannedRights,
    raw.types.UpdateChatParticipantAdd, raw.types.UpdateChatParticipantAdmin, raw.types.UpdateChatParticipantDelete,
    raw.types.UpdateChatParticipants, raw.types.UpdateChatUserTyping, raw.types.UpdateConfig,
    raw.types.UpdateContactsReset, raw.types.UpdateDcOptions, raw.types.UpdateDeleteChannelMessages,
    raw.types.UpdateDeleteMessages, raw.types.UpdateDeleteScheduledMessages, raw.types.UpdateDialogFilter,
    raw.types.UpdateDialogFilterOrder, raw.types.UpdateDialogFilters, raw.types.UpdateDialogPinned,
    raw.types.UpdateDialogUnreadMark, raw.types.UpdateDraftMessage, raw.types.UpdateEditChannelMessage,
    raw.types.UpdateEditMessage, raw.types.UpdateEncryptedChatTyping, raw.types.UpdateEncryptedMessagesRead,
    raw.types.UpdateEncryption, raw.types.UpdateFavedStickers, raw.types.UpdateFolderPeers,
    raw.types.UpdateGeoLiveViewed, raw.types.UpdateGroupCall, raw.types.UpdateGroupCallParticipants,
    raw.types.UpdateInlineBotCallbackQuery, raw.types.UpdateLangPack, raw.types.UpdateLangPackTooLong,
    raw.types.UpdateLoginToken, raw.types.UpdateMessageID, raw.types.UpdateMessagePoll,
    raw.types.UpdateMessagePollVote, raw.types.UpdateNewChannelMessage, raw.types.UpdateNewEncryptedMessage,
    raw.types.UpdateNewMessage, raw.types.UpdateNewScheduledMessage, raw.types.UpdateNewStickerSet,
    raw.types.UpdateNotifySettings, raw.types.UpdatePeerBlocked, raw.types.UpdatePeerLocated,
    raw.types.UpdatePeerSettings, raw.types.UpdatePhoneCall, raw.types.UpdatePhoneCallSignalingData,
    raw.types.UpdatePinnedChannelMessages, raw.types.UpdatePinnedDialogs, raw.types.UpdatePinnedMessages,
    raw.types.UpdatePrivacy, raw.types.UpdatePtsChanged, raw.types.UpdateReadChannelDiscussionInbox,
    raw.types.UpdateReadChannelDiscussionOutbox, raw.types.UpdateReadChannelInbox, raw.types.UpdateReadChannelOutbox,
    raw.types.UpdateReadFeaturedStickers, raw.types.UpdateReadHistoryInbox, raw.types.UpdateReadHistoryOutbox,
    raw.types.UpdateReadMessagesContents, raw.types.UpdateRecentStickers, raw.types.UpdateSavedGifs,
    raw.types.UpdateServiceNotification, raw.types.UpdateStickerSets, raw.types.UpdateStickerSetsOrder,
    raw.types.UpdateTheme, raw.types.UpdateUserName, raw.types.UpdateUserPhone,
    raw.types.UpdateUserPhoto, raw.types.UpdateUserStatus, raw.types.UpdateUserTyping,
    raw.types.UpdateWebPage
]


class TelegramClientManager:
    def __init__(
            self,
            *,
            clients: List['pyrogram.Client']
    ):
        self.db = DataBaseManager()
        self.clients = clients

    def on_message(
            self,
            client: 'pyrogram.Client',
            message: 'types.Message'
    ):
        logger.info(f"in on_message : {threading.current_thread()}")
        if message.type != 'empty':
            db_account = self.db.telegram.get_telegram_account_by_session_name(
                session_name=client.session_name
            )
            db_chat = self.db.telegram.get_chat_by_id(chat_id=message.chat.id)
            if db_chat is None:
                raw_chat = client.get_chat(message.chat.id)
                db_chat = self.db.telegram.get_updated_chat(
                    raw_chat=raw_chat,
                    db_telegram_account=db_account,

                    downloader=client.download_media
                )
                if db_chat is None:
                    return

            self.db.telegram.get_updated_message(
                db_chat=db_chat,
                raw_message=message,
                logger_account=db_account,
            )

    def on_raw_update(
            self,
            client: 'pyrogram.Client',
            raw_update: '_update',
            users: List['types.User'],
            chats: List['types.Chat']
    ):
        logger.info(f"in on_raw_update : {threading.current_thread()}")

    def run(self) -> None:
        logger.info(mp.current_process().name)
        logger.info(threading.current_thread())

        for client in map(get_client, client_names, [False] * len(client_names)):
            client.start()
            with clients_lock:
                self.clients.append(client)

            me = str(client.get_me())
            logger.info(me)

            client.add_handler(DisconnectHandler(self.on_disconnect))
            client.add_handler(MessageHandler(self.on_message))
            client.add_handler(RawUpdateHandler(self.on_raw_update))

        idle()
        with clients_lock:
            for client in self.clients:
                client.stop()

    @staticmethod
    def on_disconnect(client: 'pyrogram.Client'):
        logger.info(f"client {client.session_name} disconnected @ {arrow.utcnow()}")
