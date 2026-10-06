# Exercice 1 : Note et mention

note = int(input("Entre ta note sur 20 : "))

if note < 0 or note > 20:
    print("Note invalide")
elif note >= 16:
    print("Très bien")
elif note >= 14:
    print("Bien")
elif note >= 12:
    print("Assez bien")
elif note >= 10:
    print("Passable")
else:
    print("Refusé")


# Exercice 2 : pair ou impair
nombre = int(input("Écris un nombre : "))

if nombre % 2 == 0:
    print("Pair")
else:
    print("Impair")


# Exercice 3 : tarif cinéma

age = int(input("Entre ton âge : "))

if age < 0:
    print("Âge invalide")
elif age < 12:
    print("Tarif enfant")
elif (age >= 12 and age <= 25) or age >= 65:
    print("Tarif réduit")
else:
    print("Plein tarif")


# Exercice 4 : année bissextile
annee = int(input("Entre une année : "))

if annee % 400 == 0:
    print("Bissextile")
elif annee % 100 == 0:
    print("Non bissextile")
elif annee % 4 == 0:
    print("Bissextile")
else:
    print("Non bissextile")