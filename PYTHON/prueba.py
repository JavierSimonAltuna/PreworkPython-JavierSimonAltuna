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