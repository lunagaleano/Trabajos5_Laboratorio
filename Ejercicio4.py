#Ejercicio 4
'''Define una clase Vehiculo con propiedades marca, modelo y año.
Crea clases derivadas como Automovil y Motocicleta, incorporando un
método para calcular la eficiencia de combustible y otro para proyectar
la cantidad de combustible necesaria para un viaje.'''

class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def imprimir_detalles(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, año, km_por_litro):
        super().__init__(marca, modelo, año)
        self.km_por_litro = km_por_litro

    def combustible_necesario(self, distancia):
        return distancia / self.km_por_litro

    def imprimir_detalles(self):
        super().imprimir_detalles()
        print(f"Eficiencia: {self.km_por_litro} km/l")

class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, km_por_litro):
        super().__init__(marca, modelo, año)
        self.km_por_litro = km_por_litro

    def combustible_necesario(self, distancia):
        return distancia / self.km_por_litro

    def imprimir_detalles(self):
        super().imprimir_detalles()
        print(f"Eficiencia: {self.km_por_litro} km/l")

        # Ejemplo de uso
a = Automovil("Toyota", "Corolla", 2022, 25)
a.imprimir_detalles()
print("Combustible para 300 km:", a.combustible_necesario(300), "litros")