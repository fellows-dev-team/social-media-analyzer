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


class GeoPoint(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.GeoPoint`.

    Details:
        - Layer: ``121``
        - ID: ``0xb2a2f663``

    Parameters:
        long: ``float`` ``64-bit``
        lat: ``float`` ``64-bit``
        access_hash: ``int`` ``64-bit``
        accuracy_radius (optional): ``int`` ``32-bit``
    """

    __slots__: List[str] = ["long", "lat", "access_hash", "accuracy_radius"]

    ID = 0xb2a2f663
    QUALNAME = "types.GeoPoint"

    def __init__(self, *, long: float, lat: float, access_hash: int, accuracy_radius: Union[None, int] = None) -> None:
        self.long = long  # double
        self.lat = lat  # double
        self.access_hash = access_hash  # long
        self.accuracy_radius = accuracy_radius  # flags.0?int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "GeoPoint":
        flags = Int.read(data)

        long = Double.read(data)

        lat = Double.read(data)

        access_hash = Long.read(data)

        accuracy_radius = Int.read(data) if flags & (1 << 0) else None

        return GeoPoint(long=long, lat=lat, access_hash=access_hash, accuracy_radius=accuracy_radius)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.accuracy_radius is not None else 0

        data.write(Int(flags))

        data.write(Double(self.long))

        data.write(Double(self.lat))

        data.write(Long(self.access_hash))

        if self.accuracy_radius is not None:
            data.write(Int(self.accuracy_radius))

        return data.getvalue()
