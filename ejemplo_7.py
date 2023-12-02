#PROBLEMA 7
# Según el ejercicio realizado con la clase Phone implementar un método nuevo
#(esto incluye agregar atributos)


#SOLUCION:
# SE agrega un nuevo método y atributos a la clase Phone

class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.color = ""
        self.price = 0

    def set_color(self, color):
        self.color = color

    def set_price(self, price):
        self.price = price

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Price: {self.price}")

    # Método nuevo que agrega atributos
    def set_storage_capacity(self, storage):
        self.storage_capacity = storage

