precio = 0
cuenta = 0
while precio >= 0:
    cuenta += precio
    precio = float(input("Ingrese el precio de su producto: "))
print(f"La cuenta a pagar es de: ${cuenta:,.2f}")
# -------------------------
cuenta = 0
while (precio := float(input("Ingrese el precio de su producto: "))) >= 0:
    cuenta += precio
print(f"La cuenta a pagar es de: ${cuenta:,.2f}")