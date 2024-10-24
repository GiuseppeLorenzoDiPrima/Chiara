# Esercizio 12

# Stampa esercizio
print("\nEsercizio 12\n")

# Inizializzo una lista
numeri = []

# Inserisco i valori
while True:
    numero = float(input("Inserisci un numero - 0.0 per terminare l'inserimento\nNumero: "))
    if numero != 0.0:
        numeri.append(numero)
    else:
        break

ordinati = True # Inizializzo un flag booleano

for i in range(len(numeri) - 1):
    if numeri[i] > numeri[i+1]:
        ordinati = False
        break

print() # Riga vuota

if ordinati:
    print("Ordinata crescente")
else:
    print("Non ordinata")
