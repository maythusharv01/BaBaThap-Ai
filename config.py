from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "24491372"
# -------------------------------------------------------------
API_HASH = "4422edbefdceabba5c5575884c5db93a"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", None)
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = int(getenv("OWNER_ID", "1318826936"))
SUPPORT_GRP = "ZuriOfficialUpgrade"
UPDATE_CHNL = "ZuriOfficialUpdate"
OWNER_USERNAME = "ZuriOfficialBoy"
