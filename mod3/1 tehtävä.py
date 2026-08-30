pituus = float(input("Kuhan pituus (cm): "))
if pituus < 37:
    print(f"Laske takaisin järveen! Mitasta puuttuu {37 - pituus} cm.")
else:
    print("Kuha on sallitun mittainen.")