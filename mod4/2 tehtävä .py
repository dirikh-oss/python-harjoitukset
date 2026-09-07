luvut = []
while True:
    syote = input("Anna luku (tyhjä lopettaa): ")
    if syote == "":
        break
    luvut.append(float(syote))
    luvut.sort(reverse=True)
viisi_suurinta = luvut[:5]

print("Viisi suurinta lukua suurimmasta alkaen:")
for luku in viisi_suurinta:
    print(luku)