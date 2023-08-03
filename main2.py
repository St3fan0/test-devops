#programma somma numeri
import funzioni

"""
print("- - - - - - - S O M M A - - - - - - - ")
print("- - - - - - - - - - - - - - - - - - - ")

def requestNumbers():
    values = []
    while len(values) < 2:
        values.append( input("Inserisci un valore: "))
    funzioni.somma(values[0], values[1])

requestNumbers()

if input("vuoi eseguire nuovamente? S/N ") == "S":
    requestNumbers()
"""
print("- - - - - - - Calcolatrice - - - - - - - ")
print("- - - - - - - - - - - - -  - - - - - - - ")

operations = ["+", "-", "x", ":"]

def calcolatrice():
    values = []
    while len(values) < 2:
        values.append( input("Inserisci un valore: "))
    print("Operazioni possibili:")
    for x in range(len(operations)):
        print(operations[x] ) 
    choice = input("Quale operazione vorresti eseguire? ") 
    if choice == "+":
        funzioni.somma(values[0], values[1])
    elif choice == "-":
        funzioni.differenza(values[0], values[1])
    elif choice == "x":
        funzioni.prodotto(values[0], values[1])
    elif choice == ":":
        funzioni.divisione(values[0], values[1])
    else:
        print("operazione non supportata")

while input("vuoi eseguire un operazione? S/N ") == "S":
    try:
        calcolatrice()
    except ValueError as e:
        print("Un errore! ",  e)
    finally:
        print("programma eseguito")