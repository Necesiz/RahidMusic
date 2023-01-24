import os

class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5875169901:AAGCA2P9awld_86WY5VecA-1gKk-xdYgEmc")
    API_ID = int(os.environ.get("API_ID", "19485442"))
    API_HASH = os.environ.get("API_HASH", "a03fcb372b3ec4e406b5d52f84b02e53")
    BOT_OWNER = os.environ.get("BOT_OWNER", "nesirovqadirofficiall")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "ayparasongbot")
    PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "qrupplaylist")
    PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1001719261837"))
