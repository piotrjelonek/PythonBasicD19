# Z podanej daty urodzenia wydobywamy rok (YYYY-MM-DD)
# na podstawie obliczoneg wieku sprawdź czy użytkownik jest pełnoletni
# jeżeli age >= 18 to wypisz pełnoletni
# jeżeli age < 18 to wypisz niepełnoletni
# jeżeli wiek nie zawiera się w przediale od 0 do 120 to wypisz jesteś robotem
# dodatkowo zadbaj o walidację wprowadzonych danych
from datetime import date

# today = date.today()
# birthDate = input("wprowadź datę urodzenia YYYY-MM-DD")
# year = birthDate[:4]
# # sprawdzam czy rok jest liczbą
# if(year.isdecimal()):
#     # zrzutuj rok na int
#     validYear = int(year)
#     age = today.year - validYear
#     if(age >= 18 and age <= 120):
#         print("jesteś pełnoletni")
#     elif(age < 18 and age >= 0):
#         print("jesteś niepełnoletni")
#     else:
#         print("jesteś robotem")
# else:
#     print("niepoprawna data urodzenia")



# wykorzystując 3arg sprawdź czy wprowadzona wartość z klawiatury jest liczbą
# jeżeli tak wypisz tą liczbe
# jeżeli nie wypisz zero
toNumber = input("podaj liczbę")
number = int(toNumber) if toNumber.isdecimal() else 0
print("Wynik działania: ", number)


