# Trabajo Práctico N°11: Aplicación de la Recursividad

**Alumno:** Pablo Limardo
**Materia:** Programación I
**Carrera:** Tecnicatura Universitaria en Programación
**Universidad:** UTN

---

## Ejercicio 1: Factorial de un número

```python
def factorial(n):
  """
  Calcula el factorial de un número n de forma recursiva.
  El caso base es cuando n es 0 o 1, cuyo factorial es 1.
  Para otros números, el factorial es n multiplicado por el factorial de n-1.
  """
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n - 1)

# ---- Programa Principal ----
try:
  numero_limite = int(input("Ingresá un número entero para calcular factoriales: "))
  if numero_limite < 0:
    print("Por favor, ingresá un número no negativo.")
  else:
    print(f"\nCalculando los factoriales desde 1 hasta {numero_limite}:")
    for i in range(1, numero_limite + 1):
      resultado_factorial = factorial(i)
      print(f"El factorial de {i} es: {resultado_factorial}")
except ValueError:
  print("Entrada no válida. Por favor, ingresá un número entero.")
```

---

## Ejercicio 2: Sucesión de Fibonacci

```python
def fibonacci(pos):
  """
  Calcula el número de Fibonacci en una posición 'pos' dada de forma recursiva.
  Casos base:
  - Si la posición es 0, devuelve 0.
  - Si la posición es 1, devuelve 1.
  El paso recursivo es la suma de los dos números de Fibonacci anteriores.
  """
  if pos == 0:
    return 0
  elif pos == 1:
    return 1
  else:
    return fibonacci(pos - 1) + fibonacci(pos - 2)

# ---- Programa Principal ----
try:
  posicion_limite = int(input("Ingresá una posición para la serie de Fibonacci: "))
  if posicion_limite < 0:
    print("Por favor, ingresá una posición no negativa.")
  else:
    print(f"\nLa serie de Fibonacci hasta la posición {posicion_limite} es:")
    for i in range(posicion_limite + 1):
      print(fibonacci(i), end=" ")
    print()
except ValueError:
  print("Entrada no válida. Por favor, ingrese un número entero.")
```

---

## Ejercicio 3: Potencia de un número

```python
def potencia(base, exponente):
  """
  Calcula la potencia de una base elevada a un exponente de forma recursiva.
  Caso base: Cualquier número elevado a 0 es 1.
  Paso recursivo: base * potencia(base, exponente - 1).
  """
  if exponente == 0:
    return 1
  else:
    return base * potencia(base, exponente - 1)

# ---- Programa Principal ----
try:
  base_num = int(input("Ingresá el número base: "))
  exponente_num = int(input("Ingresá el exponente (entero no negativo): "))

  if exponente_num < 0:
    print("El exponente debe ser un número no negativo.")
  else:
    resultado_potencia = potencia(base_num, exponente_num)
    print(f"\n{base_num} elevado a la {exponente_num} es: {resultado_potencia}")
except ValueError:
  print("Entrada no válida. Por favor, ingresá números enteros.")
```

---

## Ejercicio 4: Conversión a Binario

```python
def decimal_a_binario(n):
  """
  Convierte un número decimal 'n' a su representación en binario como string.
  Caso base: Si n es 0, su binario es "0". Si es 1, es "1".
  Paso recursivo: Se llama a la función con n // 2 y se concatena el resto (n % 2).
  """
  if n <= 1:
    return str(n)
  else:
    return decimal_a_binario(n // 2) + str(n % 2)

# ---- Programa Principal ----
try:
  numero_decimal = int(input("Ingresá un número entero positivo para convertir a binario: "))
  if numero_decimal < 0:
    print("Por favor, ingresá un número positivo.")
  else:
    resultado_binario = decimal_a_binario(numero_decimal)
    print(f"\nEl número {numero_decimal} en binario es: {resultado_binario}")
except ValueError:
  print("Entrada no válida. Por favor, ingresá un número entero.")
```

---

## Ejercicio 5: Palíndromos

