import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
USER_SESSION = environ.get('USER_SESSION', 'User_Bot')
API_ID = int(environ.get('API_ID', '28376650'))
API_HASH = environ.get('API_HASH', '6200fc0feb5ff2678bf904194c8696fb')
BOT_TOKEN = environ.get('BOT_TOKEN', '6104978506:AAGkw-5XOgSOJOZ1pHCyOPy1iw2bauq02MA')
USERBOT_STRING_SESSION = environ.get('USERBOT_STRING_SESSION')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['CHANNELS'].split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', 'mongodb+srv://pkr923366:pkr923366@cluster0.nc5ygqe.mongodb.net/?retryWrites=true&w=majority')
DATABASE_NAME = environ.get('DATABASE_NAME', 'Cluster0')
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages
default_start_msg = """
Hi, I'm Media Search bot

Here you can search files in inline mode. Just press following buttons SEARCH HERE and start searching or Just type @InlineFilmBot in any chat and type the name of the movie with a space

Eg: @InlineFilmBot MOVIE NAME

NB: To use this bot first you need to subscribe @InlineFilmUpdate"""

START_MSG = environ.get('START_MSG', default_start_msg)
SHARE_BUTTON_TEXT = 'Checkout {username} for searching files'
INVITE_MSG = environ.get('INVITE_MSG', 'Please join @.... to use this bot')
