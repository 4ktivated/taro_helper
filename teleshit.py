from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN
from base_info import taro

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nТут ты можешь быстро узнать описание карт старшего аркана.")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Здесь вы можете запросить формулировку карт высшего аркана.")

@dp.message_handler()
async def value_card(msg:types.Message):
    if msg.text not in taro:
        await bot.send_message( msg.from_user.id, 'Название карты нужно указать маленькими буквами, если у вас не получилось возможно в наших списках карта имеет другое название')
    else:
        await bot.send_message( msg.from_user.id, taro.get(msg.text))

if __name__ == '__main__':
    executor.start_polling(dp)