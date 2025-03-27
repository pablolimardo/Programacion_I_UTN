# 1- Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola Mundo")

# 2- Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre = input("Ingresá tu nombre:  ")
print(f"Hola {nombre}")

# 3- Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre = input("Ingresá tu nombre:  ")
apellido = input("Ingresá tu apellido:  ")
edad = input("Ingresá tu edad:  ")
lugar = input("Ingresá tu lugar de residencia:  ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}.")

# 4- Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

radio = float(input("Ingresá el radio de un círculo:  "))

area = 3.14 * (radio ** 2)
perimetro = 2 * 3.14 * radio

print(f"El área del círculo es: {area}.")
print(f"El perímetro del círculo es: {perimetro}.")

# 5- Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

minutos = int(input("Ingresá una cantidad de segundos:  "))

horas = minutos / 60

print(f"Son {horas} horas")

# 6- Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

numeroAMultiplicar = int(input("Ingresá un número:  "))

for i in range(1, 11):
    print(f"**** Tabla de multiplicar del {numeroAMultiplicar} ****")
    print(f"{numeroAMultiplicar} x {i} = {numeroAMultiplicar * i}")

# 4- Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

primerNumero = int(input("Ingresá un número:  "))
segundoNumero = int(input("Ingresá otro número:  "))

suma = primerNumero + segundoNumero
division = primerNumero / segundoNumero
multiplicacion = primerNumero * segundoNumero
resta = primerNumero - segundoNumero

print(f"La suma es: {suma}")
print(f"La resta es: {resta}")
print(f"La multiplicación es: {multiplicacion}")
print(f"La división es: {division}")

# 8- Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo: peso / altura²

peso = float(input("Ingresá tu peso:  "))
altura = float(input("Ingresá tu altura:  "))

imc = peso / (altura ** 2)

print(f"Tu índice de masa corporal es: {imc}.")

# 9- Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: F = (C * 9/5) + 32

celsius = float(input("Ingresá una temperatura en grados Celsius:  "))

fahrenheit = (celsius * 9/5) + 32

print(f"La temperatura en grados Fahrenheit es: {fahrenheit}º.")

# 10- Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
numeroUno = float(input("Ingresá un número:  "))
numeroDos = float(input("Ingresá otro número:  "))
numeroTres = float(input("Ingresá un número más:  "))

promedio = (numeroUno + numeroDos + numeroTres) / 3

print(f"El promedio de los números ingresados es: {promedio}.")





