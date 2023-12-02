# 1.En el archivo main.py crear la condición __name__==’__main__’ ejecutar los demás problemas.

#SOLUCION:
#en primer lugar se importa los ejercicios creados-- en este caso "ejemplos".
from ejemplo_2 import CIRCULO
from ejemplo_3 import Catalogo, Producto


# ahora se realiza a crear el archivo "main.py"
if __name__ == '__main__':

    # Problema 2
    mi_circulo = CIRCULO(3)  #SE TOMA COMO EJEMPLO "RADIO=3"
    area_del_circulo = mi_circulo.calcular_area()
    print("RESPUESTA PARA EL ejemplo_2::")
    print(f"El área del círculo con radio {mi_circulo.radio} es: {area_del_circulo}")

    # Problema 3
    catalogo = Catalogo()
    producto1 = Producto("Aceite de Motor", 20.99)
    producto2 = Producto("Filtro de Aire", 5.99)

    catalogo.agregar_producto(producto1)
    catalogo.agregar_producto(producto2)

    print("RESPUESTA PARA EL ejemplo_3:")
    print("Lista de productos en el catálogo:")
    catalogo.mostrar_productos()


