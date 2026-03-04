import time
import random

class Cronometro:
    
    def __init__(self):
        self.__inicia = time.time()
        self.__finaliza = None

    def __str__(self):
        return f"inicia: {self.__inicia}, finaliza: {self.__finaliza}"

    def getinicia(self):
        return self.__inicia

    def getfinaliza(self):
        return self.__finaliza

    def inicia(self):
        self.__inicia = time.time()

    def detener(self):
        self.__finaliza = time.time()

    def lapsoDeTiempo(self):
        return (self.__finaliza - self.__inicia) * 1000


def seleccion(lista):
    n = len(lista)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]


numeros = [random.randint(1, 100000) for _ in range(100000)]

cron = Cronometro()

cron.inicia()
seleccion(numeros)
cron.detener()

print("Tiempo en milisegundos:", cron.lapsoDeTiempo())