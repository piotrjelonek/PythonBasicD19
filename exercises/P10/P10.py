# baza danych
productNames = "Chleb", "Melko", "Cuksy"
productPrices = 1.99, 2.50, 12.99
productQuantity = "szt.", "l", "kg"

# zamówienie
productOrder = 2, 0.5, 0.3

# prezentacja zamówienia
print(productNames[0], productOrder[0], productQuantity[0], sep="\t\t")
print(productNames[1], productOrder[1], productQuantity[1], sep="\t\t")
print(productNames[2], productOrder[2], productQuantity[2], sep="\t\t")

# Kwota do zapłaty
print("SUMA",
      round(productPrices[0] * productOrder[0] +
            productPrices[1] * productOrder[1] +
            productPrices[2] * productOrder[2] ,2) ,"zł")

