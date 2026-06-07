#Ejercicio 3
'''Diseña una jerarquía de clases de animales, con clases base como
Animal y derivadas como Perro y Gato. Cada clase debe tener un método
para emitir su sonido característico. Agrega un método en la clase base
para mostrar detalles generales.'''

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def imprimir_detalles(self):
        print(f"Animal: {self.nombre}")

class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def emitir_sonido(self):
        return "Guau guau"

    def imprimir_detalles(self):
        super().imprimir_detalles()
        print(f"Sonido: {self.emitir_sonido()}")

class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def emitir_sonido(self):
        return "Miauuuuuuu"

    def imprimir_detalles(self):
        super().imprimir_detalles()
        print(f"Sonido: {self.emitir_sonido()}")

        # Ejemplo de uso
p = Perro("Lola")
p.imprimir_detalles()
print()
g = Gato("Miel")
g.imprimir_detalles()