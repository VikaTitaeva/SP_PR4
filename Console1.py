from multiprocessing import Process
from multiprocessing import Queue
from datetime import datetime
from typing import List
import os

def performing_task(queue: Queue):
    number, degree = queue.get()
    result_raising = number ** degree

    sum = 0
    for i in range(result_raising + 1):
        sum += i
    
    with open("result.txt", "a") as file:
        file.write(f"{datetime.now().replace(microsecond=0)} >> {number}^{degree} = {result_raising}\n")

    
if __name__ == '__main__':

    queue = Queue()
    list_process :List[Process] = []
    
    while True:
        try:
            number, degree = input("Введите число и степень через пробел: ").split(" ")
            number = int(number)
            degree = int(degree)

            number_degree : tuple = (number, degree)
            queue.put(number_degree)

            process = Process(target=performing_task, args=(queue,))
            process.start()
            list_process.append(process)

        except:
            print("Ну не правильно введено!!!")
            continue
        
        finally:
            [process.join() for process in list_process]