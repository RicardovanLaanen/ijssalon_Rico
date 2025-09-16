from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs * (1 - korting)
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs:.2f} euro."

def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    bedrag = totaal * btw
    return f"Het totaal van alle inkomsten van deze week is {totaal:.2f} euro, waarover {bedrag:.2f} euro btw betaald dient te worden."

def laag_en_hoog(mijn_lijst):
    hoogste = max(mijn_lijst)
    laagste = min(mijn_lijst)
    return [hoogste, laagste]

def gemiddelde(mijn_lijst):
    avg = sum(mijn_lijst) / len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {avg:.2f} euro."

def meervourdig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    return mijn_functie_2(korte_lijst)