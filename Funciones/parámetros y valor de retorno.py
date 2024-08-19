# Entradas -> Parámetros
# Salida -> Valor de retorno

# Sin parámetros y sin valor de retorno
def suma1():
    x = float(input("Ingresa el valor de x: "))
    y = float(input("Ingresa el valor de y: "))
    resultado = x + y
    print(f"El resultado de la suma es: {resultado}")

# Con parámetros y sin valor de retorno
def suma2(x : float, y : float):
    resultado = x + y
    print(f"El resultado de la suma es: {resultado}")

# Con parámetros y con valor de retorno
def suma3(x : float, y : float):
    resultado = x + y
    return resultado

res = suma3(2,3) + 10 - 2
print(f"El resultado de la suma es: {res}")
# suma1()
#x = float(input("Ingresa el valor de x: "))
#y = float(input("Ingresa el valor de y: "))
#suma2(x, y)
#suma2("Hola", "mundo")
#print(suma2(274, 19))