elements = range(5,50,1)
index = -1
while(True):
    index += 1
    if(index % 2 == 0):
        continue                    # pominiecie iteracji
    print(index, elements[index])
    if(index == 13):                # warunek przerwania
        break                       # przerwanie natychmiastowe wyjście z pętli


# Wprowadź dane z klawiatury do listy tak długo aż użytkownik wpisze Q
elements = []
flag = True
while(flag):
    elem  = input("podaj wartość lub wprowadź Q zeby wyjść")
    if(elem.upper() == "Q"):
        print("wyjście")
        flag = not flag
        continue
    elements.append(elem)
else:
    print(elements)







