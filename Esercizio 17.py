# Esercizio 17

# Stampa esercizio
print("\nEsercizio 17\n")

potenza = 0 # Inizializzo potenza a zero
numero_di_cifre = 0 # Inizializzo counter a zero

# Inserisco il valore
while True:
    numero = int(input("Inserisci un numero intero positivo: "))
    if numero <= 0:
        print("\nErrore, il numero deve essere maggiore di zero.\n")
    else:
        break

# Inserisci la base
while True:
    base = int(input("Inserisci un numero intero maggiore di uno: "))
    if base <= 1:
        print("\nErrore, il numero deve essere maggiore di uno.\n")
    else:
        break

while numero >= potenza:
    potenza = base ** numero_di_cifre
    numero_di_cifre += 1

numero_di_cifre -= 1
potenza = base ** (numero_di_cifre - 1) # Inizializzo al valore corretto la potenza
numero_convertito = '' # Inizializzo una stringa vuota

temp = numero # Copio il valore di numero nella variabile temporanea temp

# Conversione in binario
for i in range(numero_di_cifre):
    if temp >= potenza:
        numero_convertito += '1'
        temp -= potenza  # Sottraggo il valore della potenza
    else:
        numero_convertito += '0'

    potenza //= base  # Passo alla potenza successiva

# Stampo il risultato
print("La conversione in base " + str(base) + " del numero " + str(numero) + " è " + numero_convertito)
