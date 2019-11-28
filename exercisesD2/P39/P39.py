numberConverter = {"jeden" : 1, "dwa" : 2, "trzy" : 3, "cztery" : 4, "pięć" : 5}
userNumber = input("podaj cyfrę słownie (1-5)").lower()

if(userNumber in numberConverter):
    print(numberConverter[userNumber])
else:
    print("Podałeś błędny klucz")

