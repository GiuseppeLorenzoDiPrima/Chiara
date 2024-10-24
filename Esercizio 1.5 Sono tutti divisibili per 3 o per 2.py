# Esercizio 1.5 Sono tutti divisibili per 3 o per 2?

# Stampa esercizio
print("\nEsercizio 1.5 Sono tutti divisibili per 3 o per 2?\n")

numeri = [] # Inizializzo una lista
divisibile = True # Inizializzo un flag booleano

while True:
    numero = int(input("Inserisci un numero, -1 per terminare l'inserimento\nNumero: "))

    # Effettuo un controllo per verificare la terminazione dell'inserimento
    if numero != -1:
        numeri.append(numero) # Aggiungo il numero in lista
    else:
        break

print() # Riga vuota

for value in numeri:
    # Verifico la divisibilità per 2 o per 3
    if not(((value % 2) == 0) or ((value % 3) == 0)):
        divisibile = False # Se non dovesse essere divisibile
        break

# Se non divisibile
if not divisibile:
    print("NO")

# Se divisibile
else:
    print("OK")
