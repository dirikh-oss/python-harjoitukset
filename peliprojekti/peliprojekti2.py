ika = int(input("Anna ikäsi: "))

if ika < 12:
    print("Olet alaikäinen. Ohjelma suljetaan.")

else:
    nimi = input("Anna nimesi: ")
    print("Tervetuloa", nimi + "!")

    komento = ""

    while komento != "lopeta":
        print("\nPÄÄVALIKKO")
        print("pelaa")
        print("ohje")
        print("pisteet")
        print("lopeta")

        komento = input("Anna komento: ")

        if komento == "pelaa":
            print("Peli alkaa!")

        elif komento == "ohje":
            print("Tässä ovat pelin ohjeet.")

        elif komento == "pisteet":
            print("Sinulla on 0 pistettä.")

        elif komento == "lopeta":
            print("Ohjelma suljetaan.")

        else:
            print("Tuntematon komento.")