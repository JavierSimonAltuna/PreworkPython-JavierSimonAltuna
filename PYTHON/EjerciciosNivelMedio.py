#Ejercicios nivel medio
"""1. Ejercicio: Define una función que utilice un bucle para imprimir los primeros n
números de la serie de Fibonacci."""
def fibonacci (n):
  fib_series =[0, 1]
  for _ in range (2, n):
    next_num = fib_series[-1] + fib_series[-2]
    fib_series.append(next_num)
  return fib_series

n = int(input("Introduce un numero para calcular los n primeros número de la seria Fibonacci: "))
print (f"Los primero {n} números de la seria fibonacci son : {fibonacci(n)}")


"""2. Ejercicio: Define una función que tome un número y retorne una lista de sus
divisores."""
def divisores (numero):
  divisor_list = [i for i in range(1, numero + 1) if numero% i == 0]
  return divisor_list

num =int(input("Introduce un número para calcular sus divisores: "))
print(f"Los divisores de {num} son: {divisores(num)}")

"""3. Ejercicio: Define una función que tome una lista y retorne una nueva lista con
los elementos únicos de la lista original."""
def elementos_unicos_desde_input():
  elementos_input = input("introduce una lista separada por espacios para extrar los elementos únicos: ")
  lista_original = elementos_input.split()
  conjunto_unico = set(lista_original)
  lista_unicos = list(conjunto_unico)
  return lista_unicos

resultado = elementos_unicos_desde_input()
print(f"Elementos originales {resultado}")


"""4. Ejercicio: Define una función que tome un número y retorne la suma de sus
dígitos."""
def suma_digitos(numero):
    suma = 0
    for digito in str(numero):
        suma += int(digito)
    return suma
num = int(input("Ingresa un número para calcular la suma de sus dígitos: "))
resultado = suma_digitos(num)
print(f"La suma de los dígitos de {num} es: {resultado}")


"""5. Ejercicio: Define una función que tome una cadena y cuente el número de
vocales en la cadena."""
def contar_vocales():
    cadena = input("Por favor, introduce una cadena para contar el número de vocales: ")
    vocales = 'aeiouAEIOU'
    return sum(1 for letra in cadena if letra in vocales)

print(f"El número de vocales en la cadena es: {contar_vocales()}")

"""6. Ejercicio: Define una función que tome una lista y un número n, y retorne los
primeros n elementos de la lista."""
def primeros_n_elementos():
   lista = list(input("Introduce una lista de elementos para extraer los elementos en posicion (n)").split())
   n = int(input("Introduce un número: "))
   return lista [:n]

resultado = primeros_n_elementos()

print (f"Los primeros {len(resultado)} elementos de la lista son: {resultado}")

"""7. Ejercicio: Define una función que tome una cadena y retorne la cantidad de
letras mayúsculas y minúsculas en la cadena."""
def contar_mayusculas_minusculas():
   cadena = input("Introduce una cadena para contar las letras mayúsculas y minusculas: ")
   mayusculas = sum(1 for letra in cadena if letra.isupper())
   minusculas = sum(1 for letra in cadena if letra.islower())
   return mayusculas, minusculas
mayusculas, minusculas = contar_mayusculas_minusculas()
print(f"La cadena tiene {mayusculas} letras mayúsculas y {minusculas}. ")

"""8. Ejercicio: Define una función que tome un número y retorne True si es un
número perfecto, False en caso contrario. Un número perfecto es aquel que es
igual a la suma de sus divisores propios positivos. Por ejemplo, 6 es un número
perfecto porque sus divisores son 1, 2 y 3, y 6 = 1 + 2 + 3."""
def es_numero_perfecto():
    numero = int(input("Introduce un número para comprobar si es perfecto: "))
    suma = sum(i for i in range(1, numero) if numero % i == 0)
    return suma == numero
print(f"¿Es el número perfecto? {es_numero_perfecto()}")


"""9. Ejercicio: Define una función que reciba un número y retorne su
representación en binario."""
def a_binario():
  numero = int(input("Introduce un número para representación binaria: "))
  binario = bin(numero)[2:]
  return binario

