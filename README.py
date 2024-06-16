"""
    examples:
        company = Company(name="Yandex")
        offer = Offer()
        senior_developer = George()
        company.send_offer(offer, senior_developer)
"""


from typing import Tuple, List, Dict
from abc import ABC
from queue import Queue
from datetime import datetime


class Offer:
    pass


class Developer(ABC):
    _birthday: Tuple[int, int, int]
    _email: str
    _telegram: str
    langs: List[str]
    queue_offers: Queue
    
    def get_offer_job(self, offer: Offer):
        self.queue_offers.put(offer)
        self.send_notification()
    
    def send_message(self, telegram_username: str):
        pass
    
    def send_notification(self):
        if not self.queue_offers.empty():
            self.send_message(self._telegram)
            

class Company:
    def __init__(self, name: str) -> None:
        self.name = name
     
    @classmethod
    def send_offer(cls, offer: Offer, developer: Developer):
        developer.get_offer_job(offer=offer)
        
        
class George(Developer):
    
    def __init__(self,):
        self.langs = ['Armenian', 'Russian', 'English']
        self._telegram = "t.me/GeorgiKn"
        self._email = "jorj.knyazyan.15@gmail.com"
        self._birthday = (2024, 7, 3)
        self.queue_offers = Queue()
        
    @property
    def contacts(self) -> Tuple[str, str]:
        return self._telegram, self._email
    
    @property
    def age(self) -> int:
        age = self.__calculate_age(self._birthday)
        return age
    
    @staticmethod
    def __calculate_age(birthday: tuple[int, int, int]) -> int:
        today = datetime.today()
        year, month, day = birthday
        return today.year - year - ((today.month, today.day) < (month, day))
	
    @property
    def coding(self) -> Tuple[Dict[str, List[str]], Dict[str, List[str]], List[str], List[str]]:
        langs = {
            'expert'      : ['python'],
            'intermediate': ['js'],
        },
        frameworks = {
            'python'      : ['fastapi', 'django', 'flask'],
            'js'          : ['vue3', 'nuxt3', 'vuetify']   
        }
        specialities  = ['web/app', 'backend', 'ai']
        ide           = ['vscode', 'pycharm', 'zed']
        
        return langs, frameworks, specialities, ide
    
  
        
        