```python
def es_palindromo(palabra):
  """
  Verifica si una palabra es un palíndromo de forma recursiva.
  Caso base: Si la palabra tiene 0 o 1 caracter, es un palíndromo.
  Paso recursivo: Compara el primer y último caracter. Si son iguales,
  llama a la función con la sub-cadena sin esos dos caracteres.
  """
  palabra = palabra.lower()
  
  if len(palabra) <= 1:
    return True
  else:
    if palabra[0] == palabra[-1]:
      return es_palindromo(palabra[1:-1])
    else:
      return False

# ---- Programa Principal ----
texto = input("Ingresá una palabra para verificar si es un palíndromo: ")
if es_palindromo(texto):
  print(f'La palabra "{texto}" SÍ es un palíndromo.')
else:
  print(f'La palabra "{texto}" NO es un palíndromo.')
```

---

## Ejercicio 6: Suma de Dígitos

```python
def suma_digitos(n):
  """
  Suma los dígitos de un número entero positivo 'n' de forma recursiva.
  Caso base: Si n es menor que 10, es un solo dígito, por lo que se devuelve a sí mismo.
  Paso recursivo: Suma el último dígito (n % 10) con la suma de los dígitos
  restantes (obtenidos con n // 10).
  """
  if n < 10:
    return n
  else:
    return (n % 10) + suma_digitos(n // 10)

# ---- Programa Principal ----
try:
  numero_entero = int(input("Ingrese un número entero positivo para sumar sus dígitos: "))
  if numero_entero < 0:
    print("El número debe ser positivo.")
  else:
    resultado_suma = suma_digitos(numero_entero)
    print(f"\nLa suma de los dígitos de {numero_entero} es: {resultado_suma}")
except ValueError:
  print("Entrada no válida. Por favor, ingrese un número entero.")
```

---

## Ejercicio 7: Pirámide de Bloques

```python
def contar_bloques(n):
  """
  Calcula el número total de bloques en una pirámide donde la base tiene 'n' bloques.
  Caso base: Si la base tiene 1 bloque (la cima), el total es 1.
  Paso recursivo: Suma los bloques de la base actual 'n' al total de bloques
  de una pirámide con base n-1.
  """
  if n <= 0:
    return 0
  if n == 1:
    return 1
  else:
    return n + contar_bloques(n - 1)

# ---- Programa Principal ----
try:
  base_piramide = int(input("Ingresá el número de bloques en la base de la pirámide: "))
  total = contar_bloques(base_piramide)
  print(f"\nPara una base de {base_piramide} bloques, el total de bloques en la pirámide es: {total}")
except ValueError:
  print("Entrada no válida. Por favor, ingresá un número entero.")
```

---

## Ejercicio 8: Contar un Dígito Específico

```python
def contar_digito(numero, digito):
  """
  Cuenta cuántas veces aparece un 'digito' en un 'numero' de forma recursiva.
  Caso base: Si el número tiene un solo dígito, se compara con el dígito buscado.
  Paso recursivo: Comprueba si el último dígito del número es el que buscamos.
  Después, suma ese resultado (1 si coincide, 0 si no) a la llamada recursiva con el resto del número (numero // 10).
  """
  if numero == 0:
    return 0

  if numero % 10 == digito:
    return 1 + contar_digito(numero // 10, digito)
  else:
    return contar_digito(numero // 10, digito)

# ---- Programa Principal ----
try:
  num_entero = int(input("Ingresá un número entero positivo: "))
  dig_buscado = int(input("Ingresá el dígito que desea contar (0-9): "))

  if not (0 <= dig_buscado <= 9):
    print("El dígito a buscar debe estar entre 0 y 9.")
  elif num_entero < 0:
    print("El número debe ser positivo.")
  else:
    cantidad = contar_digito(abs(num_entero), dig_buscado)
    if num_entero == 0 and dig_buscado == 0:
        cantidad = 1
    print(f"\nEl dígito {dig_buscado} aparece {cantidad} veces en el número {num_entero}.")
except ValueError:
  print("Entrada no válida. Por favor, ingresá números enteros.")
```

---

¿Querés que este archivo lo prepare para descargar como `.md` directamente o lo suba a un repositorio GitHub?
