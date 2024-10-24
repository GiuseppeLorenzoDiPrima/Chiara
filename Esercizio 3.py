# Esercizio 3

# Stampa esercizio
print("\nEsercizio 3\n")

# Inizializzazione
massimo = float('-inf')
minimo = float('inf')
somma = 0

# Inserisco i tre valori
for i in range(20):
    numero = float(input("Inserisci un numero: "))
    somma += numero
    if numero > massimo:
        massimo = numero
    if numero < minimo:
        minimo = numero

print() # Riga vuota

# Stampo i risultati
print("Il massimo vale:", massimo)
print("Il minimo vale:", minimo)
print("La somma vale:", somma)
