# Esercizio 14

# Stampa esercizio
print("\nEsercizio 14\n")

# Inserisco il valore
while True:
    numero = float(input("Inserisci un numero: "))
    if numero <= 1:
        print("\nErrore, il numero deve essere maggiore di uno.\n")
    else:
        break

primo = True # Inizializzo un flag booleano

# Controllo se il numero è primo
for i in range(2, int(numero**0.5) + 1):
    if numero % i == 0:
        primo = False

print() # Riga vuota

if primo:
    print("1")
else:
    print("0")
