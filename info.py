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
𝙃𝙞, 𝙄'𝙢 𝙈𝙚𝙙𝙞𝙖 𝙎𝙚𝙖𝙧𝙘𝙝 𝙗𝙤𝙩

  𝙃𝙚𝙧𝙚 𝙮𝙤𝙪 𝙘𝙖𝙣 𝙨𝙚𝙖𝙧𝙘𝙝 𝙛𝙞𝙡𝙚𝙨 𝙞𝙣 𝙞𝙣𝙡𝙞𝙣𝙚 𝙢𝙤𝙙𝙚. 𝙔𝙤𝙪 𝙘𝙖𝙣 𝙜𝙚𝙩 𝙢𝙤𝙫𝙞𝙚 𝙖𝙣𝙮𝙬𝙝𝙚𝙧𝙚 𝙟𝙪𝙨𝙩 𝙩𝙮𝙥𝙚 𝙗𝙤𝙩 𝙪𝙨𝙚𝙧𝙣𝙖𝙢𝙚 𝙖𝙣𝙙 𝙡𝙚𝙖𝙫𝙚 𝙖 𝙨𝙥𝙖𝙘𝙚 𝙖𝙣𝙙 𝙥𝙪𝙩 𝙢𝙤𝙫𝙞𝙚 𝙣𝙖𝙢𝙚

𝙀𝙜: @InlineFilmBot 𝙈𝙊𝙑𝙄𝙀 𝙉𝘼𝙈𝙀

𝙉𝘽: 𝙏𝙤 𝙪𝙨𝙚 𝙩𝙝𝙞𝙨 𝙗𝙤𝙩 𝙛𝙞𝙧𝙨𝙩 𝙮𝙤𝙪 𝙣𝙚𝙚𝙙 𝙩𝙤 𝙨𝙪𝙗𝙨𝙘𝙧𝙞𝙗𝙚 @InlineFilmUpdate"""

START_MSG = environ.get('START_MSG', default_start_msg)
SHARE_BUTTON_TEXT = 'Checkout {username} for searching files'
INVITE_MSG = environ.get('INVITE_MSG', '• 𝗝𝗼𝗶𝗻 𝗠𝘆 𝗨𝗽𝗱𝗮𝘁𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝗧𝗼 𝗖𝗼𝗻𝘁𝗶𝗻𝘂𝗲...')
