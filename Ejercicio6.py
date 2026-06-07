#Ejercicio 6
'''Diseña una jerarquía de clases que incluya Persona y clases derivadas como
Estudiante y Profesor. Implementa métodos para asignar roles y mostrar información
específica de cada rol, junto con un método en la clase base para mostrar información personal.'''

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir_detalles(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def imprimir_detalles(self):
        super().imprimir_detalles()
        print(f"Carrera: {self.carrera}")

class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia

    def imprimir_detalles(self):
        super().imprimir_detalles()
        print(f"Materia: {self.materia}")

        # Ejemplo de uso
e = Estudiante("Elizabeth", 22, "Abogacía")
e.imprimir_detalles()