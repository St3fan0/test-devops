print("- - - - - - - Istograms - - - - - - - - ")
print("- - - - - - - - - - - - - - - - - - - - ")

def convertIstogram(value):
    """
    istogram = "*"
    for x in range(value-1):
        istogram = istogram + "*"
        """
    print(str(value) + " = " + ("*" * value)  )


def convertitore():
    values = []
    while input("vuoi inserire un numero? S/N ") == "S":
        try:
           values.append( int( input("numero: ") ) )
        except ValueError as e:
            print("Hai inserito un numero? ",  e)
        finally:
            print("numero acquisito")
    for x in range(len(values)):
        print(str(x) + " = " + ("*" * x)  )
       # convertIstogram(values[x])
   
convertitore()
