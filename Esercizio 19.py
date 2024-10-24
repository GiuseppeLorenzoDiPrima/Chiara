# Esercizio 19

# Stampa esercizio
print("\nEsercizio 19\n")

# Funzione per determinare l'ordinata fornita l'ascissa
def calcola_ordinata(x):
    y = 5 * x ** 3 + 4 * x ** 2 + 7 * x + 5
    return y

# Funzione integrale analitico
def integrale_analitico(x):
    return (5/4) * x**4 + (4/3) * x**3 + (7/2) * x**2 + 5 * x

# Inserisco i tre valori
a = float(input("Inserisci l'estremo inferiore dell'integrale: "))
b = float(input("Inserisci l'estremo superiore dell'integrale: "))
n = int(input("Inserisci il numero intero di suddivisioni da effettuare: "))

# Inizializzo l'area
area = 0

# Determino la dimensione dell'intervallo
dimensione_intervallo = (b - a) / n

# Inizializzo gli estremi dell'intervallo
estremo_inferiore = a
estremo_superiore = a + dimensione_intervallo

for i in range(n):
    # Calcolo la dimensione delle due basi
    y_inferiore = calcola_ordinata(estremo_inferiore)
    y_superiore = calcola_ordinata(estremo_superiore)

    # Calcolo il valore dell'area -> Area = base maggiore + base minore * altezza / 2
    area += ((y_superiore + y_inferiore) * dimensione_intervallo) / 2

    # Aggiorno gli estremi
    estremo_inferiore = estremo_superiore
    estremo_superiore += dimensione_intervallo

# Calcolo analiticamente l'area dell'integrale
area_analitica = integrale_analitico(b) - integrale_analitico(a)

print("\nL'area calcolata approssimando attraverso il metodo dei trapezi vale:", area)
print("\nL'area calcolata analiticamente vale:", area_analitica)
print("\nLa loro differenza vale:", area - area_analitica)