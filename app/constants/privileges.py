from enum import IntEnum
from enum import unique

@unique
class Privileges(IntEnum):
    BANNED = 1 << 0 # Banned user, can not log in or upload files
    USER = 1 << 1 # Regular user

    # Privileges for moderator
    MODERATOR = 1 << 2 # Can delete other users' uploads
    ADMINISTRATOR = 1 << 3 # Can delete other users' uploads and ban users
    OWNER = 1 << 4 # Can delete other users' uploads, ban users, and promote users to moderator/administrator