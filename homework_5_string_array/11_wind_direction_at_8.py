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
    ["Debrecen", "0800", "kelet"],
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

# Vizsgáld meg (számlálókkal), hogy déli vagy keleti szél bejegyzés volt több 08:00-kor!

deliSzel = 0
keletiSzel = 0

for i in rains:
    if str(i[2]) == "dél":
        deliSzel = int(deliSzel) + 1
    if str(i[2]) == "kelet":
        keletiSzel = int(keletiSzel) + 1


if int(deliSzel) > int(keletiSzel):
    print("Több déli szél volt, mint keleti. Déli szelek száma: " + str(deliSzel) + ", Keleti szelek száma: " + str(keletiSzel))
else:
    print("Több keleti szél volt, mint déli. Keleti szelek száma: " + str(keletiSzel) + ", Déli szelek száma: " + str(deliSzel))