resultado = a_binario()
print(f"La representacion binaria del número es: {resultado}")

"""10. Ejercicio: Define una función que reciba dos listas y retorne la intersección de
ambas (los elementos que están en las dos listas)."""

def interseccion_listas():
    lista1 = list(input("Por favor, introduce la primera lista separada por espacios para comprobar la intersección de ambas: ").split())
    lista2 = list(input("Por favor, introduce la segunda lista separa por espacios: ").split())
    return list(set(lista1) & set(lista2))
print(f"La intersección de las dos listas es: {interseccion_listas()}")

"""11. Ejercicio: Define una función que tome una cadena y determine si es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda)."""
def es_palindromo():
   cadena = input("Introduce una cadena para verificar si es palíndromo: ")
   return cadena == cadena [::-1]
print(f"¿Es la cadena un palíndromo?{es_palindromo()}")

"""12. Ejercicio: Escribe un programa que imprima los números del 1 al 50, pero para
múltiplos de tres imprima “Fizz” en lugar del número y para los múltiplos de
cinco imprima “Buzz”. Para números que son múltiplos de tanto tres como cinco
imprima “FizzBuzz”."""
for i in range(1, 51):
   if i % 3 == 0 and i % 5 == 0:
      print("FizzBuzz")
   elif i % 3 == 0:
      print("Fizz")
   elif i % 5 == 0:
      print("Buzz")
   else:
      print(i)


"""13. Ejercicio: Define una función que tome una lista y retorne la lista ordenada en
orden ascendente."""
def ordenar_lista():
    lista = list(input("Introduce una lista para ordenar, separado por espacios: ").split())
    lista = [int(i) for i in lista]
    lista.sort()
    return lista

print(f"La lista ordenada en orden ascendente es: {ordenar_lista()}")


"""14. Ejercicio: Define una función que reciba una lista de palabras y un entero n, y
retorne la lista de palabras que son más largas que n."""

def palabras_largas():
    palabras = input("Introduce una lista de palabras para comprobari si son más largas que n: ").split()
    n = int(input("Introduce un número: "))
    return [palabra for palabra in palabras if len(palabra) > n]
print(f"Las palabras que son más largas que n son: {palabras_largas()}")

"""15. Ejercicio: Define una función que tome un número y calcule su serie de
Fibonacci."""
def fibonacci (n):
  fib_series =[0, 1]
  for _ in range (2, n):
    next_num = fib_series[-1] + fib_series[-2]
    fib_series.append(next_num)
  return fib_series
n = int(input("Inngrese un número para calcular la serie fibonacci: "))

resultado = fibonacci(n)
print(f"Serie Fibonacci para los primeros {n} números: {resultado}" )

"""16. Ejercicio: Define una función que tome una lista de números y retorne el
número más grande de la lista."""
def numero_mas_grande():
  lista =input("Introduce una lista de números separados por comas para calcular el más grande: ")
  lista = list(map(int, lista.split(",")))

  return max (lista)

print(numero_mas_grande())

"""17. Ejercicio: Define una función que reciba un número y retorne la suma de sus
dígitos al cubo."""

def suma_digitos_al_cubo():
   try:
      numero = int(input("Introduce un número: "))
      numero_str = str(numero)
      suma_cubos = sum(int(digito) ** 3 for digito in numero_str)
      return suma_cubos
   except ValueError: 
      return "Error: Ingresa un número válido."
   
resultado = suma_digitos_al_cubo()
print("La suma de los cubos de los dígitos es: ", resultado)
"""18. Ejercicio: Define una función que reciba una lista de números y retorne el
segundo número más grande de la lista."""
def segundo_maximo(lista):
   return sorted(set(lista), reverse=True) [1]
input_lista = input("Introduce una lista de números separados por espacios para calcular el segundo mas alto")
lista_numeros = [float(num) for num in input_lista.split()]
resultado = segundo_maximo(lista_numeros)
print(f"El segundo número más alto es: {resultado}")

