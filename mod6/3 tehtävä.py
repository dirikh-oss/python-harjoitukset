def gallonat_litroiksi(gallonat):
    return gallonat * 3.785

gallonat = float(input("Anna gallonamäärä: "))

while gallonat >= 0:
    litrat = gallonat_litroiksi(gallonat)
    print("Litroina:", litrat)

    gallonat = float(input("Anna gallonamäärä: "))