def decoreer(tekst=""):
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()

def som(dictionary):
    totaal = 0

    for waarde in dictionary.values():
        totaal += waarde

    return totaal