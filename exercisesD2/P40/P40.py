decimalToRomanCoverter = {0:"0", 1:"I",2:"II",3:"III",4:"IV",5:"V"}

try:
    decNum = float(input("Podaj cyfrę w systemie dziesiętnym"))
    if (decNum >= 0 and decNum <= 5):
        print(decimalToRomanCoverter[int(decNum)])
    else:
        print("Spoza zakresu")
except:
    print("Błąd danych")


# if(decNum.isdecimal()):
#     decNum = int(decNum)
#     if(decNum >= 0 and decNum <= 5):
#         print(decimalToRomanCoverter[decNum])
#     else:
#         print("Liczba jest spoza zakresu 0 - 5")
# else:
#     print("Błędne dane")