from helper import decoreer
def print_aanbieding():
    prijzen = {
    "aardbei" : 3,
    "vanille" : 4,
    "chocolade" : 5    
    }
    aanbieding = (prijzen["aardbei"]) * 0.8
    Reclametekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding}"
    Reclametekst2 = Reclametekst[:63]
    Reclametekst3 = Reclametekst2.upper()
    Reclametekst4 = Reclametekst3.split(" ")
    for el in Reclametekst4:
        if len(el) <= 4: 
            print (el.lower())
        else:
            print (el.upper())
decoreer("aanbieding")
print_aanbieding()