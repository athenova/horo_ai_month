from project import *
import schedule
import time

if __name__ == '__main__':
    tg = ProjectTelegram()
    vk = ProjectVk()

    def job(type, chat_id=None, group_id=None, tags=None):
        tg.send(type=type, chat_id=chat_id, tags=tags)
        if group_id is not None:
            vk.send(type=type, group_id=group_id, image_gen=False, text_gen=False,tags=tags)

    schedule.every().day.at("18:00",'Europe/Moscow').do(job, type="pisces", chat_id='@pisces_the', group_id='229837683', tags=['#гороскоп', '#астрология', '#гороскопнамесяц', '#рыбы'])
    schedule.every().day.at("18:01",'Europe/Moscow').do(job, type="aries", chat_id='@aries_the', group_id='229837854', tags=['#гороскоп', '#астрология', '#гороскопнамесяц', '#овен'])
    schedule.every().day.at("18:02",'Europe/Moscow').do(job, type="taurus", group_id='229860740', tags=['#гороскоп', '#астрология', '#гороскопнамесяц', '#телец'])
    schedule.every().day.at("18:03",'Europe/Moscow').do(job, type="gemini", chat_id='@gemini_the', group_id='229837895', tags=['#гороскоп', '#астрология', '#гороскопнамесяц', '#близнецы'])
    schedule.every().day.at("18:04",'Europe/Moscow').do(job, type="cancer", group_id='229860780', tags=['#гороскоп', '#астрология', '#гороскопнамесяц', '#рак'])
    schedule.every().day.at("18:05",'Europe/Moscow').do(job, type="leo", group_id='229860665', tags=['#гороскоп', '#астрология', '#гороскопнамесяц', '#лев'])
    schedule.every().day.at("18:06",'Europe/Moscow').do(job, type="virgo", group_id='229860810', tags=['#гороскоп', '#астрология', '#гороскопнамесяц', '#дева'])
    schedule.every().day.at("18:07",'Europe/Moscow').do(job, type="libra", group_id='229860834', tags=['#гороскоп', '#астрология', '#гороскопнамесяц', '#весы'])
    schedule.every().day.at("18:08",'Europe/Moscow').do(job, type="scorpio", group_id='229860866', tags=['#гороскоп', '#астрология', '#гороскопнамесяц', '#скорпион'])
    schedule.every().day.at("18:09",'Europe/Moscow').do(job, type="sagittarius", group_id='229860894', tags=['#гороскоп', '#астрология', '#гороскопнамесяц', '#стрелец'])
    schedule.every().day.at("18:10",'Europe/Moscow').do(job, type="capricorn", chat_id='@capricorn_the', group_id='229837876', tags=['#гороскоп', '#астрология', '#гороскопнамесяц', '#козерог'])
    schedule.every().day.at("18:11",'Europe/Moscow').do(job, type="aquarius", chat_id='@aquarius_the', group_id='229837930', tags=['#гороскоп', '#астрология', '#гороскопнамесяц', '#водолей'])

    fifteen_minutes = 15 * 60

    for i in range(fifteen_minutes):
        schedule.run_pending()
        time.sleep(1)
