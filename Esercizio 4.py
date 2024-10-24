# Esercizio 4

# Stampa esercizio
print("\nEsercizio 4\n")

# Inizializzazione
massimo = float('-inf')
minimo = float('inf')
somma = 0

# Inserisco i tre valori
while True:
    numero = float(input("Inserisci un numero: "))
    if numero != 0.0:
        somma += numero
        if numero > massimo:
            massimo = numero
        if numero < minimo:
            minimo = numero
    else:
        break

print() # Riga vuota

# Stampo i risultati
print("Il massimo vale:", massimo)
print("Il minimo vale:", minimo)
print("La somma vale:", somma)
