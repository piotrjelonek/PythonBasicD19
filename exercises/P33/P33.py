# V = SPK*(1 + p / m)**(n*m)
SPK = float(input("podaj kwotę:"))
p = int(input("podaj procent:"))/100
n = int(input("podaj czas trwania lokaty:"))
m = int(input("podaj ilość okresów kapitalizacji w roku"))

print("Twój stan konta w przyszłości: ",
      round(SPK * (1 + (p/m))**(n*m),2))
