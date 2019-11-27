try:
    number = input("Podaj liczbę")
    result = float(number)  # miejsce w którym może wystąpić błąd
except:
    result = float(len(number))

print(type(result), result)