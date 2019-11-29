for i in range(1,20,1):
    print("%2i | %4i" % (i, i**2))

name = "Michał"
age = 33.22222
print("Hello %s" % (name))
print("Hello " + name + " " +  str(age))
print("Hello %s %.2f" % (name, age))

numbers = [-1, 1, 1, -1 , -1]

for i in numbers:
    print("%+3i" % i)

signal = 101
print( "%08i" % signal)

row0 = [1, "Michał", "Kruczkowski", "2000-10-01", True]
row1 = [1, "Michał", "Kruczkowski", "2000-10-01", True]
row2 = [1, "Michał", "Kruczkowski", "2000-10-01", True]
table = [row0, row1, row2]

for row in table:
    print("| %2i | %-15s | %-15s | %15s | %5s |" %
          (row[0],row[1],row[2],row[3],row[4]))
