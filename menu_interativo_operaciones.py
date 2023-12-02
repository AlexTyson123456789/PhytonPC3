
#se ingresa cualquier nuemro
def dividir_numeros(num1, num2):
    if num2 == 0:
        return "No es posible dividir por cero."
    resultado = num1 / num2
    return resultado

def mostrar_menu():
    print("---------------RESPUESTA PARA EL ejemplo_4:------------------")
    print("Menú:")
    print("1. Dividir dos números")
    print("2. Salir")