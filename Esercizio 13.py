# Esercizio 13

# Stampa esercizio
print("\nEsercizio 13\n")

# Inizializzo una lista
numeri = []

# Inserisco i valori
while True:
    numero = float(input("Inserisci un numero - 0.0 per terminare l'inserimento\nNumero: "))
    if numero != 0.0:
        numeri.append(numero)
    else:
        break

ordinati_crescenti = True # Inizializzo un flag booleano
ordinati_decrescenti = True # Inizializzo un flag booleano

# Controllo se sono in ordine crescente
for i in range(len(numeri) - 1):
    if numeri[i] > numeri[i+1]:
        ordinati_crescenti = False
        break

# Controllo se sono in ordine decrescente
for i in range(len(numeri) - 1):
    if numeri[i] < numeri[i+1]:
        ordinati_decrescenti = False
        break

print() # Riga vuota

if ordinati_crescenti:
    print("Ordinata crescente")
elif ordinati_decrescenti:
    print("Ordinata decrescente")
else:
    print("Non ordinata")
