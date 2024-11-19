counter = 1

print("This program will ask you for 3 items with their respective prices. ")
items = []

while counter <= 3:
    item = input(f"Enter item number {counter}: ")
    prix = float(input("Enter it`s price: "))
    items.append([item, prix])
    counter += 1

# afficher le prix de l'imprimmante
dernier_article = items[-1]
nom_dernier_article = dernier_article[0]
prix_dernier_article = dernier_article[1]

print(f"Le prix pour l'imprimmante est {prix_dernier_article}")