"""19. Ejercicio: Define una función que tome dos listas y retorne True si tienen al
menos un miembro en común, de lo contrario, retorne False."""

def tienen_comun (lista1, lista2):
   return bool(set(lista1) & set(lista2))

input_lista1 = input("Introduce una lista de números separados por espacios para comprobar si tienen miembro común: ")
input_lista2 = input("Introduce una lista de números separados por espacios:")

lista_numeros1 = [float(num) for num in input_lista1.split()]
lista_numeros2 = [float(num) for num in input_lista2.split()]

resultado = tienen_comun(lista_numeros1, lista_numeros2)
print(f"Las listas tienen elementos en común: {resultado}")

"""20. Ejercicio: Define una función que tome una lista y retorne una nueva lista con
los elementos de la lista original en orden inverso."""

def invertir_lista(lista):
   return lista[::-1]
input_lista = input("Introduce una lista de números separados por espacios para retomar la lista en sentido inverso: ")
lista_numeros = [int(num) for num in input_lista.split()]
resultado = invertir_lista(lista_numeros)
print(f"Lista invertida: {resultado}")
"""21. Ejercicio: Define una función que reciba una cadena y cuente el número de
dígitos y letras que contiene."""

def contar_digitos_letras(cadena):
   digitos = sum(o.isdigit() for o in cadena)
   letras = sum(o.isalpha() for o in cadena)
   return digitos,letras
input_cadena = input ("Introduce una cadena de texto para contar el numero de digitos y letras: ")
resultado_digitos, resultado_letras = contar_digitos_letras(input_cadena)
print(f"La cadena ingresada tiene {resultado_digitos} digitos y {resultado_letras} letras.")

"""22. Ejercicio: Define una función que reciba una lista de números y retorne la
suma acumulada de los números"""

def suma_acumulada(lista):
   total = 0 
   suma_acumulada = []
   for numero in lista:
      total += numero
      suma_acumulada.append(total)
   return suma_acumulada

input_lista = input("Introduce una lista de números separados por espacios para retomar la suma acumulada: ")
lista_numeros = [float(num) for num in input_lista.split()]
resultado = suma_acumulada(lista_numeros)
print(f"La suma acumulada de la lista es: {resultado}")

"""23. Ejercicio: Define una función que encuentre el elemento más común en una
lista."""
from collections import Counter

def elemento_mas_comun(lista):
   return Counter(lista).most_common(1)[0][0]
input_lista = input("Introduce una lista de números separados por espacios para buscar el elemento mas común: ")
lista_numeros = [int(num) for num in input_lista.split()]
resultado = elemento_mas_comun(lista_numeros)

print(f"El elemento más común en la lista es: {resultado}")


"""24. Ejercicio: Define una función que tome un número y retorne un diccionario con
la tabla de multiplicar de ese número del 1 al 10."""
def tabla_de_multiplicar(numero):
   return {i: numero * i for i in range(1,11)}
numero_ingresado = int(input("Introduce un numero para generar la tabla de multiplicar: "))

resultado = tabla_de_multiplicar(numero_ingresado)
print(resultado)

"""25. Ejercicio: Define una función que tome una cadena y retorne un diccionario
con la cantidad de apariciones de cada caracter en la cadena."""
def contar_caracteres(cadena):
   return{caracter: cadena.count(caracter) for caracter in cadena}
cadena_ingresada = input("Introduce un cadena para retomar un diccionario con la cantidad de apariciones de cada caracter: ")

resultado = contar_caracteres(cadena_ingresada)
print (resultado)


"""26. Ejercicio: Define una función que tome dos listas y retorne la lista de
elementos que no están en ambas listas."""
def elementos_no_comunes(lista1 , lista2):
   return list(set(lista1) ^set(lista2))
lista1_ingresada = input("Introduce la primera lista de número separados por espacios para retomar los que no son común con la segunda lista")
lista2_ingresada = input("Introduce la segunda lista de números")

lista1 = [int(num) for num in lista1_ingresada.split()]
lista2 = [int(num) for num in lista2_ingresada.split()]

