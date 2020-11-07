from django.contrib import admin

from . import models


# Register your models here.
class TelegramChannelInline(admin.TabularInline):
    model = models.TelegramChannel


class AdminLogInline(admin.TabularInline):
    model = models.AdminLog


class MessageViewInline(admin.TabularInline):
    model = models.MessageView


class MemberCountHistoryInline(admin.TabularInline):
    model = models.ChatMemberCount


class SharedMediaHistoryInline(admin.TabularInline):
    model = models.ChatSharedMedia


class TelegramAccountAdmin(admin.ModelAdmin):
    inlines = [
        TelegramChannelInline,
        MemberCountHistoryInline,
        SharedMediaHistoryInline,
        MessageViewInline,
        AdminLogInline,
    ]
    list_display = ['first_name', 'username', 'created_at', 'modified_at']


#################################################################################

class TelegramAccountInline(admin.TabularInline):
    model = models.TelegramAccount


class ForwardedMessageInline(admin.TabularInline):
    model = models.Message
    fk_name = 'forward_from'
    verbose_name_plural = 'Forwarded Messages'


class SentMessageInline(admin.TabularInline):
    model = models.Message
    fk_name = 'from_user'
    verbose_name_plural = 'Sent Messages'


class ViaBotMessageInline(admin.TabularInline):
    model = models.Message
    fk_name = 'via_bot'
    verbose_name_plural = 'Inline Messages'


class InvitedUserInline(admin.TabularInline):
    model = models.Membership
    fk_name = 'invited_by'
    verbose_name_plural = 'Invited Users'


class UserRoleInline(admin.TabularInline):
    model = models.Membership
    fk_name = 'role_changed_by'
    verbose_name_plural = 'Modified User Roles'


class MentionedInline(admin.TabularInline):
    model = models.Entity
    fk_name = 'user'
    verbose_name_plural = 'Mentions'


class UserAdmin(admin.ModelAdmin):
    inlines = [
        TelegramAccountInline,
        ForwardedMessageInline,
        SentMessageInline,
        ViaBotMessageInline,
        InvitedUserInline,
        UserRoleInline,
        MentionedInline,
    ]
    # list_display = ()


#################################################################################

class ChatMemberInline(admin.TabularInline):
    model = models.User.chats.through
    verbose_name_plural = 'Members'


class LinkedChatInline(admin.TabularInline):
    model = models.Chat
    verbose_name_plural = 'Linked Chats'


class MessageInline(admin.TabularInline):
    model = models.Message
    fk_name = 'chat'
    verbose_name_plural = 'Messages'


class ForwardedMessageChannelInline(admin.TabularInline):
    model = models.Message
    fk_name = 'forward_from_chat'
    verbose_name_plural = 'Forwarded Messages'


class ChatAdmin(admin.ModelAdmin):
    inlines = [
        TelegramChannelInline,
        MessageInline,
        ForwardedMessageChannelInline,
        ChatMemberInline,
        LinkedChatInline,
        AdminLogInline,
        MemberCountHistoryInline,
        SharedMediaHistoryInline,
        MessageViewInline,
    ]


#################################################################################

class ChatsInline(admin.TabularInline):
    model = models.Chat.admin_log_mentions.through
    verbose_name_plural = 'Mentioned Chats'


class UsersInline(admin.TabularInline):
    model = models.User.admin_log_mentions.through
    verbose_name_plural = 'Mentioned Users'


class AdminLogEventInline(admin.TabularInline):
    model = models.AdminLogEvent


class AdminLogAdmin(admin.ModelAdmin):
    inlines = [
        UsersInline,
        ChatsInline,
        AdminLogEventInline,
    ]


#################################################################################

class EntityInline(admin.TabularInline):
    model = models.Entity


class EntityTypeInline(admin.TabularInline):
    model = models.EntityType


class MessageReplyInline(admin.TabularInline):
    model = models.Message
    verbose_name_plural = 'Replies'


