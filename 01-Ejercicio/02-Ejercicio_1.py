x = 10
y = 2

#* Operadores aritmeticos
sum = x + y
rest = x - y
mult = x * y
div = x / y
div_entera = x / 3
mod = x % y # regresa el residuo de la division 
exponencial = x**y

#* Operadores logicos
#! and: devuelve true solo si ambas condiciones son verdaderas
print(10 > 2 and 10 > 3) #ambas son ciertas devuelve 'true'
print(10 > 2 and 10 > 11) 
print("")

#! or: devuelve true si alguna de las dos condiciones es verdadera
print(10 > 2 or 10 > 3) 
print(10 > 2 or 10 > 11) # A diferencia de and aqui una si se cumple es decir regresara True
print(10 > 20 or 10 > 11)
print("")

#!not: invierte el valor de la condicion
print(not(10 > 2 and 10 > 3)) #Deberia volver true, lo negamos, retorna false
print(not(10 > 20 or 10 > 11)) 
print()
#* operadores de comparacion
igual = x == y  #false
diferente = x != y #true
mayor_que = x > y
menor_que = x < y
mayor_o_igual = x >= y
menor_o_igual = x <= y

#* operador de asignacion
z = 5
z += 3 # z = z + 3
z -= 3 #z= z-3
z *= 3 # z = z * 3
z /= 3 # z = z / 3
z //= 3 # z = z // 3
z %= 3 # z = z % 3
z **= 3 # z = z**3

#* Operador de pertenencia
string = 'Hola'
print('a' in string)
print('a' not in string)
print()

#* operadores de identidad
lista_a = [1, 2, 3]
lista_b = [1, 2, 3]

# lista_c ahora apunta exactamente a la misma dirección de memoria que lista_a
lista_c = lista_a 

# Comparando valores (Contenido)
print(lista_a == lista_b)  
# Resultado: True (Sus valores internos son idénticos)

# Comparando identidad (Memoria)
print(lista_a is lista_b)  
# Resultado: False (Son dos listas diferentes en la memoria)

print(lista_a is lista_c)  
# Resultado: True (Apuntan al mismo lugar exacto en la memoria)