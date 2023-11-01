# Ejercicio 3: Funcion Recursiva
# Imprimir numeros de 5 a 1 de manera descente usando funciones recursivas
# Puede ser cualquier valor positivo, por ej, si pasamos el
# valor de 5, debe imprimir:
# 5
# 4
# 3
# 2
# 1
# En caso de ser el numero 3 debe imprimir:
# 3
# 2
# 1
# Si se ingresan numeros negativos no imprime nada

def imprimir_numeros_rcursivos(numeros):
    if numero >= 1: # caso base
        print(numero)
        imprimir_numeros_rcursivos(numero-1) #caso recursivo
    elif numero == 0:
        return
    elif numero <= 0:
        print("Valor ingresado incorrecto...")

imprimir_numeros_rcursivos(5) # Tarea: que el numero lo ingrese al usuario


