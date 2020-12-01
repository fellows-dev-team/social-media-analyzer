#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-2020 Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Union, Any


# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class SetBotCallbackAnswer(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``117``
        - ID: ``0xd58f130a``

    Parameters:
        query_id: ``int`` ``64-bit``
        cache_time: ``int`` ``32-bit``
        alert (optional): ``bool``
        message (optional): ``str``
        url (optional): ``str``

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["query_id", "cache_time", "alert", "message", "url"]

    ID = 0xd58f130a
    QUALNAME = "functions.messages.SetBotCallbackAnswer"

    def __init__(self, *, query_id: int, cache_time: int, alert: Union[None, bool] = None,
                 message: Union[None, str] = None, url: Union[None, str] = None) -> None:
        self.query_id = query_id  # long
        self.cache_time = cache_time  # int
        self.alert = alert  # flags.1?true
        self.message = message  # flags.0?string
        self.url = url  # flags.2?string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "SetBotCallbackAnswer":
        flags = Int.read(data)

        alert = True if flags & (1 << 1) else False
        query_id = Long.read(data)

        message = String.read(data) if flags & (1 << 0) else None
        url = String.read(data) if flags & (1 << 2) else None
        cache_time = Int.read(data)

        return SetBotCallbackAnswer(query_id=query_id, cache_time=cache_time, alert=alert, message=message, url=url)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.alert is not None else 0
        flags |= (1 << 0) if self.message is not None else 0
        flags |= (1 << 2) if self.url is not None else 0
        data.write(Int(flags))

        data.write(Long(self.query_id))

        if self.message is not None:
            data.write(String(self.message))

        if self.url is not None:
            data.write(String(self.url))

        data.write(Int(self.cache_time))

        return data.getvalue()