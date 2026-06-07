#Ejercicio 5
'''Crea una clase Producto con propiedades nombre, precio y fecha de vencimiento.
Deriva clases como ProductoAlimenticio y ProductoElectrónico, y añade métodos
para aplicar descuentos basados en la fecha actual y en ciertas condiciones.'''

class Producto:
    def __init__(self, nombre, precio, fecha_vencimiento):
        self.nombre = nombre
        self.precio = precio
        self.fecha_vencimiento = fecha_vencimiento

    def imprimir_detalles(self):
        print(f"Producto: {self.nombre}")
        print(f"Precio: ${self.precio}")
        print(f"Vencimiento: {self.fecha_vencimiento}")

class ProductoAlimenticio(Producto):
    def aplicar_descuento(self):
        return self.precio * 0.63

    def imprimir_detalles(self):
        super().imprimir_detalles()
        print(f"Precio con descuento: ${self.aplicar_descuento():.2f}")

class ProductoElectronico(Producto):
    def aplicar_descuento(self):
        return self.precio * 0.84

    def imprimir_detalles(self):
        super().imprimir_detalles()
        print(f"Precio con descuento: ${self.aplicar_descuento():.2f}")


        # Ejemplo de uso
p = ProductoAlimenticio("Oreoa", 1250, "11/06/2026")
p.imprimir_detalles()