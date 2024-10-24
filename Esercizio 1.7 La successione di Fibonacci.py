# Esercizio 1.7 La successione di Fibonacci

# Stampa esercizio
print("\nEsercizio 1.7 La successione di Fibonacci\n")

def fibonacci(n):

    # Inizializzazione
    serie_di_fibonacci = [] # Inizializzo una lista
    a = 1 # Inizializzo il primo valore
    b = 1 # Inizializzo il secondo valore

    for _ in range(n):
        serie_di_fibonacci.append(a) # Aggiungo il parametro inferiore alla serie di Fibonacci

        c = a + b # Calcolo il nuovo secondo parametro
        a = b # Aggiorno il primo parametro
        b = c # Aggiorno il secondo parametro

    # Restituisco la serie
    return serie_di_fibonacci

n = 0 # Inizializzo il valore di n

while n <= 0:
    # Inserisco il valore di n
    n = int(input("Inserisci un numero intero maggiore di zero: "))

    # Stampo il messaggio di errore
    if n <= 0:
        print("\nErrore, il numero deve essere maggiore di zero.\n")

    # Stampo il risultato
    else:
        print("\nI primi " + str(n) + " numeri della serie di Fibonacci sono: " + str(fibonacci(n)))
        