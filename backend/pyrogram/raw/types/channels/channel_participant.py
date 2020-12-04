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


class ChannelParticipant(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.channels.ChannelParticipant`.

    Details:
        - Layer: ``120``
        - ID: ``0xd0d9b163``

    Parameters:
        participant: :obj:`ChannelParticipant <pyrogram.raw.base.ChannelParticipant>`
        users: List of :obj:`User <pyrogram.raw.base.User>`

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`channels.GetParticipant <pyrogram.raw.functions.channels.GetParticipant>`
    """

    __slots__: List[str] = ["participant", "users"]

    ID = 0xd0d9b163
    QUALNAME = "types.channels.ChannelParticipant"

    def __init__(self, *, participant: "raw.base.ChannelParticipant", users: List["raw.base.User"]) -> None:
        self.participant = participant  # ChannelParticipant
        self.users = users  # Vector<User>

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "ChannelParticipant":
        # No flags

        participant = TLObject.read(data)

        users = TLObject.read(data)

        return ChannelParticipant(participant=participant, users=users)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(self.participant.write())

        data.write(Vector(self.users))

        return data.getvalue()
