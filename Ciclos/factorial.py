# Factorial
# n! = n * n-1 * n-2 * ... * 1
# 5! = 5 * 4 * 3 * 2 * 1 = 120
n = int(input("Ingresa el valor de n: "))
factorial = 1
for i in range(1, n+1):
    factorial *= i
print(f"El resultado del factorial es: {factorial}")