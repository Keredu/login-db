from enum import Enum

class TokenType(int, Enum):
    ACCESS = 0
    REFRESH = 1 # TODO: implement refresh tokens
    RESET_PASSWORD = 2


class TokenStatus(int, Enum):
    ACTIVE = 0
    EXPIRED = 1
    USED = 2
    # Log out is a special case
    LOGGED_OUT = 3

class UserStatus(str, Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    DELETED = 'deleted'
    BANNED = 'banned'
    PENDING = 'pending'