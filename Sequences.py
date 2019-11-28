sentence = "Ala ma kota, a kot ma Ale."
# oczyść zdanie ze znaków interpunkcyjnych
sentence = sentence.replace(",","")
sentence = sentence.replace(".","")
print(sentence)
# zapisz wsyztkie słowa w zdaniu w liście words
words = sentence.split(" ")
print(words)

# listy
params = []
row = [1, "Adam", "Nowak", "2000-01-01", True, 5500.]

# dodawanie parametrów do parms
params.append(12.5)
params.append(11.5)
params.append(9.4)
# wypisanie elementów listy
print(params)
print(row)
# zmiana pensji w liście row
row[5] = 6000.
print(row)
print(row[1:3])
#  odczyt elementów z krokiem 2
print(row[0:5:2])
print(row[1:])
print(row[:3])
# odwrotna kolejność
print(row[::-1])
# Powielanie list
row = row * 2
print(row)
# row *= 0        # row = row * 0
print(row)
# długośc listy
print(len(row))
# row[1] = "abc"
row[6:] = [2, "Jan","Kowalski","2011-02-12",False, 10000]
print(row)

a = ["a",1, True]
b = ["a", "xyz", 15.3]
print(b[1] == a[0:2])

# operator przynależności
print("Kowalski" in row)
print("Kowalski" not in row)


name = "Michał"
# name[3] = 'k'         NIEZMIENNY
# konwersja na listę
name = list(name)       # EDYTOWALNY
name[3] = 'k'
print(name)
string = ""
for v in name:
    string += str(v);
print(string)           # NIEZMIENNY
# string[2] = 'a'

print(name)
name = str(name)
name = name.replace("'","")
name = name.replace(", ","")
name = name.replace("]","")
name = name.replace("[","")
print(name)

numbers = [1,2,3,4,5]
numbers.remove(numbers[3])      # usuwanie po wartości bez zwracania
print(numbers)
deleted = numbers.pop(2)        # usuwanie po indeksie ze zwracaniem wartości
print(numbers)
print(deleted)

# sprawdź czy dwa napisy są palindromami
# sprawdź czy dwie liczby są lustrzane
# I SPOSÓB
text = "kajak"
print(text[ : ] == text[ : :-1])
# II SPOSÓB
text = list(text)
textRev = text
textRev.reverse()
print(text == textRev)

# sortowanie
nums = [1.1, 2.1, 0.15, 15., 1., 4., 1]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)
names = ["Ala","Ola","Ela"]
names.sort()
print(names)

kik =   [
            ["_","_","_"],
            ["_","_","_","_"],
            ["_","_","_","_","_"]
        ]
print(kik)
print("lista zewnętrzna", len(kik))
print("pierwszy wiersz", len(kik[0]))
print("drugi wiersz", len(kik[1]))
print("trzeci wiersz", len(kik[2]))
kik[2][3] = "X"
print(kik)
kik[1][1:2] = ["O","O"]
print(kik)
