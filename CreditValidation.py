ccnum = input("Please enter a number ")


def CreditCardValidator(ccnum) :
    Reversenumber = []
    for i in range(0, len(ccnum)):
            Reversenumber.append(ccnum[i])
            Reversenumber.reverse()
    print("  "+str(Reversenumber[1]))

CreditCardValidator(ccnum)