# Ejercicio 1: Eliminar duplicados de una lista
# Escriba un programa donde tenga una lista y que a continuacion
# elimine los elementos repetidos, por ultimo mostrar la lista.

#Creamos una lista
lista = [1, 2, 3, "Mica", 7, 7, 3, "Antonella", 1, "Mica", 2, "Antonella"]
# conjunto = set(lista) # Convertimos la lista a un conjunto de tipo set
# lista = lista(conjunto) # Convertimos el conjunto a una lista
lista = list(set(lista)) # La conversacion hecha en una sola linea de codigo (eficiente)
print(lista)
