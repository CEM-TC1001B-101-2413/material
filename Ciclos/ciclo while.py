# for i in range(5) -> 0,1,2,3,4
i = 0 # Inicialización de la variable de control (contador)
while i <= 4: # Condición de paro o de salida
    print(f"El valor de i es: {i}")
    i += 1 # Paso

print("-" * 30)

texto = "Hola mundo"
# H -> 0, o -> 1, l -> 2, a ->3, ... , o -> 9
# for i in texto:
i = 0
while i < len(texto):
    print(f"texto[{i}] = {texto[i]}")
    i += 1
    
print("-" * 30)

continuar = 1
while continuar == 1:
    continuar = int(input("¿Desea continuar? 1)Sí, 2)No: "))
