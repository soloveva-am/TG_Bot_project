from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from weath import *


# PROXY_URL = 'socks5://xxx.xxx.xxx.xxx' # вставить здесь подходящий ip

secret_token = '5125992663:AAHf1oqhmxYnl6cY6za4dwVCLLzGPEYXm0k'  # строка вида: 123456789:ABCDEFGHJABCDEFGHJABCDEFGHJABCDEFGHJ

bot = Bot(token=secret_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler(commands=['weather'])
async def echo(message: types.Message):
    await message.reply("Какое время ты хочешь смотреть?")
    @dp.message_handler(commands=["now"])
    async def weat(message: types.Message):
        # if message == "today":
        await message.reply(content_presently)






if __name__ == '__main__':
    executor.start_polling(dp)
