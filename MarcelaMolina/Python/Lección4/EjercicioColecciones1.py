#Ejercicio 1: Eliminar duplicados de una lista
#Escriba un programa donde tenga una lista y que, a continuación
#elimine los elementos repetidos, por último mostrar la lista

#Creamos la lista
lista = [1, 2, 3, "Ariel", 7, 7, 9, "Osvaldo", 8, 2, "Ariel", "Osvaldo"]
#conjunto = set(lista)
#lista = list(conjunto)
lista = list(set(lista)) #Convertimos el conjunto a una lista
print(lista)

