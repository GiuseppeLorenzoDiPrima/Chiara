# Esercizio 1.3 Massimo fra tre

# Stampa esercizio
print("\nEsercizio 1.3 Massimo fra tre\n")

NUMERO_VALORI = 3 # Inizializzo il numero di valori
numeri = []  # Inizializzo una lista vuota

for i in range(NUMERO_VALORI):
    # Inserisco da tastiera un numero decimale e lo aggiungo alla lista
    numeri.append(float(input("Inserisci un numero: ")))

print() # Riga vuota

# Stampo il risultato
print("Il massimo tra i numeri inseriti vale: " + str(max(numeri)))
