## PROBLEMA 3
#3. Una tienda de autopartes necesita un programa para catalogar sus productos,
#crear la clase Catálogo y producto, realizar un objeto dentro de un catálogo
#productos el cual debe tener un método para agregar productos y otra para mostrar toda la lista de productos.


#SOLUCION:
 #SE crea las 2 clases producto ... catalogo
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(f"{producto.nombre}: ${producto.precio}")
