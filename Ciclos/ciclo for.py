# range(final) -> Genera una secuencia numérica que inica en 0
# avanza de uno en uno y termina antes de final
for i in range(5):
    print(f"El valor de i es: {i}")

print("-" * 30)

# range(inicio, final) -> Genera una secuencia numérica que inica en
# inicio, avanza de uno en uno y termina antes de final
for i in range(5, 10):
    print(f"El valor de i es: {i}")
    
print("-" * 30)

# range(inicio, final, paso) -> Genera una secuencia numérica que inicia
# en inicio, avanza de paso en paso y termina antes de final
for i in range(5, 30, 3):
    print(f"El valor de i es: {i}")
    
print("-" * 30)

for i in range(10, 5, -1):
    print(f"El valor de i es: {i}")
    
print("-" * 30)

texto = "Hola mundo"
for i in texto:
    print(f"El valor de i es: {i}")
    
print("-" * 30)

lista = ["hola", 34567, True, [1,2], "adiós"]
for i in lista:
    print(f"El valor de i es: {i}")
