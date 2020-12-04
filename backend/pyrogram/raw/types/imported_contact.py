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


class ImportedContact(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.ImportedContact`.

    Details:
        - Layer: ``120``
        - ID: ``0xd0028438``

    Parameters:
        user_id: ``int`` ``32-bit``
        client_id: ``int`` ``64-bit``
    """

    __slots__: List[str] = ["user_id", "client_id"]

    ID = 0xd0028438
    QUALNAME = "types.ImportedContact"

    def __init__(self, *, user_id: int, client_id: int) -> None:
        self.user_id = user_id  # int
        self.client_id = client_id  # long

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "ImportedContact":
        # No flags

        user_id = Int.read(data)

        client_id = Long.read(data)

        return ImportedContact(user_id=user_id, client_id=client_id)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Int(self.user_id))

        data.write(Long(self.client_id))

        return data.getvalue()
