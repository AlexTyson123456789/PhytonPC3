# PROBLEMA 2
#Definir una clase llamada “CIRCULO” la cual contenga un atributo inicializador
#radio. La clase “CIRCULO” debe tener un método que puede calcular el área en utilizando el atributo radio.

#SOLUCION:
import math

class CIRCULO:  #se define la clase "CIRCULO"
    def __init__(self, radio):  #inijcializa -- radio
        self.radio = radio

    def calcular_area(self):    #calcula el area de un circulo.
        return math.pi * (self.radio ** 2)

