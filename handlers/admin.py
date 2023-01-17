from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from config import dp, bot
from aiogram.dispatcher.filters import Text, IDFilter

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


# @dp.message_handler(commands='Admin', state='*')   
async def admin_panel(message: types.Message):
    user_id = message.from_user.id
    admin_id = '942789239'
    if user_id == admin_id:
        await message.answer('Что нужно, хозяин?)')#, reply_markup=button_case_admin
    else:
        await message.answer('❌ Вы не являетесь администратором бота.') 


# Начало диалога загрузки нового пункта меню
# @dp.message_handler(commands='Загрузить', state=None)
async def cm_start(message : types.Message):
    user_id = message.from_user.id
    admin_id = '942789239'
    if user_id == admin_id:
        await FSMAdmin.photo.set()
        await message.reply('Загрузи фото')
    else: 
        await message.answer('❌ Эта команда доступна только администраторам бота.') 

# Выход из состояний
# @dp.message_handler(state="*", commands='Отмена')
# @dp.message_handler(Text(equals='Отмена', ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('OK')

# Ловим первый ответ и пишем в словарь
# @dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.reply('Теперь введи название')    

# Ловим второй ответ
# @dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.reply('Введи описание')

# Ловим третий ответ
# @dp.message_handler(state=FSMAdmin.description)
async def load_description(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.reply('Теперь укажи цену')   

# Ловим последний ответ и используем полученные данные
# @dp.message_handler(state=FSMAdmin.price)    
async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = float(message.text)

    async with state.proxy() as data:
        await message.reply(str(data))
    
    await state.finish()

# Регистрируем хендлеры
def register_handlers_admin(dp : Dispatcher):
    dp.register_message_handler(admin_panel, commands='Admin', state='*')
    dp.register_message_handler(cm_start, commands=['Загрузить'], state=None)  
    dp.register_message_handler(cancel_handler, state="*", commands='Отмена')
    dp.register_message_handler(cancel_handler, Text(equals='Отмена', ignore_case=True), state="*")  
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)

