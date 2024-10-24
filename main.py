# # Esercizio 19
#
# # Stampa esercizio
# print("\nEsercizio 19\n")
#
# # Funzione per determinare l'ordinata fornita l'ascissa
# def calcola_ordinata(x):
#     y = 5 * x ** 3 + 4 * x ** 2 + 7 * x + 5
#     return y
#
# # Funzione integrale analitico
# def integrale_analitico(x):
#     return (5/4) * x**4 + (4/3) * x**3 + (7/2) * x**2 + 5 * x
#
# # Inserisco i tre valori
# a = float(input("Inserisci l'estremo inferiore dell'integrale: "))
# b = float(input("Inserisci l'estremo superiore dell'integrale: "))
# n = int(input("Inserisci il numero intero di suddivisioni da effettuare: "))
#
# # Inizializzo l'area
# area = 0
#
# # Determino la dimensione dell'intervallo
# dimensione_intervallo = (b - a) / n
#
# # Inizializzo gli estremi dell'intervallo
# estremo_inferiore = a
# estremo_superiore = a + dimensione_intervallo
#
# for i in range(n):
#     # Calcolo la dimensione delle due basi
#     y_inferiore = calcola_ordinata(estremo_inferiore)
#     y_superiore = calcola_ordinata(estremo_superiore)
#
#     # Calcolo il valore dell'area -> Area = base maggiore + base minore * altezza / 2
#     area += ((y_superiore + y_inferiore) * dimensione_intervallo) / 2
#
#     # Aggiorno gli estremi
#     estremo_inferiore = estremo_superiore
#     estremo_superiore += dimensione_intervallo
#
# # Calcolo analiticamente l'area dell'integrale
# area_analitica = integrale_analitico(b) - integrale_analitico(a)
#
# print("\nL'area calcolata approssimando attraverso il metodo dei trapezi vale:", area)
# print("\nL'area calcolata analiticamente vale:", area_analitica)
# print("\nLa loro differenza vale:", area - area_analitica)


# # Esercizio 18
#
# # Stampa esercizio
# print("\nEsercizio 18\n")
#
# # Inserisco i due valori
# m = int(input("Inserisci il primo numero intero positivo: "))
# n = int(input("Inserisci il secondo numero intero positivo: "))
#
# resto = 1 # Inizializzo il resto
#
# temp_n = n # Inizializzo la variabile temporanea
# temp_m = m # Inizializzo la variabile temporanea
#
# while resto != 0:
#     resto = max(temp_m, temp_n) % min(temp_m, temp_n)
#     if resto == 0:
#         break
#     else:
#         temp_m = temp_n
#         temp_n = resto
#
# print("\nIl massimo comune divisore tra " + str(m) + " e " + str(n) + " vale:", temp_n)



# # Esercizio 17
#
# # Stampa esercizio
# print("\nEsercizio 17\n")
#
# potenza = 0 # Inizializzo potenza a zero
# numero_di_cifre = 0 # Inizializzo counter a zero
#
# # Inserisco il valore
# while True:
#     numero = int(input("Inserisci un numero intero positivo: "))
#     if numero <= 0:
#         print("\nErrore, il numero deve essere maggiore di zero.\n")
#     else:
#         break
#
# # Inserisci la base
# while True:
#     base = int(input("Inserisci un numero intero maggiore di uno: "))
#     if base <= 1:
#         print("\nErrore, il numero deve essere maggiore di uno.\n")
#     else:
#         break
#
# while numero >= potenza:
#     potenza = base ** numero_di_cifre
#     numero_di_cifre += 1
#
# numero_di_cifre -= 1
# potenza = base ** (numero_di_cifre - 1) # Inizializzo al valore corretto la potenza
# numero_convertito = '' # Inizializzo una stringa vuota
#
# temp = numero # Copio il valore di numero nella variabile temporanea temp
#
# # Conversione in binario
# for i in range(numero_di_cifre):
#     if temp >= potenza:
#         numero_convertito += '1'
#         temp -= potenza  # Sottraggo il valore della potenza
#     else:
#         numero_convertito += '0'
#
#     potenza //= base  # Passo alla potenza successiva
#
# # Stampo il risultato
# print("La conversione in base " + str(base) + " del numero " + str(numero) + " è " + numero_convertito)



