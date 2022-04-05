import asyncio
import logging
import sys
from os import getenv
from typing import Any, Dict

#from aiogram import Bot, types
from aiogram import Bot, Dispatcher, F, Router, html
#from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import state
#from aiogram.utils import executor

from aiogram import Bot, Dispatcher, F, Router, html
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.dispatcher.fsm.state import State, StatesGroup

#from aiogram.contrib.fsm_storage.memory import MemoryStorage
#from aiogram.contrib.middlewares.logging import LoggingMiddleware

from utils import TestStates, Form
from config import TOKEN
from data import  register, know_user, unique_login, set_group

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

Command_info='у меня есть команды: \n /start - приветствие \n /help - помощь \n'

#@dp.message_handler(commands=['start']) ##
@form_router.message(commands=["start"])
async def process_start_command(message: types.Message):
    Uinfo= know_user(message.from_user.id)
    if Uinfo == False:
        s="Привет!\n я - досуговый бот МФТИ!\n я помогу тебе не заскучать и не выгореть! \n"+ Command_info + "для регистрации нажмите /register \n"
        await message.reply(s)
    else:
        s = f"Привет, {Uinfo[0]} из группы {Uinfo[1]}!\n я - досуговый бот МФТИ!\n я помогу тебе не заскучать и не выгореть! \n{Command_info}"

@dp.message_handler(commands=['help']) ##
async  def help_command(message: types.Message):
    await message.reply(Command_info)

@dp.message_handler(commands=['register']) ##
async def registration(message: types.Message):
   # await state.set_state(TestStates.all()[1])
    await state.set_state(Form.name)
    await message.reply('введите логин')

'''@dp.message_handler(state=TestStates.TEST_STATE_1_REGISTER)##
async def first_test_state_case_met(message: types.Message):
    username=message.text.strip()
    if unique_login(username):
        register(message.from_user.id,username)
        await state.set_state(TestStates.all()[3])
        await message.reply('введите номер группы')
    else:
        await message.reply('такой логин уже занят, придумай другой')'''

'''@dp.message_handler(state=TestStates.TEST_STATE_2_register_password) --
async def second_test_state_case_met(message: types.Message):
    phash=hash(message.text.strip())
    await state.set_state(TestStates.all()[3])
    await message.reply('введите номер группы')'''

'''@dp.message_handler(state=TestStates.TEST_STATE_3_REGISTER_GROUP)
async def third_test_state_case_met(message: types.Message):
    group_number=message.text.strip()
    set_group(message.from_user.id, group_number)
    await message.reply('')'''




@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)

async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()

if __name__ == '__main__':
    executor.start_polling(dp)