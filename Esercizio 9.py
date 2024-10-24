# Esercizio 9

# Stampa esercizio
print("\nEsercizio 9\n")

# Inizializzo n ed m a zero
n = -1
m = -1

# Inizializzo il contatore e il resto a zero
counter = 0
resto = 0

# Inserisco il numero n
while n < 0:
    # Inserisco il valore di n
    n = int(input("Inserisci un numero intero maggiore o uguale a zero: "))

    # Stampo il messaggio di errore
    if n < 0:
        print("\nErrore, il numero deve essere maggiore o uguale a zero.\n")

# Inserisco il numero m
while m <= 0:
    # Inserisco il valore di m
    m = int(input("Inserisci un numero intero maggiore di zero: "))

    # Stampo il messaggio di errore
    if m <= 0:
        print("\nErrore, il numero deve essere maggiore di zero.\n")

risultato = n # Inizializzo prodotto

# Calcolo il prodotto
while risultato >= 0:
    risultato -= m
    counter += 1

counter -= 1

print() # Riga vuota

risultato = n # Inizializzo nuovamente prodotto

for i in range(counter):
    risultato -= m
    resto = risultato

# Stampo il risultato
print("Il resto della divisione tra " + str(n) + " e " + str(m) + " vale: " + str(resto))
