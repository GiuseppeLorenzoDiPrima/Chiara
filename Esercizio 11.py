# Esercizio 11

# Stampa esercizio
print("\nEsercizio 11\n")

# Inizializzo una lista
numeri = []

k = int(input("Inserisci il valore k: "))

print() # Riga vuota

for i in range(k):
    numero = int(input("Inserisci un numero: "))
    numeri.append(numero)

if 0 in numeri:
    print("\nZero contenuto nella sequenza")
else:
    print("\nZero non contenuto nella sequenza")
