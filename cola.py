#C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\python.exe
import poplib
    
class cola:
    
    __data = []
    __maxsize = None
    
    def __init__(self, size):
        self.__maxsize = size
        
    def len(self) -> int:
        return len(self.__data)
        
    def __str__ (self) -> str:
            answ = "<"
            answ += f"{self.len()} de {self.__maxsize}, {self.__data}"
            if self.esVacia(): answ += "VACIA"
            if self.esLLena(): answ += " LA COLA ESTA LLENA"
            answ += ">"
            return answ
            
    def esVacia(self) -> bool: 
        pass 
    def esLLena(self) -> bool: 
       return len(self.__data) == self.__maxsize
            
    def enqueue(self ,something):
         if not self.esLLena():
            self.__data.append(something)
         else:
            raise OverflowError(f"Error: La cola está vacía.")
    
    def dqueue (self) -> object:
         if len(self.__data) == 0:
             raise ValueError (f"queue: estar vacia")
         else:
             item = self.__data[0]
             self.__data = self.__data[1:]
             return item
             

if __name__ == "__main__":
    
    c = cola(4)
    print(c)
    
    try:
        c.enqueue (55)
        print (c) 
        c.enqueue (11)
        print (c)
        c.enqueue (22)
        print (c)
        c.enqueue (33)
        print (c)
        c.enqueue (44)
        print (c) 
    except OverflowError:
        print(55, "No pudo entrar ya que la cola está llena")
        
    print (c)
    try:
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
    except ValueError:
        print ("No hay nada en la cola")    
       
   
    #TODO programar dqueue 