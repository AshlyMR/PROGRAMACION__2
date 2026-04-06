from multimethod import multimethod
import math
class miPunto:
    # (b) y (c): Constructor
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    # (a): Atributos y métodos getter
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    #  Pendiente respecto al origen
    def tiene_misma_pendiente(self, otro: "miPunto"):
        if self.x == 0 or otro.x == 0:
            return False 
        m1 = self.y / self.x
        m2 = otro.y / otro.x
        return m1 == m2
    #(d): Método distancia 
    @multimethod
    def distancia(self,otro:"miPunto"):
        return math.sqrt((otro.getX()-self.x)**2+(otro.getY()-self.y)**2)
    #(e): Método distancia para coordenadas x e
    @multimethod
    def distancia(self,x:float,y:float):
        return math.sqrt((x-self.x)**2+(y-self.y)**2)
    #class main
p1=miPunto()
p2=miPunto(10,30.5)
print(p1.distancia(p2))
#maineje
pA = miPunto(2, 1)
pB = miPunto(4, 2)

print(f"Comparando A{pA.x, pA.y} y B{pB.x, pB.y}:")
if pA.tiene_misma_pendiente(pB):
    print("Tiene la misma pendiente")
else:
    print("No tienen la misma pendiente")

print("----------------------------------")
pC = miPunto(3, 2)
pD = miPunto(6, 5)

print(f"Comparando C{pC.x, pC.y} y D{pD.x, pD.y}:")
if pC.tiene_misma_pendiente(pD):
    print("Tiene la misma pendiente")
else:
    print("No tienen la misma pendiente")