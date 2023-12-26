"""1. Ejercicio: Imprime los números del 1 al 10 usando un bucle for ."""

for numeros in range (1,11):
  print(numeros)

"""2. Ejercicio: Imprime los números pares del 1 al 20 usando un bucle while ."""
numero = 1
while numero <= 20:
  if numero % 2 ==0:
    print (numero)
  numero += 1

"""3. Ejercicio: Usa un bucle para calcular la suma de los números del 1 al 100."""
suma = 0
for x in range (1, 100):
  suma += x
print (f"La suma de los números del 1 al 100 es: {suma}")