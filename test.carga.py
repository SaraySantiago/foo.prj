#C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\python.exe

from cola import cola
import random


c = cola(20)

tries = 0
while tries < 100:
    tries += 1
    coin = random.randint(1, 2)
    if coin == 1:
        print('enqueu...')
        dice = random.randint(1, 6)
        try:
            c.enqueue(dice)
            print(c)
        except OverflowError:
         print("No entro, estaba llena")

    if coin == 2:
        print('dequeu...')
        try:
            data = c.dequeue()
            print(data)
        except ValueError:
            print("Nada sale, estaba vacía")   

total = tries
print(total)