
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import state
from aiogram.utils import executor

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from utils import TestStates
from config import TOKEN
from data import in_data, register, password_check

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

Command_info='у меня есть команды: \n /start - приветствие \n /help - помощь \n'#/login \n /register \n '

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    s="Привет!\n я - досуговый бот МФТИ!\n я помогу тебе не заскучать и не выгореть! \n"+ Command_info
    await message.reply(s)

@dp.message_handler(commands=['help'])
async  def help_command(message: types.Message):
    await message.reply(Command_info)

@dp.message_handler(commands=['register'])
async def registration(message: types.Message):
    await state.set_state(TestStates.all()[1])
    await message.reply('введите логин')

@dp.message_handler(state=TestStates.TEST_STATE_1_register)
async def first_test_state_case_met(message: types.Message):
    username=message.text.strip()
    if not in_data(username):
        await state.set_state(TestStates.all()[2])
        await message.reply('введите пароль')
    else:
        await message.reply('такой логин уже занят, придумай другой')

@dp.message_handler(state=TestStates.TEST_STATE_2_register_password)
async def second_test_state_case_met(message: types.Message):
    phash=hash(message.text.strip())
    await state.set_state(TestStates.all()[3])
    await message.reply('введите номер группы')

@dp.message_handler(state=TestStates.TEST_STATE_3_register_group)
async def third_test_state_case_met(message: types.Message):
    group_number=message.text.strip()
    register(username, phash, group_number)
    await message.reply('')




@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)

async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()

if __name__ == '__main__':
    executor.start_polling(dp)