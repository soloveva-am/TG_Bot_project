import asyncio
import logging
import sys
import datetime
from emoji import emojize
from config import TOKEN
from utils import form
from data import  register, know_user, unique_login, set_group
from linked_files import ADVICES, SKATING
from days import days

from aiogram import Bot, Dispatcher, F, Router, html
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.dispatcher.fsm.state import State, StatesGroup
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup, ReplyKeyboardRemove

form_router = Router()
Command_info='у меня есть команды: \n /start - приветствие \n /help - помощь \n'
Daynames = ['сегодня', 'завтра', 'послезавтра']
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
@form_router.message(commands = ["advice_today"])
async def advice_1(message: Message, state: FSMContext) -> None:
    user_info=know_user(message.from_user.id)
    if user_info==False:
        await message.reply('Извините, мы незнакомы. Для регистрации нажмите /register')
    else:
        username = user_info[0]
        groupnumber=user_info[1]
        today, now = str(datetime.datetime.today()).split()
        Advice = ADVICES(today, groupnumber)
        answer=f'{username}, вот, что я могу тебе сегодня посоветовать: \n'
        for pair in Advice.keys():
            if Advice[pair] =='Возьми зонт!':
                if pair == 'Advice':
                    answer=answer+emojize(f":umbrella: уходя на пары, {Advice[pair]} :umbrella: \n")
                else:
                    answer=answer+ emojize(f':umbrella: если будешь выглядывать из дома в {pair},Возьми зонт! :umbrella: \n')
            else:
                answer=answer+f'в {pair} {Advice[pair]}\n'
            if pair == '09:00 – 10:25':
                answer=answer+ emojize("ну или можешь поспать :zzz:\n")
        await message.reply(answer)

@form_router.message(commands = ["advice_three"])
async def advice_1(message: Message, state: FSMContext) -> None:
    user_info=know_user(message.from_user.id)
    if user_info==False:
        await message.reply('Извините, мы незнакомы. Для регистрации нажмите /register')
    else:
        username = user_info[0]
        groupnumber=user_info[1]
        Dates=days()
        named_dates = zip(Dates, Daynames)
        answer="советы на три дня: \n"
        for day, dayname in named_dates:
            Advice = ADVICES(day, groupnumber)
            answer=answer+ f'{username}, вот, что я могу тебе посоветовать на {dayname}: \n'
            for pair in Advice.keys():
                if Advice[pair] =='Возьми зонт!':
                    if pair == 'Advice':
                        answer=answer+ emojize(f":umbrella: уходя на пары, {Advice[pair]} :umbrella: \n")
                    else:
                        answer=answer+ emojize(f':umbrella: если будешь выглядывать из дома в {pair},Возьми зонт! :umbrella:  \n')
                else:
                    answer=answer+f'в {pair} {Advice[pair]}\n'
                if pair == '09:00 – 10:25':
                    answer=answer+ emojize("ну или можешь поспать :zzz: \n")
            answer = answer +'\n'
        await message.reply(answer)

@form_router.message(commands = ["katok"])
async def advice_1(message: Message, state: FSMContext) -> None:
    user_info=know_user(message.from_user.id)
    if user_info==False:
        await message.reply('Извините, мы незнакомы. Для регистрации нажмите /register')
    else:
        username = user_info[0]
        groupnumber=user_info[1]
        skating_advice = SKATING(groupnumber)
        if skating_advice:
            ans = f"{username}, на этой неделе ты можешь покататься на катке Салют \n"
            for day in skating_advice.keys():
                ans= ans+ emojize(f'в {day} {skating_advice[day]} :ice_skate: \n')
        else: ans=f'к сожалению, на этой неделе нет катаний'
    await(message.reply(ans))




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
    if Uinfo==False: raise Exception
    else: await message.reply(f'теперь мы знакомы, {Uinfo[0]} из группы {Uinfo[1]}! \n')

async def main():
    bot = Bot(token=TOKEN, parse_mode="HTML")
    dp = Dispatcher()
    dp.include_router(form_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())