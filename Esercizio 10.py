# Esercizio 10

# Stampa esercizio
print("\nEsercizio 10\n")

# Inizializzo n ed m a zero
n = -1
m = -1

# Inizializzo il valore di potenza
potenza = 0

# Inserisco il numero n
while n <= 0:
    # Inserisco il valore di n
    n = int(input("Inserisci un numero intero maggiore di zero: "))

    # Stampo il messaggio di errore
    if n <= 0:
        print("\nErrore, il numero deve essere maggiore di zero.\n")

# Inserisco il numero m
while m <= 0:
    # Inserisco il valore di m
    m = int(input("Inserisci un numero intero maggiore di zero: "))

    # Stampo il messaggio di errore
    if m <= 0:
        print("\nErrore, il numero deve essere maggiore di zero.\n")

potenza = n # Inizializzo la variabile potenza

# Calcolo il prodotto
for i in range(m-1):
    potenza *= n

print() # Riga vuota

# Stampo il risultato
print("Il resto della potenza " + str(n) + "**" + str(m) + " vale: " + str(potenza))
