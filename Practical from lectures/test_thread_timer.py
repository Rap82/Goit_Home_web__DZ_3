# ================================ Реалізація багатопоточності з відкладенням по часу певних потоків за допомогою *Timer.=========================================

from threading import Timer
import logging
from time import sleep


def worker(massages):
    logging.info(massages)


if __name__ == "__main__":
    
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s") # вбудована функція для логування  потоків за їх іменем *%(threadName)s 

        
    one = Timer(interval=0.5, function=worker, args=('one',)) # організація відкладеного потоку функції *worker(massages), one - зміна яка буде містити екзепляр класу *Timer , 
                                                     # який відповідає за відкладений потік (вкористовується для запуску процесів які мають обмеження по часу для виконання певних дій (скіп - реклами чи час на ведення якихось даних для двофакторної авторизації  ))
                                                     # Де *interval=*час через який запуститься потік , внашому випадку *interval=0.5 - потік запуститься через 0,5 мілісекунди.
                                                     # *worker - імя функції(чи може ути сама функція) яка відкладенна до запуску.
                                                     # *args=("one",)) - кортеж аргументів які передаються у функцію
                                                     # Примітка: можна скоротити запис до формату  one = Timer(0.5, worker, args=('one',))
    one.name = "First Thread" # присвоюємо імя потоку 
    one.start() # *імя.start() - вбудований метод який запускає наш потік з певним іменем.

    two = Timer(interval=1.5, function=worker, args=("two",))# організація відкладеного потоку функції *worker(massages), one - зміна яка буде містити екзепляр класу *Timer , 
                                                     # який відповідає за відкладений потік (вкористовується для запуску процесів які мають обмеження по часу для виконання певних дій (скіп - реклами чи час на ведення якихось даних для двофакторної авторизації  ))
                                                     # Де *interval=*час через який запуститься потік , внашому випадку *interval=1.5 - потік запуститься через 1,5 мілісекунди.
                                                     # *worker - імя функції(чи може ути сама функція) яка відкладенна до запуску.
                                                     # *args=("too",)) - кортеж аргументів які передаються у функцію
                                                     # # Примітка: можна скоротити запис до формату  two = Timer(1.5, worker, args=('two',))
    two.name = "Second Thread" # присвоюємо імя потоку 
    two.start() # *імя.start() - вбудований метод який запускає наш потік з певним іменем.

    sleep(1) # Вбудована функція *sleep(*час зупинки) модуля *time яка зупиняє всі процеси на в коді на певний час в мілісекундах , в нашому випадку 1 мс.

    one.cancel() # вбудований метод відміни виконання потоку якщо він ще не виконався , в нашому випадку відміни першого потоку невідбудеться оскільки він вспіє виконатись за 1 мс поки всі процеси будуть призупиненні функцією *sleep(1)
                 # А ось други потік буде відмінений оскльки він має запуститись через 1,5 мс.
    two.cancel() # відміна другого потоку. якщо збільшити *sleep() до двох мс *sleep(2) то відбудуться два потоки.