# # Esercizio 16
#
# # Stampa esercizio
# print("\nEsercizio 16\n")
#
# potenza = 0 # Inizializzo potenza a zero
# numero_di_cifre = 0 # Inizializzo counter a zero
# base = 2 # Impongo a base binaria
#
# # Inserisco il valore
# while True:
#     numero = int(input("Inserisci un numero intero positivo: "))
#     if numero <= 0:
#         print("\nErrore, il numero deve essere maggiore di zero.\n")
#     else:
#         break
#
# while numero >= potenza:
#     potenza = base ** numero_di_cifre
#     numero_di_cifre += 1
#
# numero_di_cifre -= 1
# potenza = base ** (numero_di_cifre - 1) # Inizializzo al valore corretto la potenza
# numero_convertito = '' # Inizializzo una stringa vuota
#
# temp = numero # Copio il valore di numero nella variabile temporanea temp
#
# # Conversione in binario
# for i in range(numero_di_cifre):
#     if temp >= potenza:
#         numero_convertito += '1'
#         temp -= potenza  # Sottraggo il valore della potenza
#     else:
#         numero_convertito += '0'
#
#     potenza //= base  # Passo alla potenza successiva
#
# # Stampo il risultato
# print("La conversione binaria del numero " + str(numero) + " è " + numero_convertito)



# # Esercizio 15
#
# # Stampa esercizio
# print("\nEsercizio 15\n")
#
# # Inserisco i tre valori
# a = float(input("Coefficiente a: "))
# b = float(input("Coefficiente b: "))
# c = float(input("Coefficiente c: "))
#
# # Calcolo il delta
# delta = (b**2 - 4 * a * c)
#
# print() # Riga vuota
#
# # Calcolo e stampo le soluzioni
# if delta >= 0:
#     soluzione_1 = ((-b + delta**0.5) / (2 * a))
#     soluzione_2 =((-b - delta**0.5) / (2 * a))
#
#     # Stampo le soluzioni:
#     print("Soluzione 1: ", soluzione_1)
#     print("Soluzione 2: ", soluzione_2)
# else:
#     print("L'equazione non ammette soluzioni reali")



# # Esercizio 14
#
# # Stampa esercizio
# print("\nEsercizio 14\n")
#
# # Inserisco il valore
# while True:
#     numero = float(input("Inserisci un numero: "))
#     if numero <= 1:
#         print("\nErrore, il numero deve essere maggiore di uno.\n")
#     else:
#         break
#
# primo = True # Inizializzo un flag booleano
#
# # Controllo se il numero è primo
# for i in range(2, int(numero**0.5) + 1):
#     if numero % i == 0:
#         primo = False
#
# print() # Riga vuota
#
# if primo:
#     print("1")
# else:
#     print("0")



# # Esercizio 13
#
# # Stampa esercizio
# print("\nEsercizio 13\n")
#
# # Inizializzo una lista
# numeri = []
#
# # Inserisco i valori
# while True:
#     numero = float(input("Inserisci un numero - 0.0 per terminare l'inserimento\nNumero: "))
#     if numero != 0.0:
#         numeri.append(numero)
#     else:
#         break
#
# ordinati_crescenti = True # Inizializzo un flag booleano
# ordinati_decrescenti = True # Inizializzo un flag booleano
#
# # Controllo se sono in ordine crescente
# for i in range(len(numeri) - 1):
#     if numeri[i] > numeri[i+1]:
#         ordinati_crescenti = False
#         break
#
# # Controllo se sono in ordine decrescente
# for i in range(len(numeri) - 1):
#     if numeri[i] < numeri[i+1]:
#         ordinati_decrescenti = False
#         break
#
# print() # Riga vuota
#
# if ordinati_crescenti:
#     print("Ordinata crescente")
# elif ordinati_decrescenti:
#     print("Ordinata decrescente")
# else:
#     print("Non ordinata")



