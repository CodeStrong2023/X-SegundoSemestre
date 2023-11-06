#Ejercicio 1
lista = [1, 2, 3, "Ariel", 7, 7, 3, "Alberto", 5, "Ariel", "Alberto"]
conjunto = set(lista)
lista = list(conjunto)
print(lista)

#Ejercicio 2
lista1 = [1, 2, 3, 4, 5, 4, 3, 2, 2, 1, 5]
lista2 = [4, 5, 6, 7, 8, 4, 5, 6, 7, 7, 8]
conjunto1 = set(lista1)
conjunto2 = set(lista2)

union = list(conjunto1 | conjunto2)
solo1 = list(conjunto1 - conjunto2)
solo2 = list(conjunto2 - conjunto1)
interseccion = list(conjunto1 & conjunto2)
print("Lista de palabras que aparecen en las listas: ", union)
print("Lista de palabras que aparecen en la primera lista, pero no en la segunda: ", solo1)
print("Lista de palabras que aparecen en la segunda lista, pero no en la primera: ", solo2)
print("Lista de palabras que aparecen en ambas listas: ", interseccion)

#Ejercicio 3
