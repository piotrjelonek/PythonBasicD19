products = {}

id = 1
while(id <= 3):
    products[id] = [input("podaj nazwę produktu"),
                    int(input("podaj ilość ")),
                    float(input("podaj cenę netto"))]
    id += 1     # id = id + 1
print(products)