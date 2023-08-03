numero1 = int(input("inserisci un numero: "))
numero2 = int(input("inserisci un'altro numero: "))
numero3 = int(input("inserisci un'altro numero: "))

if numero1 > numero2 and numero1 > numero3:
    print("Il primo numero è il più grande: " + str(numero1) + " somma: " + str(numero1 + numero2 + numero3))
elif numero2 > numero1 and numero2 > numero3:
    print("Il secondo numero è il più grande: " + str(numero2) + " prodotto: " + str(numero1 * numero2 * numero3))
elif numero3 > numero1 and numero2 > numero1:
    print("Il terzo numero è il più grande: " + str(numero3) )
else:
    print("i numeri inseriti sono uguali " + str(numero1) + " " + str(numero1) + " " + str(numero3))
#print("La somma dei due numeri è " + str(numero1 + numero2))