import os
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMINS = os.getenv('ADMINS').split(',')
NGROK = os.getenv('NGROK')

# https://bb41-178-172-182-110.ngrok-free.app
# https://bb41-178-172-182-110.ngrok-free.app/bot/6113360297:AAGikeld4Us-q3B75l2SHZNuqDEPdKbsW9U

