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
# elements = []
# flag = True
# while(flag):
#     elem  = input("podaj wartość lub wprowadź Q zeby wyjść")
#     if(elem.upper() == "Q"):
#         print("wyjście")
#         flag = not flag
#         continue
#     elements.append(elem)
# else:
#     print(elements)

# Dana jest lista wartości
a = [0.3, 0.4, 3.2, 0.31, 1, 5.4, 2, 1, 17, 7]
# Napisz program filtrujący wartości po zadanym przez użytkownika progu
# tj. w tablicy wynikowej pojawiają się tylko wartości większe od treshold
tresholdLow = float(input("podaj próg odcięcia dolny"))
tresholdTop = float(input("podaj próg odcięcia górny"))
categorizedResult = []
class0 = []     # lista przechowująca wartości skalsyfikowane jako 0
class1 = []     # lista przechowująca wartości skalsyfikowane jako 1
labelsDict = {0 : class0, 1 : class1}
index = 0
while(index < len(a)):
    if(a[index] > tresholdLow and a[index] < tresholdTop):
        categorizedResult.append(1)
        class1.append(a[index])
    else:
        categorizedResult.append(0)
        class0.append(a[index])
    index += 1

print(a)
print(categorizedResult)
print(labelsDict)