class ActionMessagePinnedInline(admin.TabularInline):
    model = models.AdminLogEventActionUpdatePinned
    verbose_name_plural = 'Pinned Actions'


class ActionMessageEditedPrevInline(admin.TabularInline):
    model = models.AdminLogEventActionEditMessage
    verbose_name_plural = 'Action Edit Prevs'
    fk_name = 'prev_message'


class ActionMessageEditedNewInline(admin.TabularInline):
    model = models.AdminLogEventActionEditMessage
    verbose_name_plural = 'Action Edit News'
    fk_name = 'new_message'


class ActionMessageStopPollInline(admin.TabularInline):
    model = models.AdminLogEventActionStopPoll
    verbose_name_plural = 'Action Stop Polls'


class MessageAdmin(admin.ModelAdmin):
    inlines = [
        MessageReplyInline,
        EntityInline,
        EntityTypeInline,
        MessageViewInline,
        ActionMessagePinnedInline,
        ActionMessageEditedPrevInline,
        ActionMessageEditedNewInline,
        ActionMessageStopPollInline,
    ]


#################################################################################

admin.site.register(models.TelegramAccount, TelegramAccountAdmin)
admin.site.register(models.TelegramChannel)
admin.site.register(models.AddChannelRequest)

admin.site.register(models.User, UserAdmin)
admin.site.register(models.Chat, ChatAdmin)
admin.site.register(models.Membership)
admin.site.register(models.Message, MessageAdmin)
admin.site.register(models.MessageView)
admin.site.register(models.Entity)
admin.site.register(models.EntityType)
admin.site.register(models.ChatMemberCount)
admin.site.register(models.ChatSharedMedia)
admin.site.register(models.Restriction)
admin.site.register(models.AdminLog, AdminLogAdmin)
admin.site.register(models.AdminLogEvent)
admin.site.register(models.AdminLogEventActionChangeTitle)
admin.site.register(models.AdminLogEventActionChangeAbout)
admin.site.register(models.AdminLogEventActionChangeUsername)
admin.site.register(models.AdminLogEventActionChangePhoto)
admin.site.register(models.AdminLogEventActionToggleInvites)
admin.site.register(models.AdminLogEventActionToggleSignatures)
admin.site.register(models.AdminLogEventActionUpdatePinned)
admin.site.register(models.AdminLogEventActionEditMessage)
admin.site.register(models.AdminLogEventActionDeleteMessage)
admin.site.register(models.AdminLogEventActionParticipantJoin)
admin.site.register(models.AdminLogEventActionParticipantLeave)
admin.site.register(models.AdminLogEventActionParticipantInvite)
admin.site.register(models.AdminLogEventActionToggleBan)
admin.site.register(models.AdminLogEventActionToggleAdmin)
admin.site.register(models.AdminLogEventActionChangeStickerSet)
admin.site.register(models.AdminLogEventActionTogglePreHistoryHidden)
admin.site.register(models.AdminLogEventActionDefaultBannedRights)
admin.site.register(models.AdminLogEventActionStopPoll)
admin.site.register(models.AdminLogEventActionChangeLinkedChat)
admin.site.register(models.AdminLogEventActionChangeLocation)
admin.site.register(models.AdminLogEventActionToggleSlowMode)
admin.site.register(models.ChannelParticipant)
admin.site.register(models.ChannelParticipantSelf)
admin.site.register(models.ChannelParticipantCreator)
admin.site.register(models.ChannelParticipantAdmin)
admin.site.register(models.ChannelParticipantBanned)
admin.site.register(models.ChatBannedRight)
admin.site.register(models.ChatPermissions)
admin.site.register(models.AdminRights)
admin.site.register(models.SharedMediaAnalyzerMetaData)
admin.site.register(models.ChatMessageViewsAnalyzerMetaData)
admin.site.register(models.ChatMemberCountAnalyzerMetaData)
admin.site.register(models.ChatMembersAnalyzerMetaData)
admin.site.register(models.AdminLogAnalyzerMetaData)