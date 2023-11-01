# Ejercicio 2: Operaciones de conjuntos con listas
# Escriba un programa que tenga 2 listas y que a continuacion
# cree las siguientes listas (en las que no deben haber repeticion)
# 1 Lista de palabras que aparecen en las listas
# 2 Lista de palabras que aparecen en la primera lista, pero no en la segunta
# 3 Lista de palabras que aparecen en la segunda lista, pero no en la primera
# 4 Lista de palabras que aparecen en ambas listas

lista1 = [1, 2, 3, 4, 5, 4, 3, 2, 1, 5]
lista2 = [4, 5, 6, 7, 8, 4, 5, 7, 7, 8]

# Eliminar los elementos repetidos de ambas listas con conjuntos
conjunto1 = set(lista1)
conjunto2 = set(lista2)

union = lista(conjunto1 | conjunto2) # Unimos los dos conjuntos
solo1 = lista(conjunto1 - conjunto2) # Solo muestra el conjunto1
union = lista(conjunto2 - conjunto1) # Solo muestra el conjunto2
interseccion = list(conjunto1 & conjunto2) # Mostramos elementos que coinciden en ambas listas

print(f"Lista de palabras que aparecen en las listas: {union}")
print(f"Lista de palabras que aparecen en las lista, pero no en la segunda: {solo1}")
print(f"Lista de palabras que aparecen en las lista, pero no en la primera: {solo2}")
print(f"Lista de palabras que aparecen en ambas listas: {interseccion}")