resultado = elementos_no_comunes(lista1, lista2)
print(resultado)

"""27. Ejercicio: Define una función que tome una lista y retorne la lista sin
duplicados."""
def eliminar_duplicados(lista):
   return list(set(lista))
lista_ingresada = input("Introduce una lista de números separados por espacios para retomar los duplicados: ")
lista_numeros = [int(num) for num in lista_ingresada.split()]

resultado = eliminar_duplicados(lista_numeros)
print (resultado)


"""28. Ejercicio: Define una función que reciba un número entero positivo y retorne la
suma de los cuadrados de todos los números pares menores o iguales a ese
número."""
def suma_cuadrados_pares(n):
   return sum(i**2 for i in range(2,n+1,2))
numero_ingresado = int(input(
   "Introduce un número entero positivo para retornar la suma de los      cuadrados de todos los números pares menores o iguales a ese número: "))
resultado = suma_cuadrados_pares(numero_ingresado)
print(resultado)

"""29. Ejercicio: Define una función que reciba una lista de números y retorne el
promedio de los números en la lista."""
def promedio(lista):
   return sum(lista) / len (lista)
lista_ingresada = input("Introduce una lista de números separados por espacios para calcular el promedio: ")
lista_numeros =[float(num) for num in lista_ingresada.split()]
resultado = promedio(lista_numeros)
print(resultado)

"""30. Ejercicio: Define una función que reciba una lista de cadenas y retorne la
cadena más larga en la lista."""
def cadena_mas_larga(lista):
   return max(lista, key=len)
lista_ingresada = input("Introduce una lista de cadenas separadas por espacios para encontrar la cadena más larga: ")
lista_cadenas = lista_ingresada.split()
resultado = cadena_mas_larga(lista_cadenas)
print (resultado)

"""31. Ejercicio: Define una función que reciba un número entero n y retorne una lista
con los n primeros números primos."""
def es_primo(num):
   if num < 2:
      return False
   for i in range(2, int(num ** 0.5) + 1):
      if num % i ==0:
         return False
   return True

def primeros_n_primos(n):
   primos = []
   numero = 2
   while len(primos) < n:
      if es_primo(numero):
         primos.append(numero)
      numero +=1
   return primos

n = int(input("Introduce un número par encontrar los primeros n primos: "))

resultado = primeros_n_primos(n)
print(resultado)

"""32. Ejercicio: Define una función que reciba una cadena y retorne la misma cadena
pero con las palabras en orden inverso."""
def invertir_palabras(cadena):
   return ' ' .join(cadena.split()[::-1])
cadena_ingresada = input("Introduce una cadena para invertirla: ")
resultado = invertir_palabras(cadena_ingresada)
print(resultado)

"""33. Ejercicio: Escribe una función que reciba una lista de tuplas y retorne una lista
ordenada basada en el último elemento de cada tupla."""

def ordenar_por_ultimo_elemento(tuplas):
   return sorted(tuplas, key=lambda x: x[-1])
tuplas_ingresadas = input("Introduce una lista de tuplas separadas por espacios para ordenarlas por el último elemento: ")
tuplas = [tuple(map(int, tupla.split(','))) for tupla in tuplas_ingresadas.split()]

resultado = ordenar_por_ultimo_elemento(tuplas)
print(resultado)

"""34. Ejercicio: Define una función que reciba una cadena y retorne la cantidad de
letras vocales en la cadena."""
def contar_vocales(cadena):
   return sum(1 for c in cadena.lower() if c in 'aeiou')
cadena_ingresada = input("Introduce una cadena para contar las vocales: ")

resultado = contar_vocales(cadena_ingresada)
print(resultado)

"""35. Ejercicio: Define una función que reciba un número entero y retorne True si es
un número primo, de lo contrario retorne False"""
def es_primo(num):
   if num < 2:
      return False
   for i in range(2, int(num ** 0.5) + 1):
      if num % i == 0:
         return False
   return True
numero_ingresado = int(input("Introduce un número para comprobar si es primo: "))
                             
resultado = es_primo(numero_ingresado)
print(resultado)
