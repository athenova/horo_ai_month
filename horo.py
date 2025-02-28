import os
import telebot
import schedule
import time
import locale
from openai import OpenAI
from datetime import datetime
from datetime import timedelta

AI_TEXT_MODEL = 'deepseek-chat'
CHAT_TOKEN_NAME = "DEEPSEEK_API_KEY"
BOT_TOKEN_NAME = "ATHE_BOT_TOKEN"
BOT_TOKEN = os.environ.get(BOT_TOKEN_NAME)
#CHAT_ID = -1002374309134
CHAT_ID = '@ai_tarot'

def job(sign, CHAT_ID=CHAT_ID):
    locale.setlocale(locale.LC_ALL, ('ru_RU', 'UTF-8'))
    date = datetime.now() + timedelta(days=10)
    month = date.strftime('%B')
    year = date.year
    client = OpenAI(api_key=os.environ.get(CHAT_TOKEN_NAME), base_url="https://api.deepseek.com")
    text = client.chat.completions.create(
        model=AI_TEXT_MODEL,
        messages=[
            { "role": "system", "content": f"Ты - профессиональный астролог" },
            { "role": "user", "content": f"Составь гороскоп на {month} {year} год для знака '{sign}', используй смайлики, используй не более 300 слов" },
        ]
    ).choices[0].message.content
    bot = telebot.TeleBot(BOT_TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=text, parse_mode="Markdown")

if __name__ == '__main__':
    schedule.every().day.at("19:00",'Europe/Moscow').do(job, sign="Рыбы", CHAT_ID='@pisces_the')
    schedule.every().day.at("19:01",'Europe/Moscow').do(job, sign="Овен", CHAT_ID='@aries_the')
    schedule.every().day.at("19:02",'Europe/Moscow').do(job, sign="Телец")
    schedule.every().day.at("19:03",'Europe/Moscow').do(job, sign="Близнецы", CHAT_ID='@gemini_the')
    schedule.every().day.at("19:04",'Europe/Moscow').do(job, sign="Рак")
    schedule.every().day.at("19:05",'Europe/Moscow').do(job, sign="Лев")
    schedule.every().day.at("19:06",'Europe/Moscow').do(job, sign="Дева")
    schedule.every().day.at("19:07",'Europe/Moscow').do(job, sign="Весы")
    schedule.every().day.at("19:08",'Europe/Moscow').do(job, sign="Скорпион")
    schedule.every().day.at("19:09",'Europe/Moscow').do(job, sign="Стрелец")
    schedule.every().day.at("19:10",'Europe/Moscow').do(job, sign="Козерог", CHAT_ID='@capricorn_the')
    schedule.every().day.at("19:11",'Europe/Moscow').do(job, sign="Водолей", CHAT_ID='@aquarius_the')

    fifteen_minutes = 15 * 60

    for i in range(fifteen_minutes):
        schedule.run_pending()
        time.sleep(1)
