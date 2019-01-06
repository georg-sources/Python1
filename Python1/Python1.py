
def Hallo(Count, *pars):
    #Dies ist eine Funktion
    #print("Anzahl der Parameter ist " + str(Count))
    for par in pars:
        print(par)
    return Count

#Hallo(2,"Hallo","Test")
print(Hallo(2,"Hallo","Test"))