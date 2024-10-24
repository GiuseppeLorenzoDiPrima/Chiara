# Esercizio 1

# Stampa esercizio
print("\nEsercizio 1\n")

def print_triangular_numbers(n):
    # Inizializzazione
    triangolari = [] # Inizializzo una lista
    b = 0 # Inizializzo il secondo valore

    for i in range(1, n + 1):
        triangolari.append(i) # Aggiungo il parametro inferiore alla serie di Fibonacci
        b += i # Aggiorno il secondo parametro
        triangolari.append(b) # Aggiungo il parametro inferiore alla serie di Fibonacci

    # Restituisco la serie
    return triangolari

n = 0 # Inizializzo il valore di n

while n <= 0:
    # Inserisco il valore di n
    n = int(input("Inserisci un numero intero maggiore di zero: "))

    # Stampo il messaggio di errore
    if n <= 0:
        print("\nErrore, il numero deve essere maggiore di zero.\n")

    # Stampo il risultato
    else:
        print("\nI primi " + str(n) + " numeri triangolari sono:\n")
        triangolari = print_triangular_numbers(n)
        for i in range(0, 2 * n, 2):
            print(str(triangolari[i]) + str("\t") + str(triangolari[i + 1]))
