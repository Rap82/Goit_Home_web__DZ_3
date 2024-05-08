# ================================ Реалізація лочення потоків а допомгою класу Rlock - модуля *hreading ========


from threading import Thread, RLock
from random import randint
import logging
from time import sleep

counter = 0 # Зміна для лічильника , початкове значення 0 .

lock = RLock() # зміна *lock яка буде містити екзепляр класу *RLock

def worker(): # Функція без аргументів , будемо її запускати в 5 потоків і лочити їх за допомогою *RLock.

    global counter # Робимо нашу зміну *counter глобальною
    
    while True : #  Безкінечний цикл в якому будемо збільшувати наш *counter на 1 з випадковою затримкою від 1 до 4 мс.

        #lock.acquire() # *імя_екзепляру_Rlock.acquire() - метод *.acquire()- лочить(резервує ресурс для потоку поки він виконується) потік 
        
        with lock: # менеджер контексту для локу потоків ,  with *імя_екзепляру_класу_Rlock : в тіло контексту вказуємо потік який потріно за лочити і позавершеню розлочити атоматично. 
            counter += 1 # Збільшуємо на 1 наш *counter
            sleep(randint(a=1, b=2)) # Функція *sleep(*час затримки) - *randint(a=1, b=4) - функція *randint(a=(ціле число), b=ціле число) - генерує виадкове число між значенням *a і *b
            with open("Result.txt", 'a') as fh:
                fh.write(f'Counter -{counter}\n')

        #lock.release() # *імя_екзепляру_Rlock.release() - метод *.release() - розлочує ресурс 
                    # Примітка : Використання *.acquire() і відповідно *.release() є небажаним. 
                    # Замість того птрібно використовувати менедер контекстів with ... as - як і дляроботи з файлами.
if __name__ == "__main__":
    
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s") ## вбудована функція для логування  потоків за їх іменем *%(threadName)s 
    logging.info("Starting")
    for i in range(5):
        th= Thread(target=worker, name=(f"Threads - {i}",))
        th.start()

    logging.info("End program")