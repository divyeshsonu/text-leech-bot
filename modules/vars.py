import os

API_ID    = os.environ.get("API_ID", "27886943")
API_HASH  = os.environ.get("API_HASH", "b28d0dae5a57f767716f1d8865560fee")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7567486951:AAHXSrT1Vr6h-nUW06w61uEDWjrCcbfn010") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
