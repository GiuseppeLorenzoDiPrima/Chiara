# Esercizio 1.4 Somma di una sequenza

# Stampa esercizio
print("\nEsercizio 1.4 Somma di una sequenza\n")

somma = 0 # Inizializzo una variabile

# Ciclo infinito
while True:
    # Inserisco valori interi
    numero = int(input("Inserisci un numero, -1 per terminare l'inserimento\nNumero: "))

    # Effettuo un controllo per verificare la terminazione dell'inserimento
    if numero != -1:
        somma += numero
    else:
        break

print() # Riga vuota

# Stampo il risultato
print("La somma dei valori inseriti vale: " + str(somma))
