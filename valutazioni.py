import pytest
print("- - - - - - - Matematica - - - - - - - - ")
print("- - - - - - - Valutazioni - - - - - - - -")

def media(valutazioni):
   return str( sum( int(valutazioni[item]) for item in valutazioni )/len(valutazioni) )

def acquisisciValutazioni():
    values = {}
    while input("Inserisci una valutazione? S/N ") == "S":
        try:
           nome = input("Nome Alunno: ")
           values[ nome ] = input("Voto: ")
        except ValueError as e:
            print("Hai inserito un numero? ",  e)
        finally:
            print("valutazione acquisita")
    
    sortedPersons = dict(sorted(values.items(), key = lambda x:x[1], reverse=True))
    for x in sortedPersons.keys():
        print(x + " Voto " +sortedPersons[x]  )
    print("La media dei voti è: " + media(sortedPersons) )  # str( sum( int(sortedPersons[item]) for item in sortedPersons )/len(sortedPersons) ) )

    #print(sortedPersons)

acquisisciValutazioni()

## TEST CODE
def test_acquisisciValutazioni():
    assert media({'key1': 8,'key2': 3}) == 5.5
