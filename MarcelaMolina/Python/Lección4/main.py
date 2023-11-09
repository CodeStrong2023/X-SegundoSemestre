#lista= Ariel, Osvaldo,Natalia
#dentro de una lista puede haber nombres u otro tipo de datos (txt, numéricos,lógicos), a cada elemento
#de la lista se le asigna un índice. Teniendo en cuenta cada índice se va a
#poder ver, modificar u eliminar los elementos.

nombres = ["Naty", "Osvaldo", "Lily", "Ariel"]
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[2])
#Para ver el último elemento de la lista sin saber qué número se le asigna
print(nombres[-1])
print (nombres[-2])
#Recuperar un rango de la lista
print(nombres[0:3]) #Solo muestra índice 0,1,2
print(nombres [1: ]) #Muestra desde el índice indicado hasta el final
#MOdificamos un valor
nombres[2] = "Liliana"
nombres[0] = "Natalia"
print(nombres)
#Iterar una lista
for nombres in nombres:
    print(nombres)
else:
    print("Se acabaron los elementos de la lista")

#Preguntar cuantos elementos tiene una lista
print(len(nombres))

#Agregamos un elemento a la lista
nombres.append("Marcelo")
print(nombres) 

#Agregar un elemento con un índice específico
nombres.insert(1, "Analía")
print(nombres)
nombres.insert(3, "Débora")
print(nombres)

#Elimminar un elemento
nombres.remove("Analía")
print(nombres)

#Eliminar el último elemento
nombres.pop()
print(nombres)

#Eliminar un índice específico
del nombres[2]


#Eliminar todos los elementos
nombres.clear()
print(nombres)

#Eliminar la lista
del(nombres)


#TUPLAS


#Definimos una tupla
cocina =("Cuchara","Cuchillo","Tenedor")
print(len(cocina))
print(cocina[0]) #Muestra el primer elemento

print(cocina[-1]) #Muestra el último elemento

#Acceder a un rango
print(cocina[0:2]) #muestra el elemento 0 y 1.

#Recorrer los elementos de la tupla
for cocina in cocina:#"/n
    print(cocina, end=" ") #end para eliminar los saltos de línea

cocinalista = list(cocina)
cocinalista[0] = "Plato"
cocina = tuple(cocinalista)
print("\n", cocina)

#Eliminar una tupla
del cocina



#Tipo set
planetas = {"Marte" , "Júpiter" , "Venus"} 
print(planetas)
print(len(planetas)) #Muestra el largo del set

#Revisar si un elemento existe dentro del set
print("Marte" in planetas) 

#Agregar un elemento
planetas.add("Tierra")
print(planetas)

#Eliminar un elemento, puede arrojar error si el elem no existe
planetas.remove("Júpiter")
print(planetas)

planetas.discard("Tierra")
print(planetas)

#Limpiar el set
planetas.clear()
print(planetas)

#Eliminar el set
del planetas




#LISTAS
#Concatenar listas
lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = lista1+lista2
print(lista3)

#Agregar elementos a una lista
lista3.extend([7, 8, 9])
print(lista3)

#Ubicar en qué indice esta el valor ingresado
print(lista3.index(5)) #Cuando da error es porque no está el índice

#Saber si hay elementos repetidos y los cuenta
print(lista3.count(1)) 

#Para poner al revés una lista
lista3.reverse()
print(lista3)

#Para que una lista se multiplique repitiendo sus elementos 
lista3 = lista3*2
print(lista3)

#Métodos de ordenamiento, en python es una función
lista3.sort() #ordena los elem ascendentemente
print(lista3)
lista3.sort(reverse=True) #ordena descendentemente
print(lista3)


#Repaso de tuplas
tupla = (4,"hola",6.87,[1,2,78],4,"Hola")#puede tener dif datos dentro
print(tupla)

print(4 in tupla) #Acción booleana, su respuesta es de tipo booleana


#Repaso de set o conjunto
#para definir un conjunto
conjunto2 = set()
conjunto1 = {'bye', }
conjunto2.add(7)
conjunto2.add("Hola")
print(conjunto2)
conjunto1.add("hola")
print(conjunto1)
print(3 not in conjunto1) #Preg si el número 3 no está en el conj1

#Como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto2) #Nos delvuelve como respuesta un booleano

#Operaciones en conjuntos
conjunto3 = conjunto1 | conjunto2 #La línea une los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1&conjunto2 #Elemento que tienen en común
print(conjunto3)

conjunto3 = conjunto1 - conjunto2 #asigna el valor que está en el conj1 y no en el conj2
print(conjunto3)
conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 #elementos que no comparten
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3)) #Si un conj es un subconj dentro de otro
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto2))

#como saber si ambos conjuntos son disconexos , si no comparten elementos en común
print(conjunto1.isdisjoint(conjunto2)) #no hay cosas en común

#Convertir un conjunto totalmente en inmutable
conjunto1 = frozenset
#No se puede agregar, modificar ni eliminar elementos



#Pilas usando listas
pila = [1, 2, 3]

#Agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

#Sacamos elementos desde el final
elementoBorrado = pila.pop() #Quita el último elemento y lo guarda en la variable
print(f'Sacamos el elemento:{elementoBorrado}')
print(f'La pila ahora quedó así: {pila}')

#Cola con listas
#Estructura de datos de tipo fifo(first input/first output)
cola = ['Ariel','Osvaldo','Liliana','Pilar']

#Agregamos elementos al final de la cola#
cola.append('Natalia')
cola.append('José')
print(cola)

#Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

