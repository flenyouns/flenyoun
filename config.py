## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgBiOQPJCx4ff00iPMPjxFPMFfra55VLJObYXwRSdNDUnI5WqENfGUa8gyZuahvMG9fswi0plyagcyl7v_uqx-3wTex5ZRXpU7gX4tFGvK8QxFgxZn-bt3w5LoUFy1tsnZvaWrYTfb0cEsI2_uSUcP24AymRVklNTkIabZd0SNGhjb8FFs8j9dal0CP9eGRV1U_c3gz5eoUXmnX6GOAwUnqtr0SsmMUsLqw1cFvbOu0AiI4H5YKQ4Q84KV3FE2IivG318CwTRdx7l-ZqQRCzfYadK2O5cl7m44U5RejQ7sA_RCn6LSEszh9Mo8rcS4yViSIqNSB-M5JRncSlDiDfO72Ee898vgA")
BOT_TOKEN = getenv("BOT_TOKEN", "5550693559:AAEuTYzCKcbEgQgABj6JUO_IMtoHKQkFQOU")
BOT_NAME = getenv("BOT_NAME", "مَــيَـۅٛࢪ࣪كَ ذِنِــۅٛنِ")
API_ID = int(getenv("API_ID", "9605118"))
API_HASH = getenv("API_HASH", "ad3ed4daeea61e86d04bde056cb5406e")
OWNER_NAME = getenv("OWNER_NAME", "ذنــون .")
OWNER_USERNAME = getenv("OWNER_USERNAME", "o_h_2")
ALIVE_NAME = getenv("ALIVE_NAME", "ذنــون .")
BOT_USERNAME = getenv("BOT_USERNAME", "o_h_2bot")
OWNER_ID = getenv("OWNER_ID", "635443181")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "x_ecd")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "T0I7I")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "SF380")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5284259786").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/e22e5d1f0ccd57fa5f677.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
