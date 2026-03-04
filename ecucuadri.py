import math

class EcuacionCuadratica:

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def getA(self):
        return self.__a

    def getB(self):
        return self.__b

    def getC(self):
        return self.__c

    def getDiscriminante(self):
        return self.__b**2 - 4*self.__a*self.__c

    def getRaiz1(self):
        if self.getDiscriminante() >= 0:
            return (-self.__b + math.sqrt(self.getDiscriminante())) / (2*self.__a)
        else:
            return 0

    def getRaiz2(self):
        if self.getDiscriminante() >= 0:
            return (-self.__b - math.sqrt(self.getDiscriminante())) / (2*self.__a)
        else:
            return 0


class main():

    a, b, c = map(float, input("Ingrese a, b, c: ").split())

    ecuacion = EcuacionCuadratica(a, b, c)

    discriminante = ecuacion.getDiscriminante()
    if discriminante > 0:
        print("La ecuacion tiene dos raices",
            round(ecuacion.getRaiz1(), 6),
                "y",
            round(ecuacion.getRaiz2(), 6))

    elif discriminante == 0:
        print("La ecuacion tiene una raiz",
            round(ecuacion.getRaiz1(), 6))

    else:
        print("La ecuacion no tiene raices reales")