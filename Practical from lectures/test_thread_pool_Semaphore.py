# ==================================================== Реалізація багатопоточності клас Semaphore (pool - з логуванням процесу виконання потоків).=========================================
# Semaphore - клас для управління потоками . використовується коли потрібно встановвити вказану кількість потоків і не більше (черга потоків).

from threading import Thread, Semaphore,RLock,current_thread
import logging
from random import randint
from time import sleep

class Logger:
    def __init__(self) -> None:
        self.active = []
        self.lock= RLock()
    
    def make_active(self, name):
        with self.lock :
            self.active.append(name)
            logging.info(f"Почав роботу потік-{name} . Пул потоку {self.active}")
    def make_inactive(self, name):
        with self.lock :
            self.active.remove(name)
            logging.info(f"закінчив роботу потік-{name} . Пул потоку {self.active}")


def worker(semaphore:Semaphore, log:Logger): # функція яка приймає два аргументи . один аргумент екзепляр  класу *Semaphore,(визначає максимальну кількість одночас працюючих потоків) 
                                            #  Другий аргумент екзепляр класу *Logger . 
    
    logging.info("Waiting ")# Вивід повіомлення про очікування додаткового потоку на виконання 
    with semaphore: # менеджер контексту запускає виконання потоку   обовязково завершить потік після його виконання 
        name = current_thread().name # Метод повертає імя поточного потоку який виконується.
        log.make_active(name) # активовуємо лог потоку з відповідним імям. 
        logging.info("Got semaphore ") # вивід повідомлення провиконання потоку.
        sleep(randint(a=1, b=3))
        logging.info(f"Finish operation ") ## Вивід повіомлення про роботу звільнення місця під інший потік.
        log.make_inactive(name) # Деактивовуємо лог потоку з відповідним імям. 


if __name__ == "__main__":

    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s") # вбудована функція для логування  потоків за їх іменем *%(threadName)s 
    
    pool = Semaphore(3) # Створюємо екзепляр класу Semaphore(*Кліькість_одночас_дозволених_потоків) так званий *пул потоків.
    logger=Logger()

    for i in range(12):
        work1= Thread(target=worker, args=(pool, logger))
        work1.start()

# +++++++++++++++++++++++++++++++++Результат виконання коду ++++++++++++++++++++++++++++

