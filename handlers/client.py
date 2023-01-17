from aiogram import Bot, types, Dispatcher
from config import dp, bot
from keyboards import create_buttons, kb_lang
from data_base.mysql_db import BotDB
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
import json


with open('C:/Users/butak/OneDrive/Рабочий стол/Anomalia_Crypto_Exchange/languages/messages.json', 'r', encoding='utf-8') as f:
    messages = json.load(f)

with open('C:/Users/butak/OneDrive/Рабочий стол/Anomalia_Crypto_Exchange/languages/buttons.json', 'r', encoding='utf-8') as f:
    buttons = json.load(f)

bot_db = BotDB()

"""Start"""
@dp.message_handler(Command("start"))
async def commands_start(message: types.Message):
    user_id = message.from_user.id 
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    user_url = message.from_user.url
    if not bot_db.user_exists(user_id):
        bot_db.add_info(user_id, first_name, last_name, username, user_url)
    else:
        bot_db.update_info(first_name, last_name, username, user_url, user_id)
    
    kb_menu = create_buttons(user_id)
    await message.answer('💸 <b>Welcome to the Anomalia trading platform!\n📱 Here you can buy or sell cryptocurrency in a couple of clicks '
    'without any need to go through identity verification.</b>', parse_mode='HTML', reply_markup=kb_menu)

    await message.answer("Please select a language 👇", reply_markup=kb_lang)
    

"""Updating user's language"""
class LanguageSelection(StatesGroup):
    waiting_for_language = State()

@dp.callback_query_handler(lambda c: c.data in ['en', 'ru'])
async def process_callback_language(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    selected_language = callback_query.data
    bot_db.update_user_language_db(selected_language, user_id)
    new_kb = create_buttons(user_id)
    await callback_query.message.answer(messages[selected_language]["lang_selected"], reply_markup=new_kb)


"""Profile"""
@dp.message_handler(Text(equals=buttons['en']['profile']), state=LanguageSelection.waiting_for_language)
@dp.message_handler(Text(equals=buttons['ru']['profile']), state=LanguageSelection.waiting_for_language)
async def profile(message: types.Message):
    user_id = message.from_user.id
    user_language = bot_db.get_user_language(user_id)
    await message.answer(messages[user_language]['profile'].format(user_id), parse_mode='HTML')

"""Settings"""
@dp.message_handler(Text(equals=buttons['en']['settings']), state=LanguageSelection.waiting_for_language)
@dp.message_handler(Text(equals=buttons['ru']['settings']), state=LanguageSelection.waiting_for_language)
async def Settings(message: types.Message):
    user_id = message.from_user.id
    user_language = bot_db.get_user_language(user_id)
    await message.answer(messages[user_language]["settings"], parse_mode='HTML')

"""Buy crypto"""
@dp.message_handler(Text(equals=buttons['en']['buy_crypto']), state=LanguageSelection.waiting_for_language)
@dp.message_handler(Text(equals=buttons['ru']['buy_crypto']), state=LanguageSelection.waiting_for_language)
async def Buy_crypto(message: types.Message):
    user_id = message.from_user.id
    user_language = bot_db.get_user_language(user_id)
    await message.answer(messages[user_language]["buy_crypto"], parse_mode='HTML')

"""Sell crypto"""
@dp.message_handler(Text(equals=buttons['en']['sell_crypto']), state=LanguageSelection.waiting_for_language)
@dp.message_handler(Text(equals=buttons['ru']['sell_crypto']), state=LanguageSelection.waiting_for_language)
async def Sell_crypto(message: types.Message):
    user_id = message.from_user.id
    user_language = bot_db.get_user_language(user_id)
    await message.answer(messages[user_language]["sell_crypto"], parse_mode='HTML')

"""About us"""
@dp.message_handler(Text(equals=buttons['en']['about']), state=LanguageSelection.waiting_for_language)
@dp.message_handler(Text(equals=buttons['ru']['about']), state=LanguageSelection.waiting_for_language)
async def About(message: types.Message):
    user_id = message.from_user.id
    user_language = bot_db.get_user_language(user_id)
    await message.answer(messages[user_language]["about"], parse_mode='HTML')

"""Support service"""
@dp.message_handler(Text(equals=buttons['en']['support']), state=LanguageSelection.waiting_for_language)
@dp.message_handler(Text(equals=buttons['ru']['support']), state=LanguageSelection.waiting_for_language)
async def  Support(message: types.Message):
    user_id = message.from_user.id
    user_language = bot_db.get_user_language(user_id)
    await message.answer(messages[user_language]["support"], parse_mode='HTML')

