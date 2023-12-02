#PROBLEMA 8
# Crear una clase Persona y que para instanciar los datos sean datos ingresados desde teclado..

class Persona:
    #se ingreas los datos de la persona.
    def __init__(self):
        self.nombre = input("Ingrese el nombre: ")
        self.edad = int(input("Ingrese la edad: "))
        self.genero = input("Ingrese el género: ")

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Género: {self.genero}")