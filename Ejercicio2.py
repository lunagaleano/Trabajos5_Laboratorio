#Ejercicio 1
'''Crea una clase Empleado con propiedades nombre, salario y cargo.
Deriva clases como Gerente y EmpleadoTemporal, añadiendo un método
en cada una que calcule el aumento de salario basado en ciertos criterios.'''

class Empleado:
    def __init__(self, nombre, salario, cargo):
        self.nombre = nombre
        self.salario = salario
        self.cargo = cargo

    def imprimir_detalles(self):
        print(f"Nombre: {self.nombre}")
        print(f"Cargo: {self.cargo}")
        print(f"Salario: ${self.salario:.2f}")


class Gerente(Empleado):
    def __init__(self, nombre, salario):
        super().__init__(nombre, salario, "Gerente")

    def calcular_aumento(self):
        return self.salario * 0.50

    def imprimir_detalles(self):
        super().imprimir_detalles()
        print(f"Aumento: ${self.calcular_aumento():.2f}")

class EmpleadoTemporal(Empleado):
    def __init__(self, nombre, salario):
        super().__init__(nombre, salario, "Empleado Temporal")

    def calcular_aumento(self):
        return self.salario * 0.30

    def imprimir_detalles(self):
        super().imprimir_detalles()
        print(f"Aumento: ${self.calcular_aumento():.2f}")

# Ejemplo de uso
if __name__ == "__main__":
    g = Gerente("Javier", 5700)
    g.imprimir_detalles()
    print()
    e = EmpleadoTemporal("Ana Maria", 3400)
    e.imprimir_detalles()