#ej1
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()


#ej2

def saludar_usuario(nombre):
    return f"Hola {nombre}!"


nombre_usuario = input("Ingrese su nombre: ")
saludo = saludar_usuario(nombre_usuario)
print(saludo)


#ej3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

#ej4
import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Ingrese el radio del círculo: "))
print("Área:", calcular_area_circulo(radio))
print("Perímetro:", calcular_perimetro_circulo(radio))


# 5. 
def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("\nIngrese los segundos: "))
print("Equivalente en horas:", segundos_a_horas(segundos))


# 6. 
def tabla_multiplicar(numero):
    print(f"\nTabla del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("\nIngrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)


# 7. 
def operaciones_basicas(a, b):
    return (a + b, a - b, a * b, a / b if b != 0 else "División indefinida")

a = float(input("\nIngrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
suma, resta, multi, div = operaciones_basicas(a, b)
print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {multi}, División: {div}")


# 8. 
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("\nIngrese su peso (kg): "))
altura = float(input("Ingrese su altura (m): "))
print("Su IMC es:", round(calcular_imc(peso, altura), 2))


# 9.
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("\nIngrese la temperatura en Celsius: "))
print("Equivalente en Fahrenheit:", celsius_a_fahrenheit(celsius))


# 10.
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("\nIngrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))
print("El promedio es:", calcular_promedio(a, b, c))
