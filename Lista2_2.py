def zamowienie1(zamowienie):
    cena = 0
    menu = {}
    with open("menu.txt") as f:
        for line in f:
            (key, val) = line.split()
            menu[key] = float(val)
       
    for i in zamowienie:
        if i in menu:
            cena += float(menu[i])

    wynik = "wartosc zamowiena z napiwkiem: " + str(round(1.1 *cena + 0.49)) + " zl"
    return wynik
    
print zamowienie1(["rosol","mielony","kompot"])
print zamowienie1(["kompot"])