# Thread-1 (worker) Waiting 
# Thread-1 (worker) Почав роботу потік-Thread-1 (worker) . Пул потоку ['Thread-1 (worker)']
# Thread-2 (worker) Waiting 
# Thread-1 (worker) Got semaphore 
# Thread-3 (worker) Waiting 
# Thread-2 (worker) Почав роботу потік-Thread-2 (worker) . Пул потоку ['Thread-1 (worker)', 'Thread-2 (worker)']
# Thread-4 (worker) Waiting 
# Thread-5 (worker) Waiting 
# Thread-6 (worker) Waiting 
# Thread-2 (worker) Got semaphore 
# Thread-3 (worker) Почав роботу потік-Thread-3 (worker) . Пул потоку ['Thread-1 (worker)', 'Thread-2 (worker)', 'Thread-3 (worker)']
# Thread-7 (worker) Waiting 
# Thread-8 (worker) Waiting 
# Thread-9 (worker) Waiting 
# Thread-10 (worker) Waiting 
# Thread-11 (worker) Waiting 
# Thread-3 (worker) Got semaphore 
# Thread-12 (worker) Waiting 
# Thread-1 (worker) Finish operation 
# Thread-1 (worker) закінчив роботу потік-Thread-1 (worker) . Пул потоку ['Thread-2 (worker)', 'Thread-3 (worker)']
# Thread-4 (worker) Почав роботу потік-Thread-4 (worker) . Пул потоку ['Thread-2 (worker)', 'Thread-3 (worker)', 'Thread-4 (worker)']
# Thread-4 (worker) Got semaphore 
# Thread-2 (worker) Finish operation 
# Thread-2 (worker) закінчив роботу потік-Thread-2 (worker) . Пул потоку ['Thread-3 (worker)', 'Thread-4 (worker)']
# Thread-5 (worker) Почав роботу потік-Thread-5 (worker) . Пул потоку ['Thread-3 (worker)', 'Thread-4 (worker)', 'Thread-5 (worker)']
# Thread-5 (worker) Got semaphore 
# Thread-3 (worker) Finish operation 
# Thread-3 (worker) закінчив роботу потік-Thread-3 (worker) . Пул потоку ['Thread-4 (worker)', 'Thread-5 (worker)']
# Thread-4 (worker) Finish operation
# Thread-6 (worker) Почав роботу потік-Thread-6 (worker) . Пул потоку ['Thread-4 (worker)', 'Thread-5 (worker)', 'Thread-6 (worker)']
# Thread-6 (worker) Got semaphore
# Thread-4 (worker) закінчив роботу потік-Thread-4 (worker) . Пул потоку ['Thread-5 (worker)', 'Thread-6 (worker)']
# Thread-7 (worker) Почав роботу потік-Thread-7 (worker) . Пул потоку ['Thread-5 (worker)', 'Thread-6 (worker)', 'Thread-7 (worker)']
# Thread-7 (worker) Got semaphore
# Thread-6 (worker) Finish operation 
# Thread-6 (worker) закінчив роботу потік-Thread-6 (worker) . Пул потоку ['Thread-5 (worker)', 'Thread-7 (worker)']
# Thread-7 (worker) Finish operation
# Thread-8 (worker) Почав роботу потік-Thread-8 (worker) . Пул потоку ['Thread-5 (worker)', 'Thread-7 (worker)', 'Thread-8 (worker)']
# Thread-8 (worker) Got semaphore
# Thread-7 (worker) закінчив роботу потік-Thread-7 (worker) . Пул потоку ['Thread-5 (worker)', 'Thread-8 (worker)']
# Thread-9 (worker) Почав роботу потік-Thread-9 (worker) . Пул потоку ['Thread-5 (worker)', 'Thread-8 (worker)', 'Thread-9 (worker)']
# Thread-9 (worker) Got semaphore
# Thread-5 (worker) Finish operation 
# Thread-5 (worker) закінчив роботу потік-Thread-5 (worker) . Пул потоку ['Thread-8 (worker)', 'Thread-9 (worker)']
# Thread-10 (worker) Почав роботу потік-Thread-10 (worker) . Пул потоку ['Thread-8 (worker)', 'Thread-9 (worker)', 'Thread-10 (worker)']
# Thread-10 (worker) Got semaphore
# Thread-8 (worker) Finish operation
# Thread-8 (worker) закінчив роботу потік-Thread-8 (worker) . Пул потоку ['Thread-9 (worker)', 'Thread-10 (worker)']
# Thread-11 (worker) Почав роботу потік-Thread-11 (worker) . Пул потоку ['Thread-9 (worker)', 'Thread-10 (worker)', 'Thread-11 (worker)']
# Thread-11 (worker) Got semaphore
# Thread-9 (worker) Finish operation
# Thread-9 (worker) закінчив роботу потік-Thread-9 (worker) . Пул потоку ['Thread-10 (worker)', 'Thread-11 (worker)']
# Thread-12 (worker) Почав роботу потік-Thread-12 (worker) . Пул потоку ['Thread-10 (worker)', 'Thread-11 (worker)', 'Thread-12 (worker)']
# Thread-12 (worker) Got semaphore
# Thread-10 (worker) Finish operation 
# Thread-10 (worker) закінчив роботу потік-Thread-10 (worker) . Пул потоку ['Thread-11 (worker)', 'Thread-12 (worker)']
# Thread-11 (worker) Finish operation 
# Thread-11 (worker) закінчив роботу потік-Thread-11 (worker) . Пул потоку ['Thread-12 (worker)']
# Thread-12 (worker) Finish operation 
# Thread-12 (worker) закінчив роботу потік-Thread-12 (worker) . Пул потоку []