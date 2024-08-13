# Sumatoria de 1 hasta n
# Pedir el valor de n
# Calcular la sumatoria: 1 + 2 + 3 + 4 + ... + n
# 1+2+3+4+5 = 15
n = int(input("Ingresa el valor de n: "))
sumatoria = 0
for i in range(1, n+1):
    sumatoria += i
print(f"El resultado de la sumatoria es: {sumatoria}")