seleccionArgentina = {
    10: {"Nombre": "Lionel Messi", "Edad": 35, "Altura": 1.70, "Precio": "50 Millones", "Posicion": "Extremo Derecho"},
    11: {"Nombre": "Angel Di Maria", "Edad": 34, "Altura": 1.80, "Precio": "12 Millones", "Posicion": "Extremo Derecho"},
    24: {"Nombre": "Paulo Dybala", "Edad": 28, "Altura": 1.77, "Precio": "35 Millones", "Posicion": "Media Punta"},
    19: {"Nombre": "Nicolas Otamendi", "Edad": 34, "Altura": 1.83, "Precio": "3.5 Millones", "Posicion": "Defensa Central"},
    1:  {"Nombre": "Franco Armani", "Edad": 35, "Altura": 1.89, "Precio": "3.5 Millones", "Posicion": "Portero"},
    23: {"Nombre": "Emiliano Martinez", "Edad": 31, "Altura": 1.95, "Precio": "30 Millones", "Posicion": "Portero"},
    13: {"Nombre": "Cristian Romero", "Edad": 25, "Altura": 1.85, "Precio": "26 Millones", "Posicion": "Defensa"},
    25: {"Nombre": "Lisandro Martinez", "Edad": 25, "Altura": 1.75, "Precio": "48 Millones", "Posicion": "Defensa"},
    9:  {"Nombre": "Julian Alvarez", "Edad": 23, "Altura": 1.70, "Precio": "21 Millones", "Posicion": "Centro"}

}
for llave, valor in seleccionArgentina.items():
    print(llave, valor)

print("Tenemos cargados en el diccionario la cantidad de jugadores: ", end= " ")
print(len(seleccionArgentina))
