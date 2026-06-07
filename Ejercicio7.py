#Ejercicio 7
'''Define una clase Instrumento con propiedades nombre y material.
Crea clases derivadas como Guitarra y Piano, agregando métodos para
tocar notas musicales y un método en la clase base para indicar el tipo de sonido.'''

class Instrumento:
    def __init__(self, nombre, material):
        self.nombre = nombre
        self.material = material

    def tipo_sonido(self):
        return "Sonido musical"

    def imprimir_detalles(self):
        print(f"Instrumento: {self.nombre}")
        print(f"Material: {self.material}")

class Guitarra(Instrumento):
    def tocar_nota(self):
        return "Do"

    def imprimir_detalles(self):
        super().imprimir_detalles()
        print(f"Nota: {self.tocar_nota()}")

class Piano(Instrumento):
    def tocar_nota(self):
        return "Mi"

    def imprimir_detalles(self):
        super().imprimir_detalles()
        print(f"Nota: {self.tocar_nota()}")

        # Ejemplo de uso
g = Guitarra("Guitarra Clásica", "Madera")
g.imprimir_detalles()