"""
Scrivere un programma che legga 3 stringhe e le ordini in senso lessicografico
"""

stringa1 = input("Prima stringa: ")
stringa2 = input("Seconda stinga: ")
stringa3 = input("Terza stringa: ")

if stringa1 > stringa2:
    if stringa2 > stringa3:
        print("No swap needed")
    else:
        if stringa1 < stringa3:
            print("Swap stringa1 and stringa3, stringa1 and stinga2")
            stringa1, stringa2, stringa3 = stringa3, stringa1, stringa2
            #stringa3 - stringa1 - stringa2
        else:
            print("swap stringa2 and stringa3")
            stringa2, stringa3 = stringa3, stringa2
            #string1 - stringa3 - stringa2
else:
    if stringa2 > stringa3:
        if stringa3 > stringa1:
            print("swap stringa1 and stringa3, stringa2 and stringa1")
            stringa1, stringa2, stringa3 = stringa2, stringa3, stringa1
            #stringa2 - stringa3 - stringa1
        else:
            print("swap stringa1 and stringa2")
            stringa1, stringa2= stringa2, stringa1
            #stringa2 - stringa1 - stringa3
    else:
        print("swap stringa3 and stringa1")
        stringa1, stringa3 = stringa3, stringa1
        #stringa3 - stringa2 - stringa1
print(f"{stringa1} \n{stringa2} \n{stringa3}")