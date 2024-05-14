class Vehiculo:
    def __init__(self, marca, modelo, ruedas):
        self.marca = marca
        self.modelo = modelo
        self.ruedas = ruedas

class Coche(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo, 4)

class Moto(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo, 2)

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo, 2)

def catalogar(vehiculos, ruedas=None):
    if ruedas is not None:
        vehiculos_filtrados = [vehiculo for vehiculo in vehiculos if vehiculo.ruedas == ruedas]
        print(f"Se han encontrado {len(vehiculos_filtrados)} vehículos con {ruedas} ruedas:")
        for vehiculo in vehiculos_filtrados:
            print(f"Clase: {type(vehiculo).__name__}, Marca: {vehiculo.marca}, Modelo: {vehiculo.modelo}, Ruedas: {vehiculo.ruedas}")
    else:
        for vehiculo in vehiculos:
            print(f"Clase: {type(vehiculo).__name__}, Marca: {vehiculo.marca}, Modelo: {vehiculo.modelo}, Ruedas: {vehiculo.ruedas}")

# Crear objetos de cada subclase
coche = Coche("Ford", "Mustang")
moto = Moto("Honda", "CBR")
bicicleta = Bicicleta("Trek", "Mountain Bike")

# Añadir los objetos a la lista de vehiculos
vehiculos = [coche, moto, bicicleta]

# Llamar a la función catalogar sin argumento ruedas
catalogar(vehiculos)

# Llamar a la función catalogar con argumento ruedas = 2
catalogar(vehiculos, 2)

# Llamar a la función catalogar con argumento ruedas = 4
catalogar(vehiculos, 4)
