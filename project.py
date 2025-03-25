from simple_blogger import SimplestBlogger
from string import Template
from datetime import datetime
from datetime import timedelta
import locale
from simple_blogger.senders.TelegramSender import TelegramSender
from simple_blogger.senders.VkSender import VkSender


class Project(SimplestBlogger):
    def _example_task_creator(self):
        prompt = Template(f"Составь гороскоп на $$month $$year для знака '$sign', используй смайликии, используй не более {self.topic_word_limit} слов")
        return [{ 
            "pisces_prompt": prompt.substitute(sign='Рыбы'),
            "aries_prompt": prompt.substitute(sign='Овен'),
            "taurus_prompt": prompt.substitute(sign='Телец'),
            "gemini_prompt": prompt.substitute(sign='Близнецы'),
            "cancer_prompt": prompt.substitute(sign='Рак'),
            "leo_prompt": prompt.substitute(sign='Лев'),
            "virgo_prompt": prompt.substitute(sign='Дева'),
            "libra_prompt": prompt.substitute(sign='Весы'),
            "scorpio_prompt": prompt.substitute(sign='Скорпион'),
            "sagittarius_prompt": prompt.substitute(sign='Стрелец'),
            "capricorn_prompt": prompt.substitute(sign='Козерог'),
            "aquarius_prompt": prompt.substitute(sign='Водолей'),
        }]
    
    def _preprocess_text_prompt(self, prompt):
        locale.setlocale(locale.LC_ALL, ('ru_RU', 'UTF-8'))
        date = datetime.now() + timedelta(days=10)
        month = date.strftime('%B')
        year = date.year
        return Template(prompt).substitute(month=month, year=year)
    
    def _system_prompt(self, _):
        return f"Ты - профессиональный астролог"
    
class ProjectTelegram(Project):
    def __init__(self, **kwargs):
        super().__init__(            
            reviewer=TelegramSender(),
            senders=[TelegramSender(channel_id='@horo_ai')],
            **kwargs)
        
class ProjectVk(Project):
    def __init__(self, **kwargs):
        super().__init__(            
            reviewer=VkSender(group_id='229822833'),
            senders=[VkSender()],
            **kwargs)