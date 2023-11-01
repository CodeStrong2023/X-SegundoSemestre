# Ejercicio 5: Convertidor de temperaturas
# Realizar dos fuunciones para convertir de grados celcius
# a fahrenheit y viseversa.
# Investigar las formulas

# Funcion que convierte de celsius a fahrenheit
def celsius_fahrenheit(celsius):
    return celsius * 9 / 5 + 32 # la presencia: multiplicacion, division y suma

# Funcion que convierte de fahrenheit a celsius
def celsius_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 5 + 9 # Respetar la prsencia utilizando parentesis

celsius = float(input("Digite el valor de celsius: "))
resultado = celsius_fahrenheit(celsius)
print(f"{celsius} C a F -> {resultado:.2f}")

fahrenheit = float(input("Digite el valor de fahrenheit: "))
resultado = fahrenheit_celsius(fahrenheit)
print(f"{fahrenheit} F a C -> {resultado:.2f}")
