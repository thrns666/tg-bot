from aiogram import Dispatcher, Bot
from aiogram.filters import Command, CommandStart, Text
from weather_api import Weather
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, BotCommand)
import db
import random
import config_bot
import content_items


#  WARNING!!! this bot without routers.

# Bot init
bot: Bot = config_bot.bot
dp: Dispatcher = Dispatcher()


# my filters
def location_filter(message: Message) -> bool:
    return True if message.location else False


# Menu button
async def menu_button(bot: Bot):
    menu_commands = [
        BotCommand(command='/weather', description='Прогноз погоды'),
        BotCommand(command='/help', description='Помощь'),
        BotCommand(command='/description', description='Описание бота'),
        BotCommand(command='/count', description='Внутренний счетчик'),
    ]
    await bot.set_my_commands(menu_commands)


# Buttons
button_location: KeyboardButton = KeyboardButton(text='Отправить геолокацию', request_location=True)
# Keyboard
keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[button_location]], resize_keyboard=True,
                                                    input_field_placeholder='Нажмите на кнопку ниже')


# Handlers
@dp.message(CommandStart())
async def command_start(message: Message):
    db.db_start(connection, message)
    await message.answer(text=content_items.start_text, parse_mode='HTML')
    await bot.send_sticker(chat_id=message.chat.id, sticker=content_items.sasha)
    await message.delete()


@dp.message(Command(commands=['description']))
async def command_descript(message: Message):
    await message.answer(text=content_items.description, parse_mode='HTML')
    await message.delete()

count: int = 0
@dp.message(Command(commands=['count']))
async def count_func(message: Message):
    global count
    count += 1
    await message.reply(text=str(count))


@dp.message(Command(commands=['help']))
async def command_help(message: Message):
    await message.answer(text=content_items.help_text, parse_mode='HTML')
    await message.delete()


@dp.message(Text('Погода'))
async def location_command(message: Message):
    await message.answer(text='<em>Отправьте вашу геолокацию для прогноза.</em>', reply_markup=keyboard,
                         parse_mode='HTML')


@dp.message(Command(commands=['weather']))
async def weather_command(message: Message):
    await message.answer(text='<em>Отправьте вашу геолокацию для прогноза.</em>',
                         reply_markup=keyboard, parse_mode='HTML')


@dp.message(location_filter)
async def take_location_command(message: Message):
    print(message.json())
    long: float = message.location.longitude
    lat: float = message.location.latitude
    print(message.location)
    db.add_location(connection, message)
    if lat and long:
        await message.answer(text='<em>Местоположение определено, сейчас отправлю прогноз.</em>',
                             reply_markup=ReplyKeyboardRemove(), parse_mode='HTML')
    else:
        await message.answer(text="Ur geo didn't defined, try again :(")

    result: Weather = Weather((lat, long))
    await message.answer(text=f'''<em>Температура за окном:</em> <b>{result.temp_fact}°C</b>
<em>Влажность:</em> <b>{result.humidity}%</b>
<em>Рассвет:</em> <b>{result.sunrise}</b>, <em>закат:</em> <b>{result.sunset}</b>🌗
<em>Порывы ветра:</em> <b>{result.wind_gust_speed} м/c</b>''', parse_mode='HTML')

    # db.add_location(connection, message)


@dp.message(Text('Love'))
async def send_sticker(message: Message):
    await message.answer(text='Смотри какая красота ❤️')
    await bot.send_sticker(chat_id=message.chat.id, sticker=random.choice(content_items.stickers))
    await message.delete()


@dp.message(Text('❤️'))
async def heart_mess(message: Message):
    await message.answer(text='🤍')


if __name__ == '__main__':
    connection = db.conn(password=config_bot.db_password, user=config_bot.db_user)
    dp.startup.register(menu_button)
    dp.run_polling(bot)
