from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "180"))

OWNER_ID = int(getenv("OWNER_ID", "5505030156"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/ff8228a476d1fc73ab8fe.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/9584b19633bf5b31faa12.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/RONNY_KI_DUNIYA")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/do_dil_ek_jaan143")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5505030156").split()))


FAILED = "https://telegra.ph/file/9584b19633bf5b31faa12.jpg"
