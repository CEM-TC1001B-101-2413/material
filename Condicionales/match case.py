opcion = int(input("""Menú de opciones:
1) Opción 1
2) Opción 2
3) Salir
Ingrese su opción: """))
if opcion == 1:
    print("Uno")
elif opcion == 2:
    print("Dos")
elif opcion == 3:
    print("Saliendo...")
else:
    print("Opción inexistente")
# Match - case
match opcion:
    case 1:
        print("Uno")
    case 2:
        print("Dos")
    case 3:
        print("Saliendo...")
    case _:
        print("Opción inexistente")
