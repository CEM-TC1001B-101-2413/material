materia1 = float(input("Introduce la calificación de tu materia 1: "))
materia2 = float(input("Introduce la calificación de tu materia 2: "))
materia3 = float(input("Introduce la calificación de tu materia 3: "))
materia4 = float(input("Introduce la calificación de tu materia 4: "))
bloque1 = float(input("Introduce la calificación de tu bloque 1: "))
bloque2 = float(input("Introduce la calificación de tu bloque 2: "))
bloque3 = float(input("Introduce la calificación de tu bloque 3: "))
promedio = (materia1 + materia2 + materia3 + materia4 + bloque1 + bloque2 + bloque3) / 7
print(f"El promedio es: {promedio:,.2f}")
if promedio > 90:
    print("Ha sido un excelente semestre.")
elif promedio >= 80:
    print("Ha sido un buen semestre.")
else:
    print("Tienes que ponerte a estudiar más.")