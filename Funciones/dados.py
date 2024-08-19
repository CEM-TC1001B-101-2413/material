import random

# Simular la tirada de dos dados
# Pedir al usuario que adivine según la suma de los dados
# 1) La suma de los dados es debajo de 7
# 2) La suma de los dados es igual a 7
# 3) La suma de los dados es mayor a 7
# Indicar si el usuario ganó o perdió

dado1 = random.randrange(1,6)
dado2 = random.randrange(1,6)
suma = dado1 + dado2
opcion = int(input("""Adivina la suma de dos dados ingresando el número
1) La suma de los dados es debajo de 7
2) La suma de los dados es igual a 7
3) La suma de los dados es mayor a 7
Ingresa tu opción: """))
print(f"""El primer dado cayó: {dado1}
El segundo dado cayó: {dado2}
La suma de los dados es: {suma}""")

if suma < 7 and opcion == 1 \
   or suma == 7 and opcion == 2 \
   or suma > 7 and opcion == 3:
    print("Felicidades, has ganado.")
else:
    print("No has atinado, suerte para la próxima.")