# # Esercizio 12
#
# # Stampa esercizio
# print("\nEsercizio 12\n")
#
# # Inizializzo una lista
# numeri = []
#
# # Inserisco i valori
# while True:
#     numero = float(input("Inserisci un numero - 0.0 per terminare l'inserimento\nNumero: "))
#     if numero != 0.0:
#         numeri.append(numero)
#     else:
#         break
#
# ordinati = True # Inizializzo un flag booleano
#
# for i in range(len(numeri) - 1):
#     if numeri[i] > numeri[i+1]:
#         ordinati = False
#         break
#
# print() # Riga vuota
#
# if ordinati:
#     print("Ordinata crescente")
# else:
#     print("Non ordinata")



# # Esercizio 11
#
# # Stampa esercizio
# print("\nEsercizio 11\n")
#
# # Inizializzo una lista
# numeri = []
#
# k = int(input("Inserisci il valore k: "))
#
# print() # Riga vuota
#
# for i in range(k):
#     numero = int(input("Inserisci un numero: "))
#     numeri.append(numero)
#
# if 0 in numeri:
#     print("\nZero contenuto nella sequenza")
# else:
#     print("\nZero non contenuto nella sequenza")



# # Esercizio 10
#
# # Stampa esercizio
# print("\nEsercizio 10\n")
#
# # Inizializzo n ed m a zero
# n = -1
# m = -1
#
# # Inizializzo il valore di potenza
# potenza = 0
#
# # Inserisco il numero n
# while n <= 0:
#     # Inserisco il valore di n
#     n = int(input("Inserisci un numero intero maggiore di zero: "))
#
#     # Stampo il messaggio di errore
#     if n <= 0:
#         print("\nErrore, il numero deve essere maggiore di zero.\n")
#
# # Inserisco il numero m
# while m <= 0:
#     # Inserisco il valore di m
#     m = int(input("Inserisci un numero intero maggiore di zero: "))
#
#     # Stampo il messaggio di errore
#     if m <= 0:
#         print("\nErrore, il numero deve essere maggiore di zero.\n")
#
# potenza = n # Inizializzo la variabile potenza
#
# # Calcolo il prodotto
# for i in range(m-1):
#     potenza *= n
#
# print() # Riga vuota
#
# # Stampo il risultato
# print("Il resto della potenza " + str(n) + "**" + str(m) + " vale: " + str(potenza))



# # Esercizio 9
#
# # Stampa esercizio
# print("\nEsercizio 9\n")
#
# # Inizializzo n ed m a zero
# n = -1
# m = -1
#
# # Inizializzo il contatore e il resto a zero
# counter = 0
# resto = 0
#
# # Inserisco il numero n
# while n < 0:
#     # Inserisco il valore di n
#     n = int(input("Inserisci un numero intero maggiore o uguale a zero: "))
#
#     # Stampo il messaggio di errore
#     if n < 0:
#         print("\nErrore, il numero deve essere maggiore o uguale a zero.\n")
#
# # Inserisco il numero m
# while m <= 0:
#     # Inserisco il valore di m
#     m = int(input("Inserisci un numero intero maggiore di zero: "))
#
#     # Stampo il messaggio di errore
#     if m <= 0:
#         print("\nErrore, il numero deve essere maggiore di zero.\n")
#
# risultato = n # Inizializzo prodotto
#
# # Calcolo il prodotto
# while risultato >= 0:
#     risultato -= m
#     counter += 1
#
# counter -= 1
#
# print() # Riga vuota
#
# risultato = n # Inizializzo nuovamente prodotto
#
# for i in range(counter):
#     risultato -= m
#     resto = risultato
#
# # Stampo il risultato
# print("Il resto della divisione tra " + str(n) + " e " + str(m) + " vale: " + str(resto))



