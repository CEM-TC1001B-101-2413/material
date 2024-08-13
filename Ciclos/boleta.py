udfs = int(input("Ingresa el número de unidades de formación que cursaste: "))
promedio = 0
for i in range(1, udfs+1):
    udf = float(input(f"Introduce la calificación de tu udf {i}: "))
    # promedio = promedio + udf
    promedio += udf
# promedio = promedio / udfs
promedio /= udfs
print(f"El promedio es: {promedio:,.2f}")
if promedio > 90:
    print("Ha sido un excelente semestre.")
elif promedio >= 80:
    print("Ha sido un buen semestre.")
else:
    print("Tienes que ponerte a estudiar más.")