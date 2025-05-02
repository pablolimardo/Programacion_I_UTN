"""
Trabajo Práctico 4: Estructuras Repetitivas
"""

import random # Necesario para el ejercicio 5

# --- Ejercicio 1 ---
print("\n--- Trabajo Práctico 4: Estructuras Repetitivas ---")
print("\n\n--- Ejercicio 1 ---")
print("Números enteros del 0 al 100 (inclusive):")
# Usamos un bucle for con range para generar los números de 0 a 100
for numero in range(101): # range(101) va de 0 a 100
    print(numero)

# --- Ejercicio 2 ---
print("\n--- Ejercicio 2 ---")
# Solicitamos un número entero al usuario
try:
    numero_ingresado_str = input("Ingrese un número entero: ")
    numero_ingresado = int(numero_ingresado_str)

    # Manejamos el caso especial del 0
    if numero_ingresado == 0:
        cantidad_digitos = 1
    else:
        # Convertimos a positivo si es negativo para contar dígitos
        numero_abs = abs(numero_ingresado)
        # La cantidad de dígitos es la longitud de su representación como cadena
        cantidad_digitos = len(str(numero_abs))

    print(f"El número {numero_ingresado} tiene {cantidad_digitos} dígito(s).")

except ValueError:
    print("Error: Tenés que ingresar un número entero.")


# --- Ejercicio 3 ---
print("\n--- Ejercicio 3 ---")
try:
    valor1 = int(input("Ingresá el primer valor entero: "))
    valor2 = int(input("Ingresá el segundo valor entero: "))

    # Aseguramos que valor_menor sea el más pequeño y valor_mayor el más grande
    valor_menor = min(valor1, valor2)
    valor_mayor = max(valor1, valor2)

    suma = 0
    # Iteramos desde el siguiente al menor hasta el anterior al mayor
    # range(inicio, fin) no incluye el 'fin', por eso usamos valor_mayor
    for numero in range(valor_menor + 1, valor_mayor):
        suma += numero

    print(f"La suma de los enteros entre {valor_menor} y {valor_mayor} es: {suma}")

except ValueError:
    print("Error: Tenés que ingresar números enteros.")

# --- Ejercicio 4 ---
print("\n--- Ejercicio 4 ---")
suma_acumulada = 0
print("Ingresá números enteros (ingresá 0 para terminar):")
while True: # Bucle infinito que romperemos con break
    try:
        numero_ingresado = int(input("> "))
        if numero_ingresado == 0:
            break # Salimos del bucle si el usuario ingresa 0
        suma_acumulada += numero_ingresado
    except ValueError:
        print("Error: Ingresá solo números enteros.")

print(f"La suma total de los números ingresados es: {suma_acumulada}")

# --- Ejercicio 5 ---
print("\n--- Ejercicio 5 ---")
# Generamos un número aleatorio entre 0 y 9
numero_ganador = random.randint(0, 9)
intentos = 0
adivinado = False

print("Adiviná el número que pensé entre 0 y 9!")

while not adivinado:
    try:
        numero_jugador = int(input("Ingresá tu corazonada: "))
        intentos += 1

        if numero_jugador < 0 or numero_jugador > 9:
             print("Por favor, ingresá un número entre 0 y 9.")
        elif numero_jugador == numero_ganador:
            print(f"Bien ahí! Adivinaste! El número era el {numero_ganador}.")
            adivinado = True
        elif numero_jugador < numero_ganador:
             print("Mmmmm... El número es mayor.")
        else: # numero_jugador > numero_ganador
             print("Nop. El número es menor.")

    except ValueError:
        print(f"Error: Ingresa un número entero válido.")

print(f"Lo lograste en {intentos} intento(s).")

# --- Ejercicio 6 ---
print("\n--- Ejercicio 6 ---")
print("Números pares entre 100 y 0 (inclusive), en orden decreciente:")
# Usamos range con inicio, fin y paso negativo
# range(100, -1, -2) va desde 100 hasta 0 (incluido) decrementando de 2 en 2
for numero in range(100, -1, -2):
    print(numero)

# --- Ejercicio 7 ---
print("\n--- Ejercicio 7 ---")
suma_total_ej7 = 0
numero_limite = -1

