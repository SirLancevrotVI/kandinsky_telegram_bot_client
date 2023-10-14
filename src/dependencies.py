import os
from os.path import join, dirname

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

REPLICATE_API = os.environ.get("REPLICATE_API_TOKEN")
TELEGRAM_BOT_API = os.environ.get("TELEGRAM_BOT_API_TOKEN")
