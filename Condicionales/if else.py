edad = int(input("Introduce tu edad: "))
if edad >= 18:
    print("Eres mayor de edad.")
    print("Puedes ejercer tu derecho al voto.")
else:
    faltante = 18 - edad
    print(f"Te faltan {faltante} años para poder votar.")
print("Terminó el programa...")