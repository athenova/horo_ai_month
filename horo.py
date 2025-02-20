import os
import telebot
import schedule
import time
import locale
from datetime import datetime
from datetime import timedelta
from openai import OpenAI

AI_TEXT_MODEL = 'gpt-4o-mini'
BOT_TOKEN_NAME = "ATHE_BOT_TOKEN"
BOT_TOKEN = os.environ.get(BOT_TOKEN_NAME)
#CHAT_ID = -1002374309134
CHAT_ID = '@horo_ai'

def job(sign, symbol, month):
    client = OpenAI()
    text = client.chat.completions.create(
        model=AI_TEXT_MODEL,
        messages=[
            { "role": "system", "content": f"Ты - профессиональный астролог" },
            { "role": "user", "content": f"Составь гороскоп на {month} для знака '{sign}', используй смайлики, не пиши дату" },
        ]
    ).choices[0].message.content
    bot = telebot.TeleBot(BOT_TOKEN)
    text = f"""{symbol} **{sign}** {symbol}

{text}    
"""
    bot.send_message(chat_id=CHAT_ID, text=text, parse_mode="Markdown")

locale.setlocale(locale.LC_ALL, ('ru_RU', 'UTF-8'))
date = datetime.now() + timedelta(days=10)
month = date.strftime('%B')

schedule.every().day.at("16:00",'Europe/Moscow').do(job, sign="Рыбы", symbol='♓', month=month)
schedule.every().day.at("16:01",'Europe/Moscow').do(job, sign="Овен", symbol='♈', month=month)
schedule.every().day.at("16:02",'Europe/Moscow').do(job, sign="Телец", symbol='♉', month=month)
schedule.every().day.at("16:03",'Europe/Moscow').do(job, sign="Близнецы", symbol='♊', month=month)
schedule.every().day.at("16:04",'Europe/Moscow').do(job, sign="Рак", symbol='♋', month=month)
schedule.every().day.at("16:05",'Europe/Moscow').do(job, sign="Лев", symbol='♌', month=month)
schedule.every().day.at("16:06",'Europe/Moscow').do(job, sign="Дева", symbol='♍', month=month)
schedule.every().day.at("16:07",'Europe/Moscow').do(job, sign="Весы", symbol='♎', month=month)
schedule.every().day.at("16:08",'Europe/Moscow').do(job, sign="Скорпион", symbol='♏', month=month)
schedule.every().day.at("16:09",'Europe/Moscow').do(job, sign="Стрелец", symbol='♐', month=month)
schedule.every().day.at("16:10",'Europe/Moscow').do(job, sign="Козерог", symbol='♑', month=month)
schedule.every().day.at("16:11",'Europe/Moscow').do(job, sign="Водолей", symbol='♒', month=month)

fifteen_minutes = 15 * 60

for i in range(fifteen_minutes):
    schedule.run_pending()
    time.sleep(1)
