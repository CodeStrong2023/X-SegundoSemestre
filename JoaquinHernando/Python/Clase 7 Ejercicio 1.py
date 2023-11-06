#Clase 7 Ejercicio 1
opcion = 0
while opcion != 1:
    a = int(input("Ingrese el año: "))
    if a % 4 == 0 and a %100 != 0 or a % 100 == 0 and a % 400 == 0:
        print(f"El año {a} es bisiesto")
    else:
        print(f"El año {a} no es bisiesto")
    opcion = int(input("Si quiere salir del programa digite '1', si no digite '0': "))