# # Esercizio 8
#
# # Stampa esercizio
# print("\nEsercizio 8\n")
#
# # Inizializzo n ed m a zero
# n = -1
# m = -1
#
# #Inizializzo il contatore a zero
# counter = 0
#
# # Inserisco il numero n
# while n < 0:
#     # Inserisco il valore di n
#     n = int(input("Inserisci un numero intero maggiore o uguale a zero: "))
#
#     # Stampo il messaggio di errore
#     if n < 0:
#         print("\nErrore, il numero deve essere maggiore o uguale a zero.\n")
#
# # Inserisco il numero m
# while m <= 0:
#     # Inserisco il valore di m
#     m = int(input("Inserisci un numero intero maggiore di zero: "))
#
#     # Stampo il messaggio di errore
#     if m <= 0:
#         print("\nErrore, il numero deve essere maggiore di zero.\n")
#
# risultato = n # Inizializzo prodotto
#
# # Calcolo il prodotto
# while risultato >= 0:
#     risultato -= m
#     counter += 1
#
# counter -= 1
#
# print() # Riga vuota
#
# # Stampo il risultato
# print("Il divisione intera tra " + str(n) + " e " + str(m) + " vale: " + str(counter))



# # Esercizio 7
#
# # Stampa esercizio
# print("\nEsercizio 7\n")
#
# # Inizializzo n ed m a zero
# n = 0
# m = 0
#
# # Inserisco il numero n
# while n <= 0:
#     # Inserisco il valore di n
#     n = int(input("Inserisci un numero intero maggiore di zero: "))
#
#     # Stampo il messaggio di errore
#     if n <= 0:
#         print("\nErrore, il numero deve essere maggiore di zero.\n")
#
# # Inserisco il numero m
# while m <= 0:
#     # Inserisco il valore di m
#     m = int(input("Inserisci un numero intero maggiore di zero: "))
#
#     # Stampo il messaggio di errore
#     if m <= 0:
#         print("\nErrore, il numero deve essere maggiore di zero.\n")
#
# prodotto = n # Inizializzo prodotto
#
# # Calcolo il prodotto
# for i in range(m-1):
#     prodotto += n
#
# print() # Riga vuota
#
# # Stampo il risultato
# print("Il prodotto tra " + str(n) + " e " + str(m) + " vale: " + str(prodotto))



# # Esercizio 6
#
# # Stampa esercizio
# print("\nEsercizio 6\n")
#
# # Funzione per calcolare il fattoriale
# def fattoriale(n):
#     risultato = 1
#     for i in range(n, 0, -1):
#         risultato *= i
#     return risultato
#
# # Inizializzo n a zero
# n = 0
#
# # Inserisco il numero
# while n <= 0:
#     # Inserisco il valore di n
#     n = int(input("Inserisci un numero intero maggiore di zero: "))
#
#     # Stampo il messaggio di errore
#     if n <= 0:
#         print("\nErrore, il numero deve essere maggiore di zero.\n")
#
#     # Stampo il risultato
#     else:
#         print("\n" + str(n) + "! vale: " + str(fattoriale(n)))



# # Esercizio 5
#
# # Stampa esercizio
# print("\nEsercizio 5\n")
#
# # Funzione per calcolare la somma dei numeri dispari nell'intervallo (0, n)
# def somma_numeri_dispari(n):
#     somma = 0
#     for i in range(n):
#         if i % 2 != 0:
#             somma += i
#     if n % 2 != 0:
#         somma += n
#     return somma
#
# # Inizializzo n a zero
# n = 0
#
# # Inserisco il numero
# while n <= 0:
#     # Inserisco il valore di n
#     n = int(input("Inserisci un numero intero maggiore di zero: "))
#
#     # Stampo il messaggio di errore
#     if n <= 0:
#         print("\nErrore, il numero deve essere maggiore di zero.\n")
#
#     # Stampo il risultato
#     else:
#         print("\nLa somma dei numeri dispari che vanno da 0 a " + str(n) + " vale: " + str(somma_numeri_dispari(n)))



