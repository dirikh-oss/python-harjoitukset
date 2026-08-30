leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))
kaikki_luodit = (leiviskat * 20 * 32) + (naulat * 32) + luodit
kokonais_grammat = kaikki_luodit * 13.3
kg = int(kokonais_grammat // 1000)
g = kokonais_grammat % 1000
print(f"Massa on {kg} kg ja {g:.2f} g.")