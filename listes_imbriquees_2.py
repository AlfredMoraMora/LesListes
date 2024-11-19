# Liste de départ avec les fruits et leurs informations
Liste_fruits = [
    ['Pomme', 38, 2.45],
    ['Pain', 70, 2.99],
    ['Orange', 42, 2.75],
    ['Carottes', 30, 1.99],
    ['Navet', 30, 0.99],
    ['Bananes', 65, 0.80]
]

# Suppression des articles non-fruits (Pain, Carottes, Navet)
Liste_fruits = [fruit for fruit in Liste_fruits if fruit[0] not in ['Pain', 'Carottes', 'Navet']]
# The following code provides a way of achieving the same result without using list comprehension
"""# Créer une nouvelle liste vide
new_list = []

# Parcourir chaque élément de la liste initiale
for fruit in Liste_fruits:
    # Si le fruit n'est pas dans la liste des éléments à supprimer
    if fruit[0] not in ['Pain', 'Carottes', 'Navet']:
        # Ajouter ce fruit à la nouvelle liste
        new_list.append(fruit)

# Remplacer l'ancienne liste par la nouvelle liste filtrée
Liste_fruits = new_list
"""

# Ajout des nouveaux fruits (Pêche, Poire)
Liste_fruits.extend([['Pêche', 38, 2.45], ['Poire', 30, 0.99]])

# Modification des indices glycémiques de la Pêche et de la Poire
for fruit in Liste_fruits:
    if fruit[0] == 'Pêche':
        fruit[1] = 30
    elif fruit[0] == 'Poire':
        fruit[1] = 38

# Afficher le dernier élément de la liste avec son indice glycémique et son prix
dernier_fruit = Liste_fruits[-1]
print(f"Le dernier fruit de la liste est {dernier_fruit[0]} avec un indice glycémique de {dernier_fruit[1]} et un prix de {dernier_fruit[2]}$.")

# Trier la liste par le nom du fruit (le premier élément de chaque sous-liste)
Liste_fruits.sort(key=lambda fruit: fruit[0])
# similar way of achieving the same result without using an anonymous function (lamda). 
"""# Définir une fonction pour extraire le nom du fruit
def get_fruit_name(fruit):
    return fruit[0]

# Trier la liste en utilisant cette fonction
Liste_fruits.sort(key=get_fruit_name)
"""

# Demander à l'utilisateur d'entrer un fruit et afficher son indice glycémique et son prix
fruit_recherche = input("Entrez le nom d'un fruit pour obtenir ses informations : ").capitalize()

# Recherche du fruit et affichage de ses informations
trouve = False
for fruit in Liste_fruits:
    if fruit[0] == fruit_recherche:
        print(f"Le fruit {fruit[0]} a un indice glycémique de {fruit[1]} et coûte {fruit[2]}$.")
        trouve = True
        break

if not trouve:
    print(f"Le fruit {fruit_recherche} n'est pas dans la liste.")

