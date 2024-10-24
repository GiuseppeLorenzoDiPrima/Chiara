# Esercizio 18

# Stampa esercizio
print("\nEsercizio 18\n")

# Inserisco i due valori
m = int(input("Inserisci il primo numero intero positivo: "))
n = int(input("Inserisci il secondo numero intero positivo: "))

resto = 1 # Inizializzo il resto

temp_n = n # Inizializzo la variabile temporanea
temp_m = m # Inizializzo la variabile temporanea

while resto != 0:
    resto = max(temp_m, temp_n) % min(temp_m, temp_n)
    if resto == 0:
        break
    else:
        temp_m = temp_n
        temp_n = resto

print("\nIl massimo comune divisore tra " + str(m) + " e " + str(n) + " vale:", temp_n)