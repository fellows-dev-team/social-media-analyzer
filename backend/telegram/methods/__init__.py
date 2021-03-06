from .analyzers import Analyzers
from .base import Base
from .users import Users
from .chats import Chats
from .requests import Requests
from .messages_and_media import MessageAndMedia
from .users_and_chats import UsersAndChats
from .posts import Posts


class TelegramMethods(
    Analyzers,
    Base,
    Users,
    Chats,
    MessageAndMedia,
    Requests,
    UsersAndChats,
    Posts,

):
    pass
