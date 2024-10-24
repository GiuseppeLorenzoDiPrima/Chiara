# Esercizio 5

# Stampa esercizio
print("\nEsercizio 5\n")

# Funzione per calcolare la somma dei numeri dispari nell'intervallo (0, n)
def somma_numeri_dispari(n):
    somma = 0
    for i in range(n):
        if i % 2 != 0:
            somma += i
    if n % 2 != 0:
        somma += n
    return somma

# Inizializzo n a zero
n = 0

# Inserisco il numero
while n <= 0:
    # Inserisco il valore di n
    n = int(input("Inserisci un numero intero maggiore di zero: "))

    # Stampo il messaggio di errore
    if n <= 0:
        print("\nErrore, il numero deve essere maggiore di zero.\n")

    # Stampo il risultato
    else:
        print("\nLa somma dei numeri dispari che vanno da 0 a " + str(n) + " vale: " + str(somma_numeri_dispari(n)))
