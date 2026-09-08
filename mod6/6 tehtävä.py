import math
def yksikkohinta(halkaisija, hinta):
    sade = halkaisija / 2 / 100
    pinta_ala = math.pi * sade ** 2
    return hinta / pinta_ala

halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija cm: "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta €: "))

halkaisija2 = float(input("Anna toisen pizzan halkaisija cm: "))
hinta2 = float(input("Anna toisen pizzan hinta €: "))

yksikkohinta1 = yksikkohinta(halkaisija1, hinta1)
yksikkohinta2 = yksikkohinta(halkaisija2, hinta2)
print("Pizza 1 yksikköhinta:", yksikkohinta1, "€/m²")
print("Pizza 2 yksikköhinta:", yksikkohinta2, "€/m²")
if yksikkohinta1 < yksikkohinta2:
    print("Pizza 1 antaa paremman vastineen rahalle.")
else:
    print("Pizza 2 antaa paremman vastineen rahalle.")