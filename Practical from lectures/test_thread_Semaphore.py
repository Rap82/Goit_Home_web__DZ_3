# ==================================================== Реалізація багатопоточності клас Semaphore.=========================================
# Semaphore - клас для управління потоками . використовується коли потрібно встановвити вказану кількість потоків і не більше (черга потоків).

from threading import Thread, Semaphore
import logging
from time import sleep



def worker(semaphore:Semaphore): # функція яка приймає один аргумент екзепляр  класу *Semaphore, функція в якій реалізовано наш додатковий потік,
                         # який буде запускатися з дозволу основного потоку функції 

    logging.info("Waiting ")# Вивід повіомлення про очікування додаткового потоку на виконання 
    with semaphore: # менеджер контексту запускає виконання потоку   обовязково завершить потік після його виконання  
        logging.info("Got semaphore ") # вивід повідомлення провиконання потоку.
        sleep(1)
        logging.info(f"Finish operation ") ## Вивід повіомлення про роботу звільнення місця під інший потік.


if __name__ == "__main__":

    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s") # вбудована функція для логування  потоків за їх іменем *%(threadName)s 
    
    pool = Semaphore(3) # Створюємо екзепляр класу Semaphore(*Кліькість_одночас_дозволених_потоків) так званий *пул потоків.
    for i in range(12):
        work1= Thread(target=worker, args=(pool,))
        work1.start()


# ++++++++++++++++++++++++++++++++++ Результат роботи коду ++++++++++++++++++++++++++++++++++++++++++++++
# Примітка : З прикладу нижче видно що запускаються не більше 3 потоків всі інші очікують

# Thread-1 (worker) Waiting 
# Thread-1 (worker) Got semaphore # відпрацював перший потік 
# Thread-2 (worker) Waiting       
# Thread-2 (worker) Got semaphore # відпрацював другий  потік 
# Thread-3 (worker) Waiting       
# Thread-4 (worker) Waiting       
# Thread-3 (worker) Got semaphore # відпрацював третій  потік
# Thread-5 (worker) Waiting       
# Thread-6 (worker) Waiting       
# Thread-7 (worker) Waiting       
# Thread-8 (worker) Waiting       
# Thread-9 (worker) Waiting       
# Thread-10 (worker) Waiting      
# Thread-11 (worker) Waiting      
# Thread-12 (worker) Waiting      
# Thread-1 (worker) Finish operation # Завершив роботу перший потік 
# Thread-4 (worker) Got semaphore    #  відпрацював 4  потік
# Thread-2 (worker) Finish operation # Завершив роботу дрігий  потік
# Thread-5 (worker) Got semaphore    #  відпрацював 5  потік
# Thread-3 (worker) Finish operation # Завершив роботу третії  потік
# Thread-6 (worker) Got semaphore    #  відпрацював 6 потік
# Thread-4 (worker) Finish operation 
# Thread-5 (worker) Finish operation 
# Thread-7 (worker) Got semaphore    
# Thread-6 (worker) Finish operation 
# Thread-8 (worker) Got semaphore    
# Thread-9 (worker) Got semaphore    
# Thread-7 (worker) Finish operation 
# Thread-10 (worker) Got semaphore 
# Thread-8 (worker) Finish operation
# Thread-9 (worker) Finish operation
# Thread-11 (worker) Got semaphore
# Thread-12 (worker) Got semaphore
# Thread-10 (worker) Finish operation 
# Thread-11 (worker) Finish operation 
# Thread-12 (worker) Finish operation