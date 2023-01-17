from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
import json
from data_base.mysql_db import BotDB

bot_db = BotDB()

def create_buttons(user_id):
    with open('C:/Users/butak/OneDrive/Рабочий стол/Anomalia_Crypto_Exchange/languages/buttons.json', 'r', encoding='utf-8') as f:
        buttons = json.load(f)
    user_language = bot_db.get_user_language(user_id)

    b1 = KeyboardButton(buttons[user_language]['profile'])
    b2 = KeyboardButton(buttons[user_language]['settings'])
    b3 = KeyboardButton(buttons[user_language]['buy_crypto'])
    b4 = KeyboardButton(buttons[user_language]['sell_crypto'])
    b5 = KeyboardButton(buttons[user_language]['about'])
    b6 = KeyboardButton(buttons[user_language]['support'])

    kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
    
    kb_client.row(b1, b2).row(b3, b4).row(b5, b6)
    return kb_client
