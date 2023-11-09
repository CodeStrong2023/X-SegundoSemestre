# Ejercicio 3: Agregar personajes a una lista
# Escriba un programa donde cree una lista con los siguientes personajes del señor de los anillos
# Nombre: Aragon
# Clase: Guerrero
# Raza: Dúnadan del norte

# Nombre: Gandalf
# Clase: Mago
# Raza: Istar

# Nombre: Legolas
# Clase: Arquero
# Raza: Elfo Sindar

personajes = [] #Creamos una lista vacía
#Creamos diccionarios
P = {'Nombre': 'Aragon', 'Clase': 'Guerrero','Raza':'Dúnadan del norte'}
personajes.append(P) # Agregamos a una lista un personaje
P = {'Nombre':'Gandalf', 'Clase':'Mago','Raza':'Istar'}
personajes.append(P)
P = {'Nombre':'Legolas', 'Clase':'Arquero','Raza':'Elfo Sindar'}
personajes.append(P)
print(personajes)


