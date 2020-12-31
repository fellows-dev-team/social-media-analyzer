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


class EditGroupCallMember(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``122``
        - ID: ``0x63146ae4``

    Parameters:
        call: :obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`
        user_id: :obj:`InputUser <pyrogram.raw.base.InputUser>`
        muted (optional): ``bool``

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["call", "user_id", "muted"]

    ID = 0x63146ae4
    QUALNAME = "functions.phone.EditGroupCallMember"

    def __init__(self, *, call: "raw.base.InputGroupCall", user_id: "raw.base.InputUser",
                 muted: Union[None, bool] = None) -> None:
        self.call = call  # InputGroupCall
        self.user_id = user_id  # InputUser
        self.muted = muted  # flags.0?true

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "EditGroupCallMember":
        flags = Int.read(data)

        muted = True if flags & (1 << 0) else False
        call = TLObject.read(data)

        user_id = TLObject.read(data)

        return EditGroupCallMember(call=call, user_id=user_id, muted=muted)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.muted else 0
        data.write(Int(flags))

        data.write(self.call.write())

        data.write(self.user_id.write())

        return data.getvalue()