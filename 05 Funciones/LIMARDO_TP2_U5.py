# Importación de librerías necesarias
import math

# ------------------------------------------------------------------------------
# DEFINICIÓN DE FUNCIONES
# ------------------------------------------------------------------------------

# --- Actividad 1 ---
def imprimir_hola_mundo():
  """
  Esta función imprime el mensaje 'Hola Mundo!' en la consola.
  """
  print("Hola Mundo!")

# --- Actividad 2 ---
def saludar_usuario(nombre):
  """
  Recibe un nombre como parámetro y devuelve un saludo personalizado.
  Por ejemplo: 'Hola Marcos!'
  """
  return f"Hola {nombre}!"

# --- Actividad 3 ---
def informacion_personal(nombre, apellido, edad, residencia):
  """
  Recibe nombre, apellido, edad y residencia e imprime una frase formateada.
  """
  print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# --- Actividad 4 ---
def calcular_area_circulo(radio):
  """
  Recibe el radio y devuelve el área del círculo (π * radio^2).
  """
  area = math.pi * (radio ** 2)
  return area

def calcular_perimetro_circulo(radio):
  """
  Recibe el radio y devuelve el perímetro del círculo (2 * π * radio).
  """
  perimetro = 2 * math.pi * radio
  return perimetro

# --- Actividad 5 ---
def segundos_a_horas(segundos):
  """
  Recibe una cantidad de segundos y la devuelve convertida en horas.
  """
  # Hay 3600 segundos en una hora (60 segundos/minuto * 60 minutos/hora)
  horas = segundos / 3600
  return horas

# --- Actividad 6 ---
def tabla_multiplicar(numero):
  """
  Recibe un número e imprime su tabla de multiplicar del 1 al 10.
  """
  print(f"--- Tabla de multiplicar del {numero} ---")
  for i in range(1, 11): # El rango va de 1 hasta 10 (11 no se incluye)
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

# --- Actividad 7 ---
def operaciones_basicas(a, b):
  """
  Recibe dos números (a y b) y devuelve una tupla con los resultados de
  (a+b, a-b, a*b, a/b).
  """
  suma = a + b
  resta = a - b
  multiplicacion = a * b
  # Se añade un control para evitar la división por cero
  if b != 0:
    division = a / b
  else:
    division = "No se puede dividir por cero"
  return (suma, resta, multiplicacion, division)

# --- Actividad 8 ---
def calcular_imc(peso, altura):
  """
  Recibe el peso en kg y la altura en metros.
  Devuelve el IMC = peso / (altura^2).
  """
  if altura > 0:
    imc = peso / (altura ** 2)
    return imc
  else:
    return "La altura debe ser mayor que cero."

# --- Actividad 9 ---
def celsius_a_fahrenheit(celsius):
  """
  Recibe una temperatura en Celsius y la devuelve en Fahrenheit.
  Fórmula: (Celsius * 9/5) + 32
  """
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

# --- Actividad 10 ---
def calcular_promedio(a, b, c):
  """
  Recibe tres números y devuelve su promedio.
  """
  promedio = (a + b + c) / 3
  return promedio

# ------------------------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ------------------------------------------------------------------------------
# El siguiente bloque se ejecutará solo si este archivo es el script principal.
if __name__ == "__main__":
  # --- Ejecución Actividad 1 ---
  print("--- Ejecutando Actividad 1 ---")
  imprimir_hola_mundo()
  print("-" * 30)

  # --- Ejecución Actividad 2 ---
  print("\n--- Ejecutando Actividad 2 ---")
  nombre_ingresado = input("Por favor, ingresá tu nombre: ")
  saludo = saludar_usuario(nombre_ingresado)
  print(saludo)
  print("-" * 30)

  # --- Ejecución Actividad 3 ---
  print("\n--- Ejecutando Actividad 3 ---")
  nombre_usr = input("ingresá tu nombre: ")
  apellido_usr = input("ingresá tu apellido: ")
  edad_usr = input("ingresá tu edad: ")
  residencia_usr = input("ingresá tu lugar de residencia: ")
  informacion_personal(nombre_usr, apellido_usr, edad_usr, residencia_usr)
  print("-" * 30)

  # --- Ejecución Actividad 4 ---
  print("\n--- Ejecutando Actividad 4 ---")
  radio_usr = float(input("ingresá el radio del círculo: "))
  area_calculada = calcular_area_circulo(radio_usr)
  perimetro_calculado = calcular_perimetro_circulo(radio_usr)
  print(f"El área del círculo es: {area_calculada:.2f}")
  print(f"El perímetro del círculo es: {perimetro_calculado:.2f}")
  print("-" * 30)

  # --- Ejecución Actividad 5 ---
  print("\n--- Ejecutando Actividad 5 ---")
  segundos_usr = int(input("ingresá la cantidad de segundos a convertir: "))
  horas_convertidas = segundos_a_horas(segundos_usr)
  print(f"{segundos_usr} segundos equivalen a {horas_convertidas:.4f} horas.")
  print("-" * 30)

  # --- Ejecución Actividad 6 ---
  print("\n--- Ejecutando Actividad 6 ---")
  numero_tabla = int(input("ingresá un número para ver su tabla de multiplicar: "))
  tabla_multiplicar(numero_tabla)
  print("-" * 30)

  # --- Ejecución Actividad 7 ---
  print("\n--- Ejecutando Actividad 7 ---")
  num1 = float(input("ingresá el primer número: "))
  num2 = float(input("ingresá el segundo número: "))
  resultados = operaciones_basicas(num1, num2)
  suma_res, resta_res, multi_res, div_res = resultados
  print(f"Suma: {suma_res}")
  print(f"Resta: {resta_res}")
  print(f"Multiplicación: {multi_res}")
  print(f"División: {div_res}")
  print("-" * 30)

  # --- Ejecución Actividad 8 ---
  print("\n--- Ejecutando Actividad 8 ---")
  peso_kg = float(input("ingresá tu peso en kg: "))
  altura_m = float(input("ingresá tu altura en metros (ej: 1.75): "))
  resultado_imc = calcular_imc(peso_kg, altura_m)
  if isinstance(resultado_imc, (int, float)):
    print(f"Tu Índice de Masa Corporal (IMC) es: {resultado_imc:.2f}")
  else:
    print(resultado_imc)
  print("-" * 30)

  # --- Ejecución Actividad 9 ---
  print("\n--- Ejecutando Actividad 9 ---")
  temp_celsius = float(input("ingresá la temperatura en grados Celsius: "))
  temp_fahrenheit = celsius_a_fahrenheit(temp_celsius)
  print(f"{temp_celsius}°C equivalen a {temp_fahrenheit:.2f}°F.")
  print("-" * 30)

  # --- Ejecución Actividad 10 ---
  print("\n--- Ejecutando Actividad 10 ---")
  num_a = float(input("ingresá el primer número: "))
  num_b = float(input("ingresá el segundo número: "))
  num_c = float(input("ingresá el tercer número: "))
  resultado_promedio = calcular_promedio(num_a, num_b, num_c)
  print(f"El promedio de los tres números es: {resultado_promedio:.2f}")
  print("-" * 30)