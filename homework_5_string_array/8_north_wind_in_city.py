# coding: utf-8

# Egy tömbben adatokat tárolunk.
# A tömbünkben tömbök vannak.
# A kicsi tömböknek három eleme van.
# Az első egy város kódja, a második pedig a nap egy időpontja, amikor esett az eső.
# Az időpontok egy négyszámjegyes formátumban szerepelnek, amik az órát és percet jelentik.
# Pl "1812" -> 18:12 (18 óraa 12 perc).
# A harmadik elem pedig a szél iránya.
# Ha a szél iránya helyén a "NA" szerepel, akkor nem fújt a szél.

rains = [
    ["Budapest", "0800", "kelet"],
    ["Budapest", "0820", "észak"],
    ["Budapest", "1000", "kelet"],
    ["Budapest", "1230", "nyugat"],
    ["Budapest", "1730", "kelet"],
    ["Budapest", "1920", "nyugat"],
    ["Debrecen", "0800", "dél"],
    ["Debrecen", "0920", "észak"],
    ["Debrecen", "1020", "nyugat"],
    ["Debrecen", "1115", "kelet"],
    ["Debrecen", "1900", "dél"],
    ["Szeged", "0600", "észak"],
    ["Szeged", "0700", "kelet"],
    ["Szeged", "0800", "dél"],
    ["Miskolc", "0800", "kelet"],
    ["Miskolc", "0920", "észak"],
]

# Kérj be egy várost a felhasználótól!
# Ha volt északi szél a városban, akkor írd ki: "Volt északi szél ekkor: 08:20"

bekert = input("Adj meg egy várost: ")
for i in rains:
    if str(i[0]) == str(bekert):
        if str(i[2]) == "észak":
            ido = i[1]
            print("Volt északi szel a városban ekkor: " + ido[0] + ido[1] + ":" + ido[2] + ido[3])
