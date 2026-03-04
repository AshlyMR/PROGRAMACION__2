import math

class Estadistica:

    def __init__(self, datos):
        self.__datos = datos

    def getDatos(self):
        return self.__datos

    def promedio(self):
        return sum(self.__datos) / len(self.__datos)

    def desviacion(self):
        prom = self.promedio()
        suma = 0
        for x in self.__datos:
            suma += (x - prom) ** 2
        return math.sqrt(suma / (len(self.__datos) - 1))


class main():
    numeros = list(map(float, input("Ingrese 10 numeros: ").split()))
    estad = Estadistica(numeros)
    print("El promedio es", round(estad.promedio(), 2))
    print("La desviacion estandar es", round(estad.desviacion(), 5))