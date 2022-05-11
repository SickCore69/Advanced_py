import time 

class FiboIter():

    #def __init__(self, iter_max:int) -> int:        
    #    self.iter_max = iter_max      
    def __inter__(self):    # Metodo para inicializar las variables a usar
        self.n1 = 0
        self.n2 = 1
        self.count = 0
        return self

    def __next__(self): # Metodo para iterar sobre el sig. numero
        if self.count == 0:
            self.count += 1
            return self.n1  # 0
        elif self.count == 1:
            self.count += 1 
            return self.n2  # 1
        #elif self.aux <= self.iter_max:
        #    self.aux = self.n1  + self.n2 
        #    self.n1, self.n2 = self.n2, self.aux
        #    self.count +=1
        #    return self.aux
        #elif self.aux > self.iter_max:
        #    raise StopIteration
        else:
            self.aux = self.n1 + self.n2    # 0 + 1 = 1
            # self.n1 = self.n2     # Aplicando swaping a la asignacion self.n1, self.n2 = self.n2, self.aux
            # self.n2 = self.aux
            self.n1, self.n2 = self.n2, self.aux    # 0+1= 1, 1+1= 2, 1+2= 3, 2+3= 5, 3+5=8...
            self.count += 1 # Se incrementa el contador en una unidad
            return self.aux

if __name__ == '__main__':
    fibonacci = FiboIter() # Instaciar o convertir al iterador en una variable
    for element in fibonacci:   # Ciclo para recorrer al iterador fibonacci y guardar los elementos en element
        print(element)  # Imprime los elementos
        time.sleep(0.5)    # Instruccion para pausar o esperar 0.05 seg antes de pasar a la sig iteracion