# # Esercizio 4
#
# # Stampa esercizio
# print("\nEsercizio 4\n")
#
# # Inizializzazione
# massimo = float('-inf')
# minimo = float('inf')
# somma = 0
#
# # Inserisco i tre valori
# while True:
#     numero = float(input("Inserisci un numero: "))
#     if numero != 0.0:
#         somma += numero
#         if numero > massimo:
#             massimo = numero
#         if numero < minimo:
#             minimo = numero
#     else:
#         break
#
# print() # Riga vuota
#
# # Stampo i risultati
# print("Il massimo vale:", massimo)
# print("Il minimo vale:", minimo)
# print("La somma vale:", somma)



# # Esercizio 3
#
# # Stampa esercizio
# print("\nEsercizio 3\n")
#
# # Inizializzazione
# massimo = float('-inf')
# minimo = float('inf')
# somma = 0
#
# # Inserisco i tre valori
# for i in range(20):
#     numero = float(input("Inserisci un numero: "))
#     somma += numero
#     if numero > massimo:
#         massimo = numero
#     if numero < minimo:
#         minimo = numero
#
# print() # Riga vuota
#
# # Stampo i risultati
# print("Il massimo vale:", massimo)
# print("Il minimo vale:", minimo)
# print("La somma vale:", somma)



# # Esercizio 2
#
# # Stampa esercizio
# print("\nEsercizio 2\n")
#
# # Inserisco i tre valori
# numero_1 = float(input("Inserisci il primo numero: "))
# numero_2 = float(input("Inserisci il secondo numero: "))
# numero_3 = float(input("Inserisci il terzo numero: "))
#
# print() # Riga vuota
#
# # Calcolo massimo minimo e somma
# massimo = max(numero_1, numero_2, numero_3)
# minimo = min(numero_1, numero_2, numero_3)
# somma = numero_1 + numero_2 + numero_3
#
# # Stampo i risultati
# print("Il massimo vale:", massimo)
# print("Il minimo vale:", minimo)
# print("La somma vale:", somma)



# # Esercizio 1
#
# # Stampa esercizio
# print("\nEsercizio 1\n")
#
# def print_triangular_numbers(n):
#     # Inizializzazione
#     triangolari = [] # Inizializzo una lista
#     b = 0 # Inizializzo il secondo valore
#
#     for i in range(1, n + 1):
#         triangolari.append(i) # Aggiungo il parametro inferiore alla serie di Fibonacci
#         b += i # Aggiorno il secondo parametro
#         triangolari.append(b) # Aggiungo il parametro inferiore alla serie di Fibonacci
#
#     # Restituisco la serie
#     return triangolari
#
# n = 0 # Inizializzo il valore di n
#
# while n <= 0:
#     # Inserisco il valore di n
#     n = int(input("Inserisci un numero intero maggiore di zero: "))
#
#     # Stampo il messaggio di errore
#     if n <= 0:
#         print("\nErrore, il numero deve essere maggiore di zero.\n")
#
#     # Stampo il risultato
#     else:
#         print("\nI primi " + str(n) + " numeri triangolari sono:\n")
#         triangolari = print_triangular_numbers(n)
#         for i in range(0, 2 * n, 2):
#             print(str(triangolari[i]) + str("\t") + str(triangolari[i + 1]))



# # Esercizio 1.7 La successione di Fibonacci
#
# # Stampa esercizio
# print("\nEsercizio 1.7 La successione di Fibonacci\n")
#
# def fibonacci(n):
#
#     # Inizializzazione
#     serie_di_fibonacci = [] # Inizializzo una lista
#     a = 1 # Inizializzo il primo valore
#     b = 1 # Inizializzo il secondo valore
#
#     for _ in range(n):
#         serie_di_fibonacci.append(a) # Aggiungo il parametro inferiore alla serie di Fibonacci
#
#         c = a + b # Calcolo il nuovo secondo parametro
#         a = b # Aggiorno il primo parametro
#         b = c # Aggiorno il secondo parametro
#
#     # Restituisco la serie
#     return serie_di_fibonacci
#
# n = 0 # Inizializzo il valore di n
#
# while n <= 0:
#     # Inserisco il valore di n
#     n = int(input("Inserisci un numero intero maggiore di zero: "))
#
#     # Stampo il messaggio di errore
#     if n <= 0:
#         print("\nErrore, il numero deve essere maggiore di zero.\n")
#
#     # Stampo il risultato
#     else:
#         print("\nI primi " + str(n) + " numeri della serie di Fibonacci sono: " + str(fibonacci(n)))



