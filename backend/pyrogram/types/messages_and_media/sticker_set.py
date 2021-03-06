from ..object import Object
import pyrogram
from pyrogram import types, raw
from typing import List


class StickerSet(Object):
    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,
            is_archived: bool = None,
            is_official: bool = None,
            is_masks: bool = None,
            is_animated: bool = None,
            installed_date: int = None,
            id: int = None,
            access_hash: int = None,
            title: str = None,
            short_name: str = None,
            thumbs: List["types.Thumbnail"] = None,
            thumb_dc_id: int = None,
            count: int = None,
            hash: int = None,
    ):
        super().__init__(client)

        self.is_archived = is_archived
        self.is_official = is_official
        self.is_masks = is_masks
        self.is_animated = is_animated
        self.installed_date = installed_date
        self.id = id
        self.access_hash = access_hash
        self.title = title
        self.short_name = short_name
        self.thumbs = thumbs
        self.thumb_dc_id = thumb_dc_id
        self.count = count
        self.hash = hash

    @staticmethod
    def _parse(client, sticker_set: raw.base.StickerSet):
        if sticker_set is None:
            return None

        return StickerSet(
            client=client,

            is_archived=getattr(sticker_set, 'archived', None),
            is_official=getattr(sticker_set, 'official', None),
            is_masks=getattr(sticker_set, 'masks', None),
            is_animated=getattr(sticker_set, 'animated', None),
            installed_date=getattr(sticker_set, 'installed_date', None),
            id=getattr(sticker_set, 'id', None),
            access_hash=getattr(sticker_set, 'access_hash', None),
            title=getattr(sticker_set, 'title', None),
            short_name=getattr(sticker_set, 'short_name', None),
            thumbs=types.Thumbnail._parse(client, getattr(sticker_set, 'thumbs', None)),
            thumb_dc_id=getattr(sticker_set, 'thumb_dc_id', None),
            count=getattr(sticker_set, 'count', None),
            hash=getattr(sticker_set, 'hash', None),
        )

    @staticmethod
    async def _parse_from_input_stickerset(client, input_stickerset: raw.base.StickerSet):
        if input_stickerset is None:
            return None

        sticker_set = await client.get_stickerset(input_stickerset)

        return sticker_set
