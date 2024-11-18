# Définir une liste d'exemple
ma_liste = [1, 2, 3, 4, 5]

# Méthode 1 : Utiliser une boucle for
print("Affichage avec une boucle for :")
for element in ma_liste:
    print(element)

# Méthode 2 : Utiliser la méthode join() et une compréhension de liste
print("\nAffichage avec join et compréhension de liste :")
print(" ".join([str(element) for element in ma_liste]))
