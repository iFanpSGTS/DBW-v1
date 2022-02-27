class TokenNotFoundError(Exception):
    pass


class IntentNotFoundError(Exception):
    pass


class InvalidTokenError(Exception):
    pass


class FetchInviteFailedError(Exception):
    pass


class RemoveInviteFailedError(Exception):
    pass


class FetchUserFailedError(Exception):
    pass


class FetchGuildFailedError(Exception):
    pass


class EditClientUserFailed(Exception):
    pass


class LeaveGuildFailed(Exception):
    pass


class FetchGuildPreviewFailed(Exception):
    pass


class CreateGuildFailed(Exception):
    pass


class CreateDMFailed(Exception):
    pass