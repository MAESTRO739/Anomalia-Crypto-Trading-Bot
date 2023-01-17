from aiogram.utils import executor
from config import dp
from aiogram import types, Dispatcher
from handlers import client, admin, other
from data_base import mysql_db

async def on_startup(_):
	mysql_db.start()
	print('The bot is now online.')

admin.register_handlers_admin(dp)


'''Unknown command'''
async def unknown_command(message: types.Message):
    await message.answer('<b>❌ Упс, похоже что это неизвестная команда!\nВоспользуйтесь, пожалуйста, меню. 👇</b>', parse_mode='HTML')

def register_handlers_main(dp: Dispatcher):
	dp.register_message_handler(unknown_command)
	
register_handlers_main(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)