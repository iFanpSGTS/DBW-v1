class GetChannelError(Exception):
    pass

class SendMessageToChannelFailed(Exception):
    pass

class EditChannelFailed(Exception):
    pass

class DeleteChannelFailed(Exception):
    pass

class FetchChannelHistoryFailed(Exception):
    pass

class FetchChannelMessageFailed(Exception):
    pass

class FetchChannelInvitesFailed(Exception):
    pass

class CreateInviteFailed(Exception):
    pass

class FetchPinnedMessagesFailed(Exception):
    pass

class PinMessageFailed(Exception):
    pass

class UnpinMessageFailed(Exception):
    pass

class EditChannelPermissionsFailed(Exception):
    pass

class DeleteChannelPermissionsFailed(Exception):
    pass

class TriggerTypingFailed(Exception):
    pass

class DeleteChannelMessageFailed(Exception):
    pass

class CreateWebhookFailed(Exception):
    pass

class FetchWebhooksFailed(Exception):
    pass
