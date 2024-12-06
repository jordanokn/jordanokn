```python

"""
    examples:
        
        company = Company(name="Yandex")
        offer = Offer(description="very interesting project")
        senior_developer = George(
            langs=["Russian", "English", "Armenian"],
            telegram="t.me/GeorgiKn",
            email="jorj.knyazyan.15@gmail.com",
            birthday=(2024, 7, 3),
        )
        company.invite_to_work(offer, senior_developer)
"""


from typing import Tuple, List, Dict, Literal
from abc import ABC
from queue import Queue
from datetime import datetime

from pydantic import BaseModel, Field


class Offer:
    rate_in_hour: int = Field(alias='RateInHout', default=25)
    currency: Literal["USD", "USDT"]
    description: str


class Developer(ABC):
        
    def __init__(self, langs: tuple, telegram: str, email: str, birthday: tuple):
        self._birthday: Tuple[int, int, int] = birthday
        self._email: str = email
        self._telegram: str = telegram
        self.langs: Tuple[str] = langs
        self.queue_offers: Queue = Queue() 

    @property
    def contacts(self) -> Tuple[str, str]:
        return self._telegram, self._email

    @property    
    def hard_skills(self) -> Tuple:
        raise NotImplementedError

    @property
    def age(self) -> int:
        age = self.__calculate_age(self._birthday)
        return age

    def send_offer(self, offer: Offer):
        self.queue_offers.put(offer)
        self._send_notification()

    def _send_message(self, telegram_username: str):
        pass
    
    def __calculate_age(self,) -> int:
        today = datetime.today()
        year, month, day = self._birthday
        return today.year - year - ((today.month, today.day) < (month, day))	

    def _send_notification(self):
        if not self.queue_offers.empty():
            self.send_message(self._telegram)
            

class Company:
    def __init__(self, name: str) -> None:
        self.name = name
     
    @classmethod
    def invite_to_work(cls, offer: Offer, developer: Developer):
        developer.send_offer(offer=offer)
        
        
class George(Developer):
  
    @property
    def hard_skills(self) -> Tuple[Dict[str, List[str]], Dict[str, List[str]], List[str], List[str]]:
        langs = {
            'expert'      : ['python'],
            'intermediate': ['js'],
        },
        frameworks = {
            'python'      : ['fastapi', 'django', 'flask'],
            'js'          : ['vue3', 'nuxt3', 'vuetify']   
        }
        specialities  = ['web/app', 'backend', 'ai']
        ide           = ['vscode', 'vim']
        
        return langs, frameworks, specialities, ide
```
        
