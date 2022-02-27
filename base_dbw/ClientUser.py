from dataclasses import dataclass

from ..error.ChannelErrors import *
from ..error.MessageErrors import *
from ..error.SessionErrors import *
from Dict2Query import convert as d2q_converter
from Request import Request
from WrongType import raise_error


@dataclass
class ClientUser:
    # Attrs
    def __init__(self, json: dict, token: str, max_messages: int) -> None:
        self.__token: str = token
        self.max_messages = max_messages
        self.request_handler = Request()

        for key in json:
            setattr(self, key, json[key])

        self.cache: dict = {
            "message": [],
            "guild": []
        }
 
    async def add_message_cache(self, message):
        """Add message to cache"""

        self.cache['message'].append(message)

        if len(self.cache['message']) > self.max_messages:
            del self.cache['message'][0]

    async def remove_message_cache(self, packet):
        """Remove deleted message from cache"""

        for index, cache in enumerate(self.cache['message']):
            if cache.id == packet['id'] and cache.channel_id == packet['channel_id']:
                del self.cache['message'][index]
                break

    async def bulk_delete_message_cache(self, packet):
        """Remove Bulk-deleted message from cache"""

        shift = 0
        for index, cache in enumerate(self.cache['message'][:]):
            if cache.id in packet['ids'] and cache.channel_id == packet['channel_id']:
                del self.cache['message'][index - shift]
                shift += 1

    async def update_message_cache(self, message):
        """Update message from cache"""

        for index, cache in enumerate(self.cache['message']):
            if cache.id == message.id and cache.channel_id == message.channel_id:
                self.cache['message'][index] = message
                break