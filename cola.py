#C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\python.exe
import poplib
    
class cola:
    
    __data = []
    __maxsize = None
    
    def __init__(self, size = 10):
        self.__maxsize = size
        
    def len(self):
        return len(self.__data)
        
    def __str__ (self) -> str:
            answ = "<"
           # answ += f"{self.len()} de {self.__maxsize}, {self.__data}"
            answ +=f"{len(self)} de {self.__maxsize}, {self.__data}"
            if self.esVacia(): answ += "VACIA"
            if self.esLLena(): answ += " LA COLA ESTA LLENA"
            answ += ">"
            return answ
            
    def esVacia(self) -> bool: 
        return len(self)== 0 
    def esLLena(self) -> bool: 
       return len(self) == self.__maxsize
            
    def enqueue(self ,something):
         if not self.esLLena():
            self.__data.append(something)
         else: 
            raise OverflowError(f"queue: La cola está llena.")
    
    def dqueue (self) -> object:
         if len(self) == 0:
             raise ValueError (f"queue: estar vacia")
         else:
             item = self.__data[0]
             self.__data = self.__data[1:]
             return item
             

if __name__ == "__main__":
    
    c = cola(4)
    print(c)
    
    try: 
        c.enqueue (11)
        print (c)
        c.enqueue (22)
        print (c)
        c.enqueue (33)
        print (c)
        c.enqueue (44)
        print (c) 
       # c.enqueue (55)
        # print (c)
        item = c.dqueue()
        print (item, c)
        item = c.dqueue()
        print (item, c)
        item = c.dqueue()
        print (item, c)
        item = c.dqueue()
        print (item, c)
        item = c.dqueue()
        print (item, c)
        print ("FINAL DEL TRY")
    except OverflowError:
        print("No entro, estaba llena")
    except ValueError:
        print("Nada sale, estaba vacía")
        

 