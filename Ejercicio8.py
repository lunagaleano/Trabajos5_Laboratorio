#Ejercicio 8
'''Crea una clase base Transporte con propiedades de capacidad y velocidad máxima.
Deriva clases como Avión y Barco, e implementa métodos para calcular el tiempo de
viaje basado en la distancia y la velocidad.'''

class Transporte:
    def __init__(self, capacidad, velocidad_maxima):
        self.capacidad = capacidad
        self.velocidad_maxima = velocidad_maxima

    def imprimir_detalles(self):
        print(f"Capacidad: {self.capacidad}")
        print(f"Velocidad máxima: {self.velocidad_maxima} km/h")

class Avion(Transporte):
    def calcular_tiempo(self, distancia):
        return distancia / self.velocidad_maxima

class Barco(Transporte):
    def calcular_tiempo(self, distancia):
        return distancia / self.velocidad_maxima

        # Ejemplo de uso
a = Avion(180, 900)
print("Tiempo:", a.calcular_tiempo(1800), "horas")