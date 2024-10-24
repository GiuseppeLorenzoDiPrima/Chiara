# Esercizio 7

# Stampa esercizio
print("\nEsercizio 7\n")

# Inizializzo n ed m a zero
n = 0
m = 0

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

prodotto = n # Inizializzo prodotto

# Calcolo il prodotto
for i in range(m-1):
    prodotto += n

print() # Riga vuota

# Stampo il risultato
print("Il prodotto tra " + str(n) + " e " + str(m) + " vale: " + str(prodotto))
