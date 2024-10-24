# Esercizio 15

# Stampa esercizio
print("\nEsercizio 15\n")

# Inserisco i tre valori
a = float(input("Coefficiente a: "))
b = float(input("Coefficiente b: "))
c = float(input("Coefficiente c: "))

# Calcolo il delta
delta = (b**2 - 4 * a * c)

print() # Riga vuota

# Calcolo e stampo le soluzioni
if delta >= 0:
    soluzione_1 = ((-b + delta**0.5) / (2 * a))
    soluzione_2 =((-b - delta**0.5) / (2 * a))

    # Stampo le soluzioni:
    print("Soluzione 1: ", soluzione_1)
    print("Soluzione 2: ", soluzione_2)
else:
    print("L'equazione non ammette soluzioni reali")