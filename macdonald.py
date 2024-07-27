import datetime

date_time = datetime.datetime.now()
temps = "%Y-%m-%d %H:%M"
date = date_time.strftime(temps)
print(date)


print("Bonjour! Nous sommes ravis de vous accueuillir sur notre site Internet.Commandez nos produits frais et régalez-vous bien.")


print("Maintenant vous pouvez choisir votre entrée: ")
print(" \n 1.Salade 5,75€ \n 2.Nuggets 5,25€ \n 3.Frites 3,75")
numero_entree = int(input('Entrez le numéro de votre entrée choisie (1-3): '))
while numero_entree != [1, 2, 3]:
    print("Choisissez le bon chiffre, s'il vous plaît.")
    numero_entree = int(input('Entrez le numéro de votre entrée choisie (1-3): '))

if numero_entree == 1:
    entree_prix = 5.75
    entree_label = "Salade"
elif numero_entree == 2:
    entree_prix = 5.25
    entree_label = "Nuggets"
elif numero_entree == 3:
    entree_prix = 3.75
    entree_label = "Frites"

print(f"{entree_label} {entree_prix}€ ")

numero_plat = int(input('\nEntrez le numéro de votre plat choisi (1-3): '))
print("\nQu'est-ce qui vous tente comme plat?")
print(" \n 1.Big Mac 10,95€ \n 2.McChicken 8,95€ \n 3.Filet-O-Fish 9,95€")


if numero_plat == 1:
    plat_label = "Big Mac"
    plat_prix = 10.95
elif numero_plat == 2:
    plat_label = "McChicken"
    plat_prix = 8.95
elif numero_plat == 3:
    plat_label = "Filet-O-Fish"
    plat_prix = 9.95
else:
    print("Choisissez le bon chiffre, s'il vous plaît")
print(f"{plat_label} {plat_prix}€ ")

numero_dessert = int(input('Entrez le numéro de votre dessert choisi (1-3): '))
print("et en fin, The best for less.\nAdoucissez votre journée avec de la magie d'un bon dessert MacDO!")
print(" \n 1.Sundae 2,15€ \n 2.Apple Pie 3,25€ \n 3.McFlurry 2,55€")


if numero_dessert == 1:
    dessert_label = "Sundae"
    dessert_prix = 2.25
elif numero_dessert == 2:
    dessert_label = "Apple Pie"
    dessert_prix = 3.25
elif numero_dessert == 3:
    dessert_label = "McFlurry"
    dessert_prix = 2.55
else:
    print("Choisissez le bon chiffre, s'il vous plaît.")

print(f"{entree_label} {dessert_prix}€")

print("\nEt voici votre commande chez nous:")
print(f"{entree_label} {entree_prix}€")
print(f"{plat_label} {plat_prix}€")
print(f"{dessert_label} {dessert_prix}€")

total = entree_prix + plat_prix + dessert_prix

print (f"Total de votre commande est: {total}€ ")
print("Je valide et je passe à l'étape suivante.")
