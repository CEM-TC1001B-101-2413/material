alumnos = ["Juan", "Pedro", "Pepe", "María", "Wicho"]
nombre = input("Ingresa el nombre a buscar: ")
encontrado = False
for alumno in alumnos:
    if nombre == alumno:
        encontrado = True
if encontrado == True:
    print("El alumno se encuentra en la lista.")
else:
    print("El alumno no está en la lista.")
    
# ---------------------------------------
# break -> Detiene de manera prematura el ciclo
# continue -> Detiene la repetición actual del ciclo y pasa a la siguiente

for alumno in alumnos:
    if nombre == alumno:
        print("El alumno se encuentra en la lista.")
        break
else: # Se ejecuta siempre y cuando no se haya detenido de manera prematura el ciclo
    print("El alumno no está en la lista.")