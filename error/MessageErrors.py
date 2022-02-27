class EditMessageFailed(Exception):
    pass


class DeleteMessageFailed(Exception):
    pass


class BulkDeleteMessageFailed(Exception):
    pass


class AddReactionToMessageFailed(Exception):
    pass


class RemoveReactionToMessageFailed(Exception):
    pass


class FetchReactionsFromMessageFailed(Exception):
    pass


class RemoveReactionsFromMessageFailed(Exception):
    pass


class CrossPostMessageFailed(Exception):
    pass
