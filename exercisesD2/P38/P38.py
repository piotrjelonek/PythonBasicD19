dates = [(10,10,2019),(1,4,2020),(5,3,2020)]

while(True):
    inputDate = input("wprowadź datę w formacie (DD-MM-YYYY) lub Q-wyjdź")
    if(inputDate.upper()[0] == "Q"):
        break
    dates.append(tuple(inputDate.split("-")))

print(dates)
#
# print("Data ważności: " + str(dates[0][0]) + "-" + str(dates[0][1]) + "-" + str(dates[0][2]))
# print("Data ważności: " + str(dates[1][0]) + "-" + str(dates[1][1]) + "-" + str(dates[1][2]))
# print("Data ważności: " + str(dates[2][0]) + "-" + str(dates[2][1]) + "-" + str(dates[2][2]))
# print("Data ważności: " + str(dates[3][0]) + "-" + str(dates[3][1]) + "-" + str(dates[3][2]))