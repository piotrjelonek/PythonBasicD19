# słownik id -> lista cech
products = {"1" : ["A", 3.5, 10],
            "2" : ["B", 2.99, 5],
            "3" : ["C", 9.99, 1]}
# koszyk zawiera listy zamówionych produktów
basket = []
cumSum = 0
# CLI użytkownika
while(True):
    # pętla wypisująca produkty
    for key in products.keys():
        print(key, products[key])
    # pobieranie danych od użytkownika
    choice = input("Co chcesz zamówić podaj id produktu lub Q-wyjście")
    # wyjście z programu
    if(choice.upper() == "Q"):
        print("Wyjście")
        break
    # spr czy istnieje taki id
    if(choice not in products.keys()):
        print("Wie ma takiego produktu")
        continue
    quantity = float(input("Wprowadź ilość zamawianego produktu"))
    # sprawdzenie dostępności produktu
    if(quantity > products[choice][2] and quantity > 0):
        print("Dostępnych jest tylko: " + str(products[choice][2]) + "szt.")
        continue
    # aktualizacja magazynu i koszyka
    products[choice][2] -= quantity # products[choice][2] = products[choice][2] - quantity
    basket.append([products[choice][0],products[choice][1], quantity])
    # suma skumulowana zamówień w koszyku
    cumSum += quantity * products[choice][1]
    print("Twój koszyk:", basket)
    print("Suma do zapłaty:", cumSum, "zł")