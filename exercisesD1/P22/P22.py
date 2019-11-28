# 5500 PLN - 168 h
# x PLN    - 1 h
salaryNet = 5500
hours = 168
print("Stawka godzinowa netto: ", round(salaryNet / hours,2), "PLN/H" )
print("Stawka godzinowa brutto: ", round((1.23 * salaryNet) / hours,2), "PLN/H" )

collection = "Stawka godzinowa brutto: ", round((1.23 * salaryNet) / hours,2), "PLN/H"
text = "Stawka godzinowa brutto: " +  str(round((1.23 * salaryNet) / hours,2)) + "PLN/H"
print(collection)
print(text)