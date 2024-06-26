# ==================================================== Реалізація багатопоточності класу EVANT(управління set , wait).=========================================
# Evant - клас для управління потоками . Можна визначати який потік є основний а які залежні.

from threading import Thread, Event, current_thread
from random import randint
import logging
from time import sleep



def worker_prostyj(event:Event): # функція яка приймає один аргумент екзепляр  класу *Event, функція в якій реалізовано наш додатковий потік,
                         # який буде запускатися з дозволу основного потоку функції *master(event:Event) через методом *event.set()
                         # виконує свої дії тільки після дозволу мастера.

    logging.info(f"{current_thread().name}- waiting ")# Вивід повіомлення про очікування додаткового потоку на виконання.
    event.wait() #За допомогою методу  *.wait() - метод дозволяє додатковому потоку очікувати на запуск після дозволу в основному . 
                 # Дозвіл отримується від мастера потоку методом *event.set()
    logging.info(f"{current_thread().name}- working ") ## Вивід повіомлення про роботу  додаткового потоку після дозволу з основного потоку.


def worker_skladnyj(event:Event, time:float): # функція яка приймає два аргумент - перший екзепляр  класу *Event, 
                                              # - другий *time (тип *float) - час в сек, через який запускається локальний потік поки очікується дозволу від мастера на виконання основного завдання .
                                              # функція в якій реалізовано наш додатковий потік, який виконує додаткове завдання поки мастер недозволить виконати основен.
                                              # запускатися з дозволу основного потоку функції *master(event:Event) через методом *event.set()
                                              # виконує певні дії очікуючи на виконання основної з дозволу мастера.
    while not event.is_set(): # цикл в якому буде виконуватись додатковий потік(складний : основне завдання потоку і додаткове поки мастер недозволить виконання основного) 
                              # метод *event.is_set() - поверне *True - це станеться тоді коли основний потік мастер дасть дозвіл на запуск додаткового потоку.
    
        logging.info(f"{current_thread().name}- waiting ")# Вивід повіомлення про очікування додаткового потоку на виконання.
        
        e_wait = event.wait(time) # поверне *True коли закінчиться час *time і False поки *time- триває.
        
        if e_wait :
            logging.info(f"Виконуємо роботу мастер дав добро") ## Вивід повідомлення про роботу  додаткового потоку після дозволу з основного потоку.
        else :
            logging.info(f" Робимо в потоці щось своє поки мастер не дасть добро на виконання основної роботи")

if __name__ == "__main__":

    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s") # вбудована функція для логування  потоків за їх іменем *%(threadName)s 
    
    event = Event() # Створення *пустого екзепляру класу *Event Примітка : пустий означає 

    
    work1 = Thread(target=worker_prostyj, args=(event,))# Реалізація залежного потоку екзепляру класу *Thread який запуститься в потоці функціію *worker_prostyj(event) після того як завершить роботу основний потік *master(event)
                                                # з одним аргументом *event - *пустим екзепляром класу *Event()
    work2 = Thread(target=worker_skladnyj, args=(event, 1))  # Складний додатковий потік (виконує додаткове завдання поки мастер недозволить виконання основного додаткового завдання)
                                                             # Другий аргумент час встановлено 1 сек.
    
    work1.start() # Стартуємо перший залежний потік
    work2.start() # Стартуємо другий складний залежний потік
    
    sleep(3)    # встановлюємо паузу в 2 сек

    event.set() # дозвіл на запуск додаткових потоків як складного так і простого. Примітка: мастером буде виступати основний код 
    logging.info("End program")

# ++++++++++++++++++++++++++++++++++ Результат роботи коду ++++++++++++++++++++++++++++++++++++++++++++++

# Thread-1 (worker_prostyj) Thread-1 (worker_prostyj)- waiting 
# Thread-2 (worker_skladnyj) Thread-2 (worker_skladnyj)- waiting 
# Thread-3 (worker_skladnyj) Thread-3 (worker_skladnyj)- waiting 
# Thread-3 (worker_skladnyj)  Робимо в потоці щось своє поки мастер не дасть добро на виконання основної роботи
# Thread-2 (worker_skladnyj)  Робимо в потоці щось своє поки мастер не дасть добро на виконання основної роботи
# Thread-3 (worker_skladnyj) Thread-3 (worker_skladnyj)- waiting 
# Thread-2 (worker_skladnyj) Thread-2 (worker_skladnyj)- waiting 
# MainThread End program
# Thread-1 (worker_prostyj) Thread-1 (worker_prostyj)- working 
# Thread-2 (worker_skladnyj) Виконуємо роботу мастер дав добро 
# Thread-3 (worker_skladnyj) Виконуємо роботу мастер дав добро 

# Як бачимо з результатів , 
# *worker_prostyj очікує поки мастер не дасть добро на виконання . запускається вже після завершення *MainThread End program тобто через 3 секунди поки незавершиться пауза  *sleep(3)
# *worker_skladnyj очікує поки мастер не дасть добро на виконання . запускається вже після завершення *MainThread End program тобто через 3 секунди поки незавершиться пауза  *sleep(3)
# проте поки він очікує на добро від мастер потоку виконує 3 рази додаткове завдання (оскільки час перевірки на команду від мастера 1 сек )