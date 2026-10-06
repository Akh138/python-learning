places_occupees = 10

if places_occupees >= 16:
    print("fermer")
elif places_occupees >= 14:
    print("Presque complet")
else:
    print("Ouvert")

places_occupees = int(input("Nombre de places occupées : "))
if  places_occupees >= 0 and places_occupees < 14:
    print("Ouvert")