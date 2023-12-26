"""1. Ejercicio: Define una función que tome dos números y retorne su suma."""
def suma_numeros():
  num1 = float(input("Introduce el primer número para sumar: "))
  num2= float(input("Introduce el segundo número: "))
  return num1 + num2

resultado = suma_numeros()
print(resultado)

"""2. Ejercicio: Defineuna función que tome un número y retorne su factorial."""
def factorial():
  numero = int(input("Introduce un número para calcular su factorial: "))
  if numero < 0:
    return "factorial no definido para números negativos."
  elif numero == 0 or numero == 1:
    return 1
  else:
    resultado = 1
    for x in range(2,numero +1):
      resultado *= x
    return resultado
  
resultado_factorial = factorial()
print(resultado_factorial)

"""3. Ejercicio: Define una función que tome un número y determine si es primo."""
def primo():
  numero = int(input("Introduce un número para verificar si es primo: "))
  if numero < 2 :
    return "No es primo"
  for i in range(2, int(numero**0.5) +1):
    if numero % 1 == 0:
      return "No es primo: "
  return "Es primo"
print (primo())

"""4. Ejercicio: Define una función que reciba una lista de números y retorne la suma
de ellos."""
def suma_lista():
  numeros = input("Introduce una lista de números separados por espacios para sumar: ")
  numeros =[float(x) for x in numeros.split()]
  return sum(numeros)

print(suma_lista())

"""5. Ejercicio: Define una función que reciba una cadena de texto y retorne la
cadena en reversa."""
def cadena_reversa(cadena):
  return cadena [::-1]

cadena_original = input("Introduce una cadena de texto para revertirla: ")
resultado_reversa = cadena_reversa(cadena_original)
print(resultado_reversa)