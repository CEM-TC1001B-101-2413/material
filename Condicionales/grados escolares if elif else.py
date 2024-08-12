# sin escuela - menos de 3
# kinder - 3 a 5
# primaria - 6 a 11
# secundaria - 12 a 14
# preparatoria - 15 a 17
# licenciatura - 18 a 21
# posgrado - 22 en adelante
edad = int(input("Introduce tu edad: "))
if edad < 3:
    print("Todavía no estás en edad de acudir a la escuela.")
elif edad <= 5:
    print("Kinder")
elif edad <= 11:
    print("Primaria")
elif edad <= 14:
    print("Secundaria")
elif edad <= 17:
    print("Preparatoria")
elif edad <= 21:
    print("Licenciatura")
else:
    print("Posgrado")
