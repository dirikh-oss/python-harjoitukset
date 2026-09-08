import random

def heita_noppaa(tahkot):
    return random.randint(1, tahkot)

tahkot = int(input("Anna nopan tahkojen määrä: "))

noppa = 20

while noppa != tahkot:
    noppa = heita_noppaa(tahkot)
    print("Nopan silmäluku:", noppa)