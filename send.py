from project import Project
import schedule
import time

if __name__ == '__main__':
    p = Project()

    schedule.every().day.at("18:00",'Europe/Moscow').do(p.send, type="pisces", chat_id='@pisces_the')
    schedule.every().day.at("18:01",'Europe/Moscow').do(p.send, type="aries", chat_id='@aries_the')
    schedule.every().day.at("18:02",'Europe/Moscow').do(p.send, type="taurus")
    schedule.every().day.at("18:03",'Europe/Moscow').do(p.send, type="gemini", chat_id='@gemini_the')
    schedule.every().day.at("18:04",'Europe/Moscow').do(p.send, type="cancer")
    schedule.every().day.at("18:05",'Europe/Moscow').do(p.send, type="leo")
    schedule.every().day.at("18:06",'Europe/Moscow').do(p.send, type="virgo")
    schedule.every().day.at("18:07",'Europe/Moscow').do(p.send, type="libra")
    schedule.every().day.at("18:08",'Europe/Moscow').do(p.send, type="scorpio")
    schedule.every().day.at("18:09",'Europe/Moscow').do(p.send, type="sagittarius")
    schedule.every().day.at("18:10",'Europe/Moscow').do(p.send, type="capricorn", chat_id='@capricorn_the')
    schedule.every().day.at("18:11",'Europe/Moscow').do(p.send, type="aquarius", chat_id='@aquarius_the')

    fifteen_minutes = 15 * 60

    for i in range(fifteen_minutes):
        schedule.run_pending()
        time.sleep(1)
