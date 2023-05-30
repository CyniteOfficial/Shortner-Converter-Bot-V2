# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "10812811"))
API_HASH = os.environ.get("API_HASH", "dfa8a8101c210c98860d446d9376c4cf")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6275659893:AAFr9iG1tDRX22s1ipsjEqwiZfCnt6tCi3w")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("775251743")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Linkbanao")
DATABASE_URL = os.getenv("DATABASE_URL", "Monfo url") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "775251743")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(775251743)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001895580600")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "mdiskshortner_site") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
