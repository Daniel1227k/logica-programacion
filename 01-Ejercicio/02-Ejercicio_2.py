#* Estructuras de control

#* if - elif - else
edad = 20

if edad < 18:
    print("Eres menor de edad.")
elif edad == 18:
    print("Acabas de cumplir la mayoría de edad.")
else:
    print("Eres mayor de edad.")
  
print()
  
#* Bucle for 
usuarios = ["Ana", "Carlos", "Luis"]

for usuario in usuarios:
  print("Hola " + usuario)

#* Bucle while
bateria = 100
while bateria > 0:
    print("Usando el dispositivo... Batería al", bateria, "%")
    bateria -= 20
  
# Switch
estado_servidor = 404

match estado_servidor:
    case 200:
        print("Conexión exitosa")
    case 404:
        print("Página no encontrada")
    case 500:
        print("Error interno del servidor")
    case _:  # El guion bajo actúa como el 'else' (cualquier otro caso)
        print("Código de estado desconocido")