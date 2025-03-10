from __future__ import annotations

import os

from dotenv import load_dotenv

load_dotenv(override=True)

SORA_HOST = os.environ["SORA_HOST"]
SORA_PORT = int(os.environ["SORA_PORT"])

WORKERS = int(os.environ["WORKERS"])

MYSQL_USER = os.environ["MYSQL_USER"]
MYSQL_PASS = os.environ["MYSQL_PASS"]
MYSQL_HOST = os.environ["MYSQL_HOST"]
MYSQL_PORT = int(os.environ["MYSQL_PORT"])
MYSQL_DB = os.environ["MYSQL_DB"]

MYSQL_DSN = f"mysql://{MYSQL_USER}:{MYSQL_PASS}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"

REDIS_USER = os.environ["REDIS_USER"]
REDIS_PASS = os.environ["REDIS_PASS"]
REDIS_HOST = os.environ["REDIS_HOST"]
REDIS_PORT = int(os.environ["REDIS_PORT"])
REDIS_DB = int(os.environ["REDIS_DB"])

UPLOAD_ID_LENGTH = int(os.environ["UPLOAD_ID_LENGTH"])

UPLOAD_LIMIT = str(os.environ["UPLOAD_LIMIT"])

REDIS_URI = f"redis://{REDIS_USER}:{REDIS_PASS}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"

FILES_DIRECTORY = os.environ["FILES_DIRECTORY"]