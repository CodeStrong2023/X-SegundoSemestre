class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f"Los datos a mostrar son los siguientes: {self._nombre} {self._apellido}"

    @property
    def nombre(self):
        print("Etamos utilizando el metodo get")
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        print("Estamos utilizando el metodo set")
        self.nombre = nombre




# Tarea crear tres objetos mas, utilizando los metodos getter and setter
# para modificar, mostrar los cambios con el metodo mostrar detalles

persona2 = Persona2("Mica", "Sanmar", 23)
persona2.nombre = "Micaela"
persona2.apellido = "San Martin"
persona2.edad = 22
print(persona2.nombre)
print(persona2.apellido)
print(persona2.edad)
print(persona2.mostrar_detalles())

persona3 = Persona2("Luci", "Figuer", 21)
persona3.nombre = "Lucia"
persona3.apellido = "Figueroa"
persona3.edad = 25
print(persona3.nombre)
print(persona3.apellido)
print(persona3.edad)
print(persona3.mostar_detalles())

persona4 = Persona2("Facu", "Fun", 26)
persona4.nombre = "Facundo"
persona4.apellido = "Funes"
persona4.edad = 30
print(persona4.nombre)
print(persona4.apellido)
print(persona4.edad)
print(persona4.mostrar_detalles())
