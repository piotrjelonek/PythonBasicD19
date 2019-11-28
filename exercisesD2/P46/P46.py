list = [4,5,3,2,1,6]
index = int(input("którą wartość chcesz ustawić: " + str(list))) - 1

if(index >= 0 and index < len(list)):
    print("Twój wybór:", list[index])
else:
    print("OUT OF RANGE")

# czy dwa pierwsze elementy listy są dodatnie
if(list[0] > 0 and list[1] > 0):
    print("dwa pierwsze elementy są dodatnie")
elif(list[0] > 0 and list[1] <= 0):
    print("tylko pierwszy leement jest dodatni")
elif(list[0] <= 0 and list[1] > 0):
    print("tylko drugi element jest dodatni")
else:
    print("oba elementy są ujemne")
# sprawdź czy wprowadzona liczba jest parzysta
print("Wprowadzona wartość jest: ", "parzysta" if (index % 2 == 0) else "nieparzysta" )