# # Esercizio 1.6 Spostamenti casuali
#
# # Stampa esercizio
# print("\nEsercizio 1.6 Spostamenti casuali\n")
#
# import turtle
# import random
#
# dimensione_spostamento = 5 # Imposto lo spostamento a 5 pixel
#
# def muovi(movimenti):
#     for _ in range(movimenti):
#         turtle.forward(dimensione_spostamento)  # Mi muovo di 5 pixel
#         angolo = random.randint(-30, 30)  # restituisco un angolo casuale compreso tra -30° e 30°
#         turtle.right(angolo)  # Ruoto dell'angolo randomico calcolato
#
# # Inserimento numero di mosse
# numero_movimenti = int(input("Inserisci il numero di movimenti che verranno svolti dalla tartaruga: "))
#
# turtle.speed(3) # Imposto la velocità di disegno ad 3
# turtle.pensize(3) # Imposto lo spessore del tratto ad 3
# turtle.pencolor("red") # Imposto il colore a rosso
# turtle.showturtle # Mostro la tartaruga durante il disegno
#
# # Eseguo le mosse
# muovi(numero_movimenti)
#
# # Concludo il disegno
# turtle.done()



# # Esercizio 1.5 Sono tutti divisibili per 3 o per 2?
#
# # Stampa esercizio
# print("\nEsercizio 1.5 Sono tutti divisibili per 3 o per 2?\n")
#
# numeri = [] # Inizializzo una lista
# divisibile = True # Inizializzo un flag booleano
#
# while True:
#     numero = int(input("Inserisci un numero, -1 per terminare l'inserimento\nNumero: "))
#
#     # Effettuo un controllo per verificare la terminazione dell'inserimento
#     if numero != -1:
#         numeri.append(numero) # Aggiungo il numero in lista
#     else:
#         break
#
# print() # Riga vuota
#
# for value in numeri:
#     # Verifico la divisibilità per 2 o per 3
#     if not(((value % 2) == 0) or ((value % 3) == 0)):
#         divisibile = False # Se non dovesse essere divisibile
#         break
#
# # Se non divisibile
# if not divisibile:
#     print("NO")
#
# # Se divisibile
# else:
#     print("OK)



# # Esercizio 1.4 Somma di una sequenza
#
# # Stampa esercizio
# print("\nEsercizio 1.4 Somma di una sequenza\n")
#
# somma = 0 # Inizializzo una variabile
#
# # Ciclo infinito
# while True:
#     # Inserisco valori interi
#     numero = int(input("Inserisci un numero, -1 per terminare l'inserimento\nNumero: "))
#
#     # Effettuo un controllo per verificare la terminazione dell'inserimento
#     if numero != -1:
#         somma += numero
#     else:
#         break
#
# print() # Riga vuota
#
# # Stampo il risultato
# print("La somma dei valori inseriti vale: " + str(somma))



# # Esercizio 1.3 Massimo fra tre
#
# # Stampa esercizio
# print("\nEsercizio 1.3 Massimo fra tre\n")
#
# NUMERO_VALORI = 3 # Inizializzo il numero di valori
# numeri = []  # Inizializzo una lista vuota
#
# for i in range(NUMERO_VALORI):
#     # Inserisco da tastiera un numero decimale e lo aggiungo alla lista
#     numeri.append(float(input("Inserisci un numero: ")))
#
# print() # Riga vuota
#
# # Stampo il risultato
# print("Il massimo tra i numeri inseriti vale: " + str(max(numeri)))
