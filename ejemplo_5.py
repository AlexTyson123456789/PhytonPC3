#PRBLEMA 5.
#Programa que tenga una clase Producto el cual solo tiene los atributo de nombre y código.
#el código tiene la siguiente estructura ‘PAIS-LOTE-AÑO’ ejemplo : ‘PERU-0001-2023’ crear un método que permita imprimir el objeto de forma literal (__str__) y
#que me permita identificar el país de origen , el numero de lote .

#SOLUCION:
# producto.py
class Producto_5:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def __str__(self):
        pais, lote, anio = self.codigo.split('-')
        return f'Nombre: {self.nombre}, Código: {self.codigo}, País: {pais}, Lote: {lote}, Año: {anio}'





