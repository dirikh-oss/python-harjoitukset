pienin = suurin = None

while (syote := input("Anna luku (tyhjä lopettaa): ")) != "":
    luku = float(syote)
    pienin = luku if pienin is None else min(pienin, luku)
    suurin = luku if suurin is None else max(suurin, luku)

if pienin is not None:
    print(f"Pienin: {pienin}\nSuurin: {suurin}")
else:
    print("Et antanut lukuja.")