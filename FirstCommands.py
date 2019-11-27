# CTRL + / -> komantarz jednowierszowy
'''
komentarz
wielo-
linijkowy
'''
print('Witaj w Pythonie')
# zmienne -> zeklaracja i przypisanie -> inicjalizacja zmiennej (obiektu)
text = "Witaj"
name = "Michał"
sign = 'a'
print(text + " " + name)

# zmienne na podstawie innych zmiennych
a = 1
b = a + 1
print(a, b, (a * b))
print(a, end=';')
print(b , end=';')
print(a + b, end='\n')      # \n - newline
print('www.xyz.pl\\all')    # \\ - '\'
print('www.xyz.pl\\\\all')  # \\ - '\'
print('"Cytat"')
print("I'm Michal")
print("\"Cytat\"")

# usuwanie obiektu z pamięci podręcznej
del(a)
# print(a) -> a is not defined

# typy zmiennych
name = "Michał"
salary = 10000.
isActivated = True
element = 1
print(type(name), type(salary), type(isActivated), type(element))


# liczby zespolone
complexNum1 = 2 + 2j
complexNum2 = 5j
realNum1 = 2

print(complexNum1 + complexNum2)
print(complexNum1 * realNum1)
print(type(complexNum1))

# operacje na liczbach
num1 = 1
num2 = 2

print(type(num1), type(num2), 1/2)
print(type(num1), type(num2), 1//2)

print(round(1.5,3))

# konwersja rozszerzająca i zawężającej
floatNum = 111.9999
floatNum = int(floatNum)    # konwersja zawężająca
print(floatNum)
intNum = 5
print(float(intNum))        # konwersja rozszerzająca