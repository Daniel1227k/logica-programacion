"""
Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), 
pares, y que no son ni el 16 ni múltiplos de 3.
"""

x = 10
y = 55


while(x <= y):
  if(x%2 == 0 and x != 16 and x % 3 != 0):
    print(x)
  x += 1