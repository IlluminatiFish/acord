from typing import TypeVar

Snowflake = TypeVar("Snowflake", bound=int)

# Simple snowflake object

from .user import User
from .emoji import Emoji
from .sticker import Sticker
from .roles import Role, RoleTags

from .message import Message, MessageReference
from .channels import Channel, TextChannel, Stage
from .guild import Guild
from .guild_template import GuildTemplate

Message.update_forward_refs()
