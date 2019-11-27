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

