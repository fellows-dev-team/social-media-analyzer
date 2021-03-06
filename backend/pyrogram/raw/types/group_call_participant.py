#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-2021 Dan <https://github.com/delivrance>
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


class GroupCallParticipant(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.GroupCallParticipant`.

    Details:
        - Layer: ``123``
        - ID: ``0x64c62a15``

    Parameters:
        user_id: ``int`` ``32-bit``
        date: ``int`` ``32-bit``
        source: ``int`` ``32-bit``
        muted (optional): ``bool``
        left (optional): ``bool``
        can_self_unmute (optional): ``bool``
        just_joined (optional): ``bool``
        versioned (optional): ``bool``
        min (optional): ``bool``
        muted_by_you (optional): ``bool``
        volume_by_admin (optional): ``bool``
        active_date (optional): ``int`` ``32-bit``
        volume (optional): ``int`` ``32-bit``
    """

    __slots__: List[str] = ["user_id", "date", "source", "muted", "left", "can_self_unmute", "just_joined", "versioned",
                            "min", "muted_by_you", "volume_by_admin", "active_date", "volume"]

    ID = 0x64c62a15
    QUALNAME = "types.GroupCallParticipant"

    def __init__(self, *, user_id: int, date: int, source: int, muted: Union[None, bool] = None,
                 left: Union[None, bool] = None, can_self_unmute: Union[None, bool] = None,
                 just_joined: Union[None, bool] = None, versioned: Union[None, bool] = None,
                 min: Union[None, bool] = None, muted_by_you: Union[None, bool] = None,
                 volume_by_admin: Union[None, bool] = None, active_date: Union[None, int] = None,
                 volume: Union[None, int] = None) -> None:
        self.user_id = user_id  # int
        self.date = date  # int
        self.source = source  # int
        self.muted = muted  # flags.0?true
        self.left = left  # flags.1?true
        self.can_self_unmute = can_self_unmute  # flags.2?true
        self.just_joined = just_joined  # flags.4?true
        self.versioned = versioned  # flags.5?true
        self.min = min  # flags.8?true
        self.muted_by_you = muted_by_you  # flags.9?true
        self.volume_by_admin = volume_by_admin  # flags.10?true
        self.active_date = active_date  # flags.3?int
        self.volume = volume  # flags.7?int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "GroupCallParticipant":
        flags = Int.read(data)

        muted = True if flags & (1 << 0) else False
        left = True if flags & (1 << 1) else False
        can_self_unmute = True if flags & (1 << 2) else False
        just_joined = True if flags & (1 << 4) else False
        versioned = True if flags & (1 << 5) else False
        min = True if flags & (1 << 8) else False
        muted_by_you = True if flags & (1 << 9) else False
        volume_by_admin = True if flags & (1 << 10) else False
        user_id = Int.read(data)

        date = Int.read(data)

        active_date = Int.read(data) if flags & (1 << 3) else None
        source = Int.read(data)

        volume = Int.read(data) if flags & (1 << 7) else None
        return GroupCallParticipant(user_id=user_id, date=date, source=source, muted=muted, left=left,
                                    can_self_unmute=can_self_unmute, just_joined=just_joined, versioned=versioned,
                                    min=min, muted_by_you=muted_by_you, volume_by_admin=volume_by_admin,
                                    active_date=active_date, volume=volume)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.muted else 0
        flags |= (1 << 1) if self.left else 0
        flags |= (1 << 2) if self.can_self_unmute else 0
        flags |= (1 << 4) if self.just_joined else 0
        flags |= (1 << 5) if self.versioned else 0
        flags |= (1 << 8) if self.min else 0
        flags |= (1 << 9) if self.muted_by_you else 0
        flags |= (1 << 10) if self.volume_by_admin else 0
        flags |= (1 << 3) if self.active_date is not None else 0
        flags |= (1 << 7) if self.volume is not None else 0
        data.write(Int(flags))

        data.write(Int(self.user_id))

        data.write(Int(self.date))

        if self.active_date is not None:
            data.write(Int(self.active_date))

        data.write(Int(self.source))

        if self.volume is not None:
            data.write(Int(self.volume))

        return data.getvalue()
