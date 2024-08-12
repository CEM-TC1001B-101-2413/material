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
else:
    if edad <= 5:
        print("Kinder")
    else:
        if edad <= 11:
            print("Primaria")
        else:
            if edad <= 14:
                print("Secundaria")
            else:
                if edad <= 17:
                    print("Preparatoria")
                else:
                    if edad <= 21:
                        print("Licenciatura")
                    else:
                        print("Posgrado")