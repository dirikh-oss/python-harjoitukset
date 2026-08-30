sp = input("Sukupuoli (nainen/mies): ")
hb = float(input("Hemoglobiiniarvo (g/l): "))
if sp == "nainen":
    if hb < 117:
        print("Alhainen")
    elif hb <= 175:
        print("Normaali")
    else:
        print("Korkea")
elif sp == "mies":
    if hb < 134:
        print("Alhainen")
    elif hb <= 195:
        print("Normaali")
    else:  print("Korkea")
else:
     print("Virheellinen sukupuoli.")