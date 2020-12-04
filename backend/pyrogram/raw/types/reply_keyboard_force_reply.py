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


class ReplyKeyboardForceReply(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.ReplyMarkup`.

    Details:
        - Layer: ``120``
        - ID: ``0xf4108aa0``

    Parameters:
        single_use (optional): ``bool``
        selective (optional): ``bool``
    """

    __slots__: List[str] = ["single_use", "selective"]

    ID = 0xf4108aa0
    QUALNAME = "types.ReplyKeyboardForceReply"

    def __init__(self, *, single_use: Union[None, bool] = None, selective: Union[None, bool] = None) -> None:
        self.single_use = single_use  # flags.1?true
        self.selective = selective  # flags.2?true

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "ReplyKeyboardForceReply":
        flags = Int.read(data)

        single_use = True if flags & (1 << 1) else False
        selective = True if flags & (1 << 2) else False
        return ReplyKeyboardForceReply(single_use=single_use, selective=selective)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.single_use is not None else 0
        flags |= (1 << 2) if self.selective is not None else 0
        data.write(Int(flags))

        return data.getvalue()
