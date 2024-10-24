# Esercizio 6

# Stampa esercizio
print("\nEsercizio 6\n")

# Funzione per calcolare il fattoriale
def fattoriale(n):
    risultato = 1
    for i in range(n, 0, -1):
        risultato *= i
    return risultato

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
        print("\n" + str(n) + "! vale: " + str(fattoriale(n)))
        