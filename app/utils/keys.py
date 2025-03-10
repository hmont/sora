import secrets

from . import VALID_CHARS

def generate_key(length: int = 16) -> str:
    return "".join(secrets.choice(VALID_CHARS) for _ in range(length))