import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
    def cuadrante(self):
        if self.x == 0 and self.y != 0:
            return "El punto está sobre el eje Y"
        elif self.x != 0 and self.y == 0:
            return "El punto está sobre el eje X"
        elif self.x == 0 and self.y == 0:
            return "El punto está sobre el origen"
        else:
            if self.x > 0 and self.y > 0:
                return "El punto está en el primer cuadrante"
            elif self.x < 0 and self.y > 0:
                return "El punto está en el segundo cuadrante"
            elif self.x < 0 and self.y < 0:
                return "El punto está en el tercer cuadrante"
            else:
                return "El punto está en el cuarto cuadrante"
    
    def vector(self, punto):
        vector_x = punto.x - self.x
        vector_y = punto.y - self.y
        return f"El vector resultante entre los puntos {self} y {punto} es ({vector_x},{vector_y})"
    
    def distancia(self, punto):
        distancia = math.sqrt((punto.x - self.x)**2 + (punto.y - self.y)**2)
        return f"La distancia entre los puntos {self} y {punto} es {distancia}"

class Rectangulo:
    def __init__(self, punto_inicial=Punto(), punto_final=Punto()):
        self.punto_inicial = punto_inicial
        self.punto_final = punto_final
    
    def base(self):
        return abs(self.punto_final.x - self.punto_inicial.x)
    
    def altura(self):
        return abs(self.punto_final.y - self.punto_inicial.y)
    
    def area(self):
        return self.base() * self.altura()

# Crear puntos
A = Punto(2, 3)
B = Punto(5, 5)
C = Punto(-3, -1)
D = Punto()

# Imprimir puntos
print(A)
print(B)
print(C)
print(D)

# Consultar cuadrantes
print(A.cuadrante())
print(C.cuadrante())
print(D.cuadrante())

# Consultar vectores
print(A.vector(B))
print(B.vector(A))

# Consultar distancias
print(A.distancia(B))
print(B.distancia(A))

# Determinar punto más lejano al origen
distancia_A = A.distancia(Punto())
distancia_B = B.distancia(Punto())
distancia_C = C.distancia(Punto())

if distancia_A > distancia_B and distancia_A > distancia_C:
    print("El punto A está más lejos del origen")
elif distancia_B > distancia_A and distancia_B > distancia_C:
    print("El punto B está más lejos del origen")
else:
    print("El punto C está más lejos del origen")

# Crear rectángulo
rectangulo = Rectangulo(A, B)

# Consultar base, altura y área del rectángulo
print(rectangulo.base())
print(rectangulo.altura())
print(rectangulo.area())
