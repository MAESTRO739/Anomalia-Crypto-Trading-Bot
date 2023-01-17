from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from data_base.mysql_db import BotDB


inline_kb_en = InlineKeyboardButton(text='🇺🇸 English', callback_data='en')
inline_kb_ru = InlineKeyboardButton(text='🇷🇺 Russian', callback_data='ru')

kb_lang = InlineKeyboardMarkup()

kb_lang.add(inline_kb_en, inline_kb_ru)