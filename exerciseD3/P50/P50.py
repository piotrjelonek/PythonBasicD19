# słownik id -> lista cech
products = {"1" : ["A", 3.5, 10],
            "2" : ["B", 2.99, 5],
            "3" : ["C", 9.99, 1]}
# koszyk zawiera listy zamówionych produktów
basket = []
# CLI użytkownika
while(True):
    # pętla wypisująca produkty
    for key in products.keys():
        print(key, products[key])
    # pobieranie danych od użytkownika
    choice = input("Co chcesz zamówić podaj id produktu lub Q-wyjście")
    # wyjście z programu
    if(choice.upper() == "Q"):
        break