# Validamos que el número sea positivo
while numero_limite < 0:
    try:
        numero_limite = int(input("Ingresá un número entero positivo límite: "))
        if numero_limite < 0:
            print("Error: El número tiene que ser positivo.")
    except ValueError:
        print("Error: Tenés que ingresar un número entero.")
        numero_limite = -1 # Reiniciamos por si acaso

# Sumamos los números desde 0 hasta el límite inclusive
for numero in range(numero_limite + 1):
    suma_total_ej7 += numero

print(f"La suma de los números desde 0 hasta {numero_limite} es: {suma_total_ej7}")


# --- Ejercicio 8 ---
print("\n--- Ejercicio 8 ---")
# Constante para la cantidad de números a ingresar
CANTIDAD_NUMEROS_EJ8 = 10 # Cambiado a 10

# Inicializar contadores
contador_pares = 0
contador_impares = 0
contador_positivos = 0
contador_negativos = 0
contador_ceros = 0 # Contamos los ceros explícitamente

print(f"Ingresá {CANTIDAD_NUMEROS_EJ8} números enteros:")

for i in range(CANTIDAD_NUMEROS_EJ8):
    while True: # Bucle para reintentar si la entrada no es válida
        try:
            numero_ingresado = int(input(f"Número {i+1}/{CANTIDAD_NUMEROS_EJ8}: "))
            break # Salir del bucle de reintento si la entrada es válida
        except ValueError:
            print("Error: Ingresá un número entero válido.")

    # Clasificar paridad
    if numero_ingresado % 2 == 0:
        contador_pares += 1
    else:
        contador_impares += 1

    # Clasificar signo
    if numero_ingresado > 0:
        contador_positivos += 1
    elif numero_ingresado < 0:
        contador_negativos += 1
    else:
        contador_ceros += 1

print("\n--- Resultados Ejercicio 8 ---")
print(f"Cantidad de números pares: {contador_pares}")
print(f"Cantidad de números impares: {contador_impares}")
print(f"Cantidad de números positivos: {contador_positivos}")
print(f"Cantidad de números negativos: {contador_negativos}")
print(f"Cantidad de ceros: {contador_ceros}")

# --- Ejercicio 9 ---
print("\n--- Ejercicio 9 ---")
# Constante para la cantidad de números
CANTIDAD_NUMEROS_EJ9 = 5 # Cambiado a 5 para probar
suma_total_ej9 = 0

print(f"Ingresá {CANTIDAD_NUMEROS_EJ9} números enteros para calcular la media:")

for i in range(CANTIDAD_NUMEROS_EJ9):
     while True:
        try:
            numero_ingresado = int(input(f"Número {i+1}/{CANTIDAD_NUMEROS_EJ9}: "))
            suma_total_ej9 += numero_ingresado
            break
        except ValueError:
            print("Error: Ingresá un número entero válido.")

# Calcular la media (promedio)
if CANTIDAD_NUMEROS_EJ9 > 0:
    media = suma_total_ej9 / CANTIDAD_NUMEROS_EJ9
    print(f"\nLa suma total es: {suma_total_ej9}")
    print(f"La media de los {CANTIDAD_NUMEROS_EJ9} números es: {media:.2f}") # :.2f formatea a 2 decimales
else:
    print("No se ingresaron números para calcular la media.")


# --- Ejercicio 10 ---
print("\n--- Ejercicio 10 ---")
numero_invertido_str = ""
try:
    numero_original_str = input("Ingresá un número entero para invertir sus dígitos: ")
    # Validar que sea un número (puede ser negativo)
    numero_original = int(numero_original_str)

    # Manejar el signo negativo por separado
    signo = ""
    if numero_original < 0:
        signo = "-"
        numero_original_str = numero_original_str[1:] # Quitar el signo '-' para invertir

    # Invertir la cadena de dígitos usando slicing [::-1]
    numero_invertido_str = signo + numero_original_str[::-1]

    print(f"El número original es: {numero_original}")
    print(f"El número con dígitos invertidos es: {numero_invertido_str}")

except ValueError:
    print("Error: Tenés que ingresar un número entero.")

print("\n--- Fin del Trabajo Práctico ---")