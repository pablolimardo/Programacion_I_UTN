# Soluciones para el Trabajo Práctico 5: Listas

print("--- Ejercicio 1 ---")
# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4.
multiplos_de_cuatro = list(range(4, 101, 4))
print("Múltiplos de 4 del 1 al 100:", multiplos_de_cuatro)

print("\n--- Ejercicio 2 ---")
# 2) Crear una lista con cinco elementos y mostrar el penúltimo.
mis_gustos = ["cocinar", "fotografía", "videojuegos", "viajar", "música"]
print("Lista de gustos:", mis_gustos)
# Usando índice negativo para obtener el penúltimo
print("Penúltimo elemento:", mis_gustos[-2])

print("\n--- Ejercicio 3 ---")
# 3) Crear una lista vacía, agregar tres palabras con append e imprimir.
palabras = [] # Lista vacía
palabras.append("Ejercicio")
palabras.append("número")
palabras.append("tres")
print("Lista de palabras:", palabras)

print("\n--- Ejercicio 4 ---")
# 4) Reemplazar el segundo y último valor de la lista "animales".
animales = ["perro", "gato", "conejo", "pez"]
print("Lista original de animales:", animales)
animales[1] = "loro"  # Reemplaza el segundo elemento (índice 1)
animales[-1] = "oso" # Reemplaza el último elemento (índice -1)
print("Lista modificada de animales:", animales)

print("\n--- Ejercicio 5 ---")
# 5) Analizar el programa y explicar 

""" El programa elimina el número más grande de la lista
    e imprime la lista actualizada.
"""

print("\n--- Ejercicio 6 ---")
# 6) Crear lista del 10 al 30 con saltos de 5 y mostrar los dos primeros.
numeros_saltos = list(range(10, 31, 5)) # 31 para incluir el 30
print("Lista con saltos:", numeros_saltos)
# Usando slicing para obtener los dos primeros
dos_primeros = numeros_saltos[:2]
print("Los dos primeros elementos:", dos_primeros)

print("\n--- Ejercicio 7 ---")
# 7) Reemplazar los dos valores centrales de la lista "autos".
autos = ["sedan", "polo", "suran", "gol"]
print("Lista original de autos:", autos)
# Reemplaza elementos en índice 1 y 2 usando slicing
autos[1:3] = ["Renault 4", "Corsa"]
print("Lista modificada de autos:", autos)

print("\n--- Ejercicio 8 ---")
# 8) Crear lista "dobles" y agregar el doble de 5, 10 y 15 usando append.
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print("Lista de dobles:", dobles)

print("\n--- Ejercicio 9 ---")
# 9) Modificar la lista anidada "compras".
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
print("Lista de compras original:", compras)

# a) Agregar "jugo" a la lista del tercer cliente (índice 2)
compras[2].append("jugo")
print("a) Después de agregar 'jugo':", compras)

# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente (índice 1)
    # Encuentra el índice de "fideos" en la sublista compras[1]
indice_fideos = compras[1].index("fideos")
compras[1][indice_fideos] = "tallarines"
print("b) Después de reemplazar 'fideos':", compras)

# c) Eliminar "pan" de la lista del primer cliente (índice 0)
compras[0].remove("pan")
print("c) Después de eliminar 'pan':", compras)

# d) Imprimir la lista resultante final (ya se hizo en los pasos anteriores)
print("d) Lista de compras final:", compras)

print("\n--- Ejercicio 10 ---")
# 10) Elaborar la lista anidada "lista_anidada".
lista_anidada = [15,True,[25.5, 57.9, 30.6],False]
print("Lista anidada creada:", lista_anidada)

