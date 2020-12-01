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


class MessageService(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.Message`.

    Details:
        - Layer: ``117``
        - ID: ``0x9e19a1f6``

    Parameters:
        id: ``int`` ``32-bit``
        to_id: :obj:`Peer <pyrogram.raw.base.Peer>`
        date: ``int`` ``32-bit``
        action: :obj:`MessageAction <pyrogram.raw.base.MessageAction>`
        out (optional): ``bool``
        mentioned (optional): ``bool``
        media_unread (optional): ``bool``
        silent (optional): ``bool``
        post (optional): ``bool``
        legacy (optional): ``bool``
        from_id (optional): ``int`` ``32-bit``
        reply_to_msg_id (optional): ``int`` ``32-bit``
    """

    __slots__: List[str] = ["id", "to_id", "date", "action", "out", "mentioned", "media_unread", "silent", "post",
                            "legacy", "from_id", "reply_to_msg_id"]

    ID = 0x9e19a1f6
    QUALNAME = "types.MessageService"

    def __init__(self, *, id: int, to_id: "raw.base.Peer", date: int, action: "raw.base.MessageAction",
                 out: Union[None, bool] = None, mentioned: Union[None, bool] = None,
                 media_unread: Union[None, bool] = None, silent: Union[None, bool] = None,
                 post: Union[None, bool] = None, legacy: Union[None, bool] = None, from_id: Union[None, int] = None,
                 reply_to_msg_id: Union[None, int] = None) -> None:
        self.id = id  # int
        self.to_id = to_id  # Peer
        self.date = date  # int
        self.action = action  # MessageAction
        self.out = out  # flags.1?true
        self.mentioned = mentioned  # flags.4?true
        self.media_unread = media_unread  # flags.5?true
        self.silent = silent  # flags.13?true
        self.post = post  # flags.14?true
        self.legacy = legacy  # flags.19?true
        self.from_id = from_id  # flags.8?int
        self.reply_to_msg_id = reply_to_msg_id  # flags.3?int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "MessageService":
        flags = Int.read(data)

        out = True if flags & (1 << 1) else False
        mentioned = True if flags & (1 << 4) else False
        media_unread = True if flags & (1 << 5) else False
        silent = True if flags & (1 << 13) else False
        post = True if flags & (1 << 14) else False
        legacy = True if flags & (1 << 19) else False
        id = Int.read(data)

        from_id = Int.read(data) if flags & (1 << 8) else None
        to_id = TLObject.read(data)

        reply_to_msg_id = Int.read(data) if flags & (1 << 3) else None
        date = Int.read(data)

        action = TLObject.read(data)

        return MessageService(id=id, to_id=to_id, date=date, action=action, out=out, mentioned=mentioned,
                              media_unread=media_unread, silent=silent, post=post, legacy=legacy, from_id=from_id,
                              reply_to_msg_id=reply_to_msg_id)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.out is not None else 0
        flags |= (1 << 4) if self.mentioned is not None else 0
        flags |= (1 << 5) if self.media_unread is not None else 0
        flags |= (1 << 13) if self.silent is not None else 0
        flags |= (1 << 14) if self.post is not None else 0
        flags |= (1 << 19) if self.legacy is not None else 0
        flags |= (1 << 8) if self.from_id is not None else 0
        flags |= (1 << 3) if self.reply_to_msg_id is not None else 0
        data.write(Int(flags))

        data.write(Int(self.id))

        if self.from_id is not None:
            data.write(Int(self.from_id))

        data.write(self.to_id.write())

        if self.reply_to_msg_id is not None:
            data.write(Int(self.reply_to_msg_id))

        data.write(Int(self.date))

        data.write(self.action.write())

        return data.getvalue()