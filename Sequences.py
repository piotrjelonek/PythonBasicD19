sentence = "Ala ma kota, a kot ma Ale."
# oczyść zdanie ze znaków interpunkcyjnych
sentence = sentence.replace(",","")
sentence = sentence.replace(".","")
print(sentence)
# zapisz wsyztkie słowa w zdaniu w liście words
words = sentence.split(" ")
print(words)

