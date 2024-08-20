from dotenv import load_dotenv
from os import getenv

load_dotenv()

TOKEN = getenv('TOKEN')
ADMIN = int(getenv('ADMIN_ID'))
WEB_SERVER_HOST = getenv('WEB_SERVER_HOST')
WEB_SERVER_PORT = int(getenv('WEB_SERVER_PORT'))
WEBHOOK_PATH = getenv('WEBHOOK_PATH')
WEBHOOK_SECRET = getenv('WEBHOOK_SECRET')
BASE_WEBHOOK_URL = getenv('BASE_WEBHOOK_URL')
DB_NAME = getenv('DB_NAME')
DB_USER = getenv('DB_USER')
DB_PASS = getenv('DB_PASS')
DB_HOST = getenv('DB_HOST')
DB_PORT = getenv('DB_PORT')
INSTAGRAM_URL = getenv('INSTAGRAM_URL')
CARD_NUMBER = getenv('CARD_NUMBER')
DEFAULT_LANGUAGE = getenv('DEFAULT_LANGUAGE')
GROUP_PHOTO = getenv('GROUP_PHOTO')
SINGLE_PHOTO = getenv('SINGLE_PHOTO')

