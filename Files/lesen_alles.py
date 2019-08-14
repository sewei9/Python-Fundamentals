import sys

# zugriffsversuch
try:
    d = open("lesen.txt")
except:
    print("Dateizugriff nicht möglich")
    sys.exit(0)

# Lesen des gesamten Textes
gesamtertext = d.read()

# Schliessen der Datei
d.close()

# Umwandeln in eine Liste
zeilenliste = gesamtertext.split(chr(10))

# Summieren und Ausgeben
summe = 0
for zeile in zeilenliste:
    if zeile:
        summe += float(zeile)
    print(zeile)

# Summe ausgeben
print("Summe:", summe)
