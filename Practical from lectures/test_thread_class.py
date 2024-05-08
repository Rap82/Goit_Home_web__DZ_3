
# ==================================================== Перевизначення вбудованого класу Thread, модуля *theading =========================================

from threading import Thread
from random import randint
import logging
from time import sleep

#+++++++++++++++++++++++++++++++++++++++++++++++++++ Модуь threading вдодований клас Thread  +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Thread(group = None, target = None, name= None, args=None,  kwargs = None, *, daemon = None) # вбудований калс Thread(*параметри) калс модуля *threading 
                                                                #- для реалізації багатопоточності в phyton. 
                                                                # необовязковий параметер *group = None(позамовчуванні), - відповідає за груування потоків.
                                                                # параметер *target = None(позамовчуванні), - відповідає за функцію, чи її імя , яку будемо розбивати на потоки
                                                                # необовязковий параметер *name= None(позамовчуванні) ,-  відповідає за імя потоку.
                                                                # параметер *args=None(позамовчуванні), - відає за аргументи(дані чи зміні) які передаються в потік. 
                                                                # необовязковий параметер *kwargs = None , - відає за параметри(функції чи їх імена)  які передаються в потік.
                                                                # необовязковий параметер *daemon = None , *daemon = True - відповідає за зупинку всіх потоків по завершеню основного потоку , 
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class My_Theard(Thread):
    def __init__(self, group = None, target = None, name= None, args=None,  kwargs = None, *, daemon = None) -> None:
        super().__init__(group=group, target=target, name=name, args=args, kwargs=kwargs, daemon=daemon)
        self.args =args
    
    def run(self):
        ttl = randint(a=1, b=3)
        sleep(ttl)
        logging.info(f"My Thread {self.name}  {ttl} - by seconds ")

if __name__ == "__main__" :

    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(message)s" ) # вбудована фукуція *logging з методом *.basicConfig() модуля *logging , для відслідковування подій які відбуваються в потоках чи процесах.

    threads = [] # пустий список в який будемо збирати наші потоки. 

    for i in  range(5):

        th= My_Theard( name=f"Thread {i+2}", args=(f"Count {i}",)) # зміна яка відповідає за поточний потік , є екзепляром класу *My_Theard з відповідними параметрами.
        th.start() # метод імя.start() - метод який активовує відповідний потік з відповідним іменем.В нашому випадку імя= th.
        threads.append(th) # доаємо відповідне імя в список *threads для подальшої роботи з ним. 

    [thr.join() for thr in threads] # цикл  в якому очікуємо завершення всіх процесів в потоках, метод імя.join() - очікує завершення потоку з певним іменем.
    
    logging.info("End proga") # Вбудована функція *logging модуля *logging.  з методом *.info("*Будь яке повідомлення") для виведення повідомлення в лог файл чи консоль .Аналог print(). 

 
