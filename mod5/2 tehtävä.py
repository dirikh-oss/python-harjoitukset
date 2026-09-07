while True:
    tuumat = float(input("Anna tuumamäärä (negatiivinen luku lopettaa): "))
    if tuumat < 0:
        print("Ohjelma lopetettu.")
        break
    senttimetrit = tuumat * 2.54
    print(f"{tuumat} tuumaa on {senttimetrit} cm\n") 