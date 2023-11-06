seleccionArgentina = {
    10: {"Nombre": "Lionel Messi", "Edad": 35, "Altura": 1.70, "Precio": "50 Millones", "Posicion": "Extremo Derecho"},
    11: {"Nombre": "Angel Di Maria", "Edad": 34, "Altura": 1.80, "Precio": "12 Millones", "Posicion": "Extremo Derecho"},
    24: {"Nombre": "Paulo Dybala", "Edad": 28, "Altura": 1.77, "Precio": "35 Millones", "Posicion": "Media Punta"},
    19: {"Nombre": "Nicolas Otamendi", "Edad": 34, "Altura": 1.83, "Precio": "3.5 Millones", "Posicion": "Defensa Central"},
    1: {"Nombre": "Franco Armani", "Edad": 35, "Altura": 1.89, "Precio": "3.5 Millones", "Posicion": "Arquero"},
    5: {"Nombre": "Leandro Paredes", "Edad": 29, "Altura": 1.82, "Precio": "4.5 Millones", "Posicion": "Mediocampista"},
    23: {"Nombre": "Damian Martinez", "Edad": 31, "Altura": 1.95, "Precio": "28 Millones", "Posicion": "Arquero"},
    24: {"Nombre": "Enzo Fernandez", "Edad": 22, "Altura": 1.78, "Precio": "121 Millones", "Posicion": "Mediocampista"},
    20: {"Nombre": "Alexis Mac Allister", "Edad": 24, "Altura": 1.76, "Precio": "40 Millones", "Posicion": "Mediocampista"},
    7: {"Nombre": "Rodrigo De Paul", "Edad": 29, "Altura": 1.80, "Precio": "37 Millones", "Posicion": "Mediocampista"}
}

for llave, valor in seleccionArgentina.items():
    print(llave, valor)
print("Tenemos cargados en el diccionario la cantidad de jugadores:", end="")
print(len(seleccionArgentina))
pila = [1, 2, 3]