import requests
import datetime
import logging
from config import tg_bot_token, weather_token
from aiogram import Bot, types
from aiogram import Dispatcher, executor

logging.basicConfig(filename='weather_bot.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет! Напиши мне название города и я пришлю сводку погоды!")


@dp.message_handler()
async def get_weather(message: types.Message):
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={weather_token}&units=metric"
        )
        r.raise_for_status()

        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Не знаю какая погода!"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])

        await message.reply(f"**{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}**\n"
              f"Погода в городе: {city}\nТемпература: {cur_weather}C° {wd}\n"
              f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
              f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
              f"**Хорошего дня!**"
              )
        logging.info(f"Successfully retrieved weather data for {city}")

    except requests.exceptions.RequestException as e:
        logging.error(f"Error retrieving weather data: {e}")
        await message.reply("\U00002620 Проверьте название города \U00002620")

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        await message.reply("\U00002620 Что-то пошло не так. Пожалуйста, попробуйте позже. \U00002620")


if __name__ == '__main__':
    executor.start_polling(dp)