name = input("Podaj imię: ")    # input zwraca stringa
lastName = input("Podaj nazwisko: ")    # input zwraca stringa
birthDate = input("Podaj datę urodzenia (YYYY-MM-DD): ")    # input zwraca stringa
possition = input("Podaj stanowisko")
salaryNet = float(input("Wprowadź wynagrodzenie netto"))       # konwersja string -> float

# print(name, lastName, birthDate, possition, str(salaryNet) + "zł", str(salaryNet * 1.23) + "zł", sep=' | ')

print("Pan " + name + " " + lastName + "(ur. " + birthDate + " )")
print("Wiek: " + str(2019 - int(birthDate[0:4])))
print("Stanowisko: " + possition)
print("Wynagrodzenie netto: " + str(round(salaryNet,2)) + "zł")
