# Demander à l'utilisateur d'entrer trois articles et leurs prix
Liste_articles = []
for i in range(3):
    article = input(f"Entrez le nom du {i+1}er article: ")
    prix = float(input(f"Entrez le prix du {i+1}er article (en dollars): "))
    Liste_articles.append([article, prix])

# Afficher le prix de l'imprimante
for article in Liste_articles:
    if article[0].lower() == "imprimante":
        print(f"Le prix de l’article Imprimante est {article[1]}$.")

# Vérification du prix du dernier article de la liste
dernier_article = Liste_articles[-1]
nom_article = dernier_article[0]
prix_article = dernier_article[1]

if prix_article >= 1000:
    print(f"Le prix de l’article {nom_article} est trop cher.")
elif prix_article >= 500:
    print(f"Le prix de l’article {nom_article} est un peu cher.")
elif prix_article >= 100:
    print(f"Le prix de l’article {nom_article} est abordable.")
else:
    print(f"Le prix de l’article {nom_article} est excellent.")

# Demander à l'utilisateur de chercher un article par son nom
nom_recherche = input("Entrez le nom d'un article pour obtenir son prix: ")

# Rechercher l'article dans la liste et afficher son prix ou un message d'erreur
trouve = False
for article in Liste_articles:
    if article[0].lower() == nom_recherche.lower():
        print(f"Le prix de l’article {article[0]} est {article[1]}$.")
        trouve = True
        break

if not trouve:
    print(f"Article {nom_recherche} non trouvé dans la liste.")
