import asyncio
import logging
import sys
from os import getenv
from typing import Any, Dict

from config import TOKEN
from utils import form
from data import  register, know_user, unique_login, set_group

from aiogram import Bot, Dispatcher, F, Router, html
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.dispatcher.fsm.state import State, StatesGroup
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup, ReplyKeyboardRemove

form_router = Router()
Command_info='у меня есть команды: \n /start - приветствие \n /help - помощь \n'

@form_router.message(commands=["start"])
async def command_start(message: Message, state: FSMContext) -> None:
    Uinfo = know_user(message.from_user.id)
    if Uinfo == False:
        s = "Привет!\n я - досуговый бот МФТИ!\n я помогу тебе не заскучать и не выгореть! \n" + Command_info + "Мы незнакомы. Представься, пожалуйста! \n"
        await state.set_state(form.register)

    else:
        s = f"Привет, {Uinfo[0]} из группы {Uinfo[1]}!\n я - досуговый бот МФТИ!\n я помогу тебе не заскучать и не выгореть! \n{Command_info}"
    await message.reply(s,
        reply_markup=ReplyKeyboardRemove())

@form_router.message(commands=["help"])
async def command_start(message: Message, state: FSMContext) -> None:
    await message.answer(
        Command_info,
    )

@form_router.message(form.register)
async def register_login(message: Message, state: FSMContext) -> None:
    username = message.text.strip()
    if unique_login(username):
        register(message.from_user.id, username)
        await state.set_state(form.group)
        await message.reply('введите номер группы')
    else:
        await message.reply('такой логин уже занят, придумай другой')


@form_router.message(form.group)
async def register_group(message: Message, state: FSMContext) -> None:
    group_number = message.text.strip()
    set_group(message.from_user.id, group_number)
    Uinfo = know_user(message.from_user.id)
    await message.reply(f'теперь мы знакомы, {Uinfo[0]} из группы {Uinfo[1]}! \n')

async def main():
    bot = Bot(token=TOKEN, parse_mode="HTML")
    dp = Dispatcher()
    dp.include_router(form_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())