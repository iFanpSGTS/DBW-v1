from dataclasses import dataclass
from urllib.parse import quote

from dateutil.parser import parse

from ..error.ChannelErrors import *
from ..error.MessageErrors import *
from Dict2Query import convert as d2q_converter
from Request import Request
from WrongType import raise_error


@dataclass
class Message:
    # Attrs
    def __init__(self, json, token) -> None:
        self.id = None
        self.channel_id = None

        from .User import User

        self.__token: str = token
        self.request_handler = Request()

        for key in json:
            if key in ("mentions", "author"):
                setattr(
                    self,
                    key,
                    User(
                        json[key], 
                        self.__token) if key == "author" else [
                        User(
                            i,
                            self.__token) for i in json[key]])
            else:
                setattr(self, key, json[key])

    async def reply(self, options=None):
        """Reply to the message with API params."""
        if options is None:
            options = {}
        raise_error(options, "options", dict)

        atom, result = await self.request_handler.send_async_request(f"/channels/{self.channel_id}/messages", "POST", self.__token,
                                                                     {
                                                                         **options,
                                                                         "message_reference": {
                                                                             "message_id": self.id
                                                                         }
                                                                     })

        if atom == 0:
            return Message(result, self.__token)
        else:
            raise SendMessageToChannelFailed(result)

    async def edit(self, options=None):
        """Edit your message with API params."""
        if options is None:
            options = {}
        raise_error(options, "options", dict)

        atom, result = await self.request_handler.send_async_request(f"/channels/{self.channel_id}/messages/{self.id}", "PATCH",
                                                                     self.__token, options)

        if atom == 0:
            return Message(result, self.__token)
        else:
            raise EditMessageFailed(result)

    async def delete(self):
        """Delete the message."""

        atom, result = await self.request_handler.send_async_request(f"/channels/{self.channel_id}/messages/{self.id}", "DELETE",
                                                                     self.__token)

        if atom == 0:
            return self
        else:
            raise DeleteMessageFailed(result)
