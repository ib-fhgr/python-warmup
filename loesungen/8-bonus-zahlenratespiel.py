# in dieser Aufgabe soll ein Zahlenratespiel implementiert werden

# Wir importieren die Bibliothek random, damit kann man Zufallszahlen generieren
# z.B. random.randint(1, 100) generiert eine Zufallszahl zwischen 1 und 100 
import random

# Zufallszahl generieren (zwischen 1 und 100
zufallszahl = random.randint(1, 100)


# Wiederhole:
while True:
    # Zahl vom Benutzer einlesen
    zahl = input("Bitte Zahl eingeben: ")
    zahl = int(zahl) # String in Zahl umwandeln, wir überprüfen hier nicht, ob der Benutzer eine Zahl eingegeben hat

    # Falls die Zahl erraten wurde, soll das Programm beendet werden (break)
    if zahl == zufallszahl:
        print("Richtig geraten!")
        break

    # Sonst Ausgabe ob die Zahl zu gross oder zu klein ist
    if zahl > zufallszahl:
        print("Zu gross!")
    else:
        print("Zu klein!")

print("Ende")

