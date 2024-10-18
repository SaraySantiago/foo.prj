#C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\python.exe

from cola import cola
import random

class Pila:
    def __init__(self, size):
        self.size = size
        self.items = []

    def push(self, item):
        if len(self.items) < self.size:
            self.items.append(item)
        else:
            raise Exception("La pila está llena")

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise Exception("La pila está vacía")

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return str(self.items)

c = Pila(20)

tries = 0
while tries < 100:
    tries += 1
    coin = random.randint(1, 2)
    if coin == 1:
        dice = random.randint(1, 6)
        try:
            c.push(dice)
            print("Introducimos el siguiente dato ", data, "con lo cual la lista se quedaria de la siguiente manera --> ", c)
        except:
            pass
    if coin == 2:
        print('')
        try:
            data = c.pop()
            print("Quitamos el siguiente dato --> ", data)
            print("Con lo cual la lista se nos quedaría de la siguiente manera --> ", c)

        except:
            pass

total = tries
print(total)