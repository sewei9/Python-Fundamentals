# Definition der Funktion
def halbieren(wert):
    print(wert)
    wert = wert / 2
    if wert > 0.05:
        halbieren(wert)

# Main programm
halbieren(3)