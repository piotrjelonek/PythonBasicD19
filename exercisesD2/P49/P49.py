# PANEL LOGOWANIA
logs = { "user" : "user", "admin" : "admin"}
login = input("podaj login")
password = input("podaj hasło")

if(login not in logs.keys()):       # błędny login
    print("błędny login")
elif(logs[login] == password):      # poprawne logowanie
    print("zalogowano")
else:
    print("błędne hasło")           # błędne hasło

