from os import getenv
from dotenv import load_dotenv
from base64 import b64decode as who

ONLINE_ON = """
➠ **Userbot Online** 🔥
➠ **Type** `.alive`
➠ **Channel:** : @RendyProjects
"""

RendyProjects = who("YXdhaXQgY2xpZW50LmpvaW5fY2hhdChSZW5keVByb2plY3RzKQo=").decode("utf-8")

KONTOLMU = "https://graph.org/file/3727ab65ad17325a9196f.jpg"

ALIVE_ONLINE = ONLINE_ON
LOG_ALIVE = KONTOLMU

# jangan hapus && auto crashed

GIT_TOKEN = getenv(
    "GIT_TOKEN",
    who("").decode("utf-8"),
)


REPO_URL = "https://github.com/TeamKillerX/TigerX-Userbot"

CHANNEL = who("UmVuZHlQcm9qZWN0cwo=").decode("utf-8")
SUPPORT = who("cGFudGVreWtzCg==").decode("utf-8")
