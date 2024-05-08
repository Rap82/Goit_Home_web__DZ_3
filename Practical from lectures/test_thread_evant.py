# ==================================================== Реалізація багатопоточності класу EVANT.=========================================
# Evant - клас для управління потоками . Можна визначати який потік є основний а які залежні.

from threading import Thread, Event, current_thread
from random import randint
import logging
from time import sleep

def master(event:Event) : # функція яка приймає один аргумент екзепляр  класу *Event, функція в якій реалізовано наш основний потік.
    
    logging.info("Master is working...") # Принтемо "Master Event"
    sleep(1) # Встановлюємо затримку виконання коду на 1 мс.
   
    logging.info("Master finished and set Event") # Виводимо в лог "Master set Event"
    event.set() # За допомогою методу  *.set() запускаємо основний потік функції *master(event)

def worker(event:Event): # функція яка приймає один аргумент екзепляр  класу *Event, функція в якій реалізовано наш додатковий потік,
                         # який буде запускатися з дозволу основного потоку функції *master(event:Event)

    logging.info(f"{current_thread().name}- waiting ")# Вивід повіомлення про очікування додаткового потоку на виконання 
    event.wait() #За допомогою методу  *.wait() - метод дозволяє додатковому потоку очікувати на запуск після дозволу в основному .
    logging.info(f"{current_thread().name}- working ") ## Вивід повіомлення про роботу  додаткового потоку після дозволу з основного потоку.


if __name__ == "__main__":

    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s") # вбудована функція для логування  потоків за їх іменем *%(threadName)s 
    
    event = Event() # Створення *пустого екзепляру класу *Event Примітка : пустий означає 

    mast = Thread(target=master, args=(event,)) # Реалізація мастер потоку екзепляру класу *Thread який запустить в додатковому  потоці функціію *master(event)
                                                # з одним аргументом *event - *пустим екзепляром класу *Event()

    work1 = Thread(target=worker, args=(event,))# Реалізація залежного потоку екзепляру класу *Thread який запуститься в потоці функціію *worker(event) після того як завершить роботу основний потік *master(event)
                                                # з одним аргументом *event - *пустим екзепляром класу *Event()
    work2 = Thread(target=worker, args=(event,))  # Щеодин залежний поків
    work3 = Thread(target=worker, args=(event,))  # Щеодин залежний поків


    work1.start() # Стартуємо перший залежний потік
    work2.start() # Стартуємо другий залежний потік
    work3.start() # Стартуємо третій залежний потік
    sleep(0.5)    # встановлюємо паузу в 0.5 сек

    mast.start() # Після запуску залежних потоків запускаємо основний потік. Дивись результат нижче

# ++++++++++++++++++++++++++++++++++ Результат роботи коду ++++++++++++++++++++++++++++++++++++++++++++++

#Thread-2 (worker) Thread-2 (worker)- waiting 
#Thread-3 (worker) Thread-3 (worker)- waiting 
#Thread-4 (worker) Thread-4 (worker)- waiting 
#Thread-1 (master) Master is working...
#Thread-1 (master) Master finished and set Event
#Thread-2 (worker) Thread-2 (worker)- working 
#Thread-4 (worker) Thread-4 (worker)- working 
#Thread-3 (worker) Thread-3 (worker)- working

# Як бачимо з результатів , незважаючи на те що основний потік запускався в кінці всі залежні потоки були встатусі очікування поки незавершиться основний тоді почали виконуватись залежні.
# *Event дозволяє управляти виконанням потоків . Виділяти основний і залежні.
