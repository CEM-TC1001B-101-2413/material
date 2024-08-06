# Actividad 01
# Ejercicio 01
# Aram Baruch González Pérez 4538484
# Aram Baruch González Pérez 4538484

materia1 = float(input("Introduce la calificación de tu materia 1: "))
materia2 = float(input("Introduce la calificación de tu materia 2: "))
materia3 = float(input("Introduce la calificación de tu materia 3: "))
materia4 = float(input("Introduce la calificación de tu materia 4: "))
bloque1 = float(input("Introduce la calificación de tu bloque 1: "))
bloque2 = float(input("Introduce la calificación de tu bloque 2: "))
bloque3 = float(input("Introduce la calificación de tu bloque 3: "))
promedio = (materia1 + materia2 + materia3 + materia4 + bloque1 + bloque2 + bloque3) / 7

# Formas clásicas
print("El promedio es:", promedio)
print("El promedio es: " + str(promedio))
print("El promedio es: {0:,.2f} {1:,.2f}".format(promedio, 274747834.5))
# Formato moderno - f-strings
print(f"El promedio es: {promedio:,.2f}")
# : -> Formato especial
# , -> Separador de miles
# .2 -> Número de decimales a redondear
# f -> Mostrarlo como float, de lo contrario se usa formato científico