"""1. Ejercicio: Dado un número, imprime si es positivo o negativo."""

#solicitar input para calcular el resultado
numero =float(input("Introduce un número para calcular si es positivo o negativo."))
#Verificar si el numero es positivo o negativo
if numero > 0:
  print ("El número es positivo.")
elif numero >0:
  print ("El número es negativo.")
else:
  print ("El número es cero.")


"""2. Ejercicio: Dado un número, imprime si es par o impar."""

#Solicitar input para calcular si es par o impar
numero = float(input("Introduce un numero para verificar si es par o impar."))
#Verificar si el número es par o impar e imprimir el resultado
if numero % 2 ==0:
  print ("El número es par.")
else:
  print ("El número es impar.")


"""3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos."""

#Solicitar input para encontrar el mayor de 3 número
numero1 = float(input("Introduce el primer número para encontrar el mayor: "))
numero2 = float(input("Introduce el segudo número: "))
numero3 = float(input("Introduce el tercer número: "))
#Buscar cual el es mayor e imprimir
if numero1 >= numero2 and numero1 >= numero3:
  print (f"El número mayor es : {numero1}")
elif numero2 >= numero1 and numero2 >= numero3:
  print(f"El número mayor es : {numero2}")
else:
  print (f"El numero mayor es : {numero3}")