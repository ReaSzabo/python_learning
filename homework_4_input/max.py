# coding: utf-8

# Kérj be egy számot a felhasználótól!
# Keresd meg és írd ki a tömb legnagyobb számát, ami kisebb mint a bekért szám.
# Pl. ha a bekért szám 17, akkor írd ki 16.

tomb = [1, 5, 10, 14, 16, 22, 25, 27]

legnagyobb = 0

bekertSzam = input("Adj meg egy számot: ")

for i in tomb:
    if i > legnagyobb and i < int(bekertSzam):
        legnagyobb = i

print(legnagyobb)