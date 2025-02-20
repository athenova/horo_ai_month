import os
import telebot
import locale
from openai import OpenAI
from datetime import datetime
from datetime import timedelta

AI_TEXT_MODEL = 'gpt-4o-mini'
BOT_TOKEN_NAME = "ATHE_BOT_TOKEN"
BOT_TOKEN = os.environ.get(BOT_TOKEN_NAME)
CHAT_ID = -1002374309134
#CHAT_ID = '@horo_ai'

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
    text = f"""{symbol} **{sign}. {month}**  {symbol}

{text}    
"""
    bot.send_message(chat_id=CHAT_ID, text=text, parse_mode="Markdown")

locale.setlocale(locale.LC_ALL, ('ru_RU', 'UTF-8'))
date = datetime.now() + timedelta(days=10)
month = date.strftime('%B')

job('Рыбы', symbol='♓', month=month)