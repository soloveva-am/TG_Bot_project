
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

Command_info='у меня есть команды: \n \start - приветствие \n \help - помощь \n'#\login \n \\register \n '

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\n я - досуговый бот МФТИ!\n я помогу тебе не заскучать и не выгореть! \n", Command_info)

@dp.message_handler(commands=['help'])
async  def help_command(message: types.Message):
    await message.reply(Command_info)

if __name__ == '__main__':
    executor.start_polling(dp)