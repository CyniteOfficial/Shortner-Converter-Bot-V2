# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "29081699"))
API_HASH = os.environ.get("API_HASH", "4c4beb5bf57a6d52a4cda249a98f0980")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6095380962:AAEEzGU4r7sxEtCYXQvA-mYSeplxzc5ao8E")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("576151570")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "short")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://short:sh9824786@cluster0.szric3m.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "576151570")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(Id Owned Id)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001914707973")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "Shortnerfly") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
