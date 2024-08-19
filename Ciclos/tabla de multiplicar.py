# Tabla de multiplicar de n
n = int(input("Ingrese el valor de n: "))
i = 1
while i <= 10:
    resultado = i * n
    print(f"{n} x {i} = {resultado}")
    i += 1