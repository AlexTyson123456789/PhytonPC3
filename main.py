# 1.En el archivo main.py crear la condición __name__==’__main__’ ejecutar los demás problemas.

#SOLUCION:
#en primer lugar se importa los ejercicios creados-- en este caso "ejemplos".
from ejemplo_2 import CIRCULO
from ejemplo_3 import Catalogo, Producto
from ejemplo_5 import Producto_5
from ejemplo_7 import Phone
from ejemplo_8 import Persona

# ahora se realiza a crear el archivo "main.py"
if __name__ == '__main__':

    # Problema 2
    mi_circulo = CIRCULO(3)  #SE TOMA COMO EJEMPLO "RADIO=3"
    area_del_circulo = mi_circulo.calcular_area()
    print("---------------RESPUESTA PARA EL ejemplo_2:------------------")
    print(f"El área del círculo con radio {mi_circulo.radio} es: {area_del_circulo}")

    # Problema 3
    catalogo = Catalogo()
    producto1 = Producto("Aceite de Motor", 20.99)
    producto2 = Producto("Filtro de Aire", 5.99)

    catalogo.agregar_producto(producto1)
    catalogo.agregar_producto(producto2)

    print("---------------RESPUESTA PARA EL ejemplo_3:------------------")
    print("Lista de productos en el catálogo:")
    catalogo.mostrar_productos()

    # Problema 4

    from menu_interativo_operaciones import mostrar_menu, dividir_numeros

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultado_division = dividir_numeros(num1, num2)
            print(f"El resultado de la división es: {resultado_division}")
        elif opcion == "2":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")

    # Problema 5
    
    Ejemplo_cualquier_producto = Producto_5("Ejemplo_cualquier_producto", "PERU-0021-2020")
    print("---------------RESPUESTA PARA EL ejemplo_5:------------------")
    print(Ejemplo_cualquier_producto)

    #Problema 6

    #from menu_interativo_operaciones import menu_operaciones #para "ejemplo_4"
    #funcioness de manejo d e errores.
    #try:
    #    menu_operaciones()
    #except Exception as e:
    #    print(f"Error: {e}")
    #else:
    #    import os
    #    print(f"Directorio de trabajo: {os.getcwd()}")
    #finally:
    #    print("Proceso terminado")


    #Problema 7

    # Ejemplo de uso del nuevo método y atributos
    my_phone = Phone(brand="Apple", model="iPhone 13")
    my_phone.set_color("Blue")
    my_phone.set_price(999.99)
    my_phone.set_storage_capacity("128GB")
        
    # Llamar al nuevo método
    my_phone.display_info()

    # Imprimir el nuevo atributo
    print(f"Storage Capacity: {my_phone.storage_capacity}")


    #Problema 6
    
    #DATOS DE LA PERSONA
    nueva_persona = Persona()
    nueva_persona.mostrar_informacion()