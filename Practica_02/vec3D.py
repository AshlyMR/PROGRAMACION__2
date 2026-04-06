from multimethod import multimethod
import math
from numbers import Real

class vec3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    @multimethod
    def suma(self, b: "vec3D"):
        return vec3D(self.x + b.x, self.y + b.y, self.z + b.z)

    @multimethod
    def multiplicacion(self, r: Real):
        return vec3D(r * self.x, r * self.y, r * self.z)

    def longitud(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normal(self):
        mag = self.longitud()
        if mag == 0:
            raise ValueError("No se puede normalizar un vector nulo")
        return vec3D(self.x / mag, self.y / mag, self.z / mag)

    def producto_escalar(self, b: "vec3D"):
        return self.x * b.x + self.y * b.y + self.z * b.z

    def producto_vectorial(self, b: "vec3D"):
        i = self.y * b.z - self.z * b.y
        j = self.z * b.x - self.x * b.z
        k = self.x * b.y - self.y * b.x
        return vec3D(i, j, k)
    def volumen_tetraedro(self, b: "vec3D", c: "vec3D"):
        cruz_bc = b.producto_vectorial(c)
        triple_producto = self.producto_escalar(cruz_bc)
        return (1/6) * abs(triple_producto)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

v1 = vec3D(1, 2, 3)
v2 = vec3D(4, 5, 6)
v3 = vec3D(7, 4, 0)
print("Suma:", v1.suma(v2))
print("Multiplicación por 2:", v1.multiplicacion(2))
print("Multiplicación por 2.5:", v1.multiplicacion(2.5))
print("Producto escalar:", v1.producto_escalar(v2))
print("Producto vectorial:", v1.producto_vectorial(v2))
print("Longitud de v1:", v1.longitud())
print("Vector normal de v1:", v1.normal())

vol = v1.volumen_tetraedro(v2, v3)
print(f"Vector A: {v1}")
print(f"Vector B: {v2}")
print(f"Vector C: {v3}")
print("==========================")
print(f"Volumen del tetraedro: {vol:.4f}")