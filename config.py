# ©️ DKBOTZ or https://t.me/DKBOTZ
# Coded By https://t.me/DKBOTZHELP 
# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "12124605"))
API_HASH = os.environ.get("API_HASH", "5cf3577d85fd02286535ec2296934287")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5859450514:AAE83JvDqDlqRNXX4HLrN-JJHKLIuxDv3ZY")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("1883570185")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "conve")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://strange89:strange1234@cluster0.68luwly.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "1883570185")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(1883570185)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001791144635")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "shortnerfly") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
