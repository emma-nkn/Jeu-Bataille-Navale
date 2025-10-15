"""
    ### Le jeu ce deroule dans la console ###
"""

print("Bonjour et bienvenue dans le jeu")
# on crée un tableau vide 'grille' qui represente la grille du jeu
def creer_grille():
    grille = []
    for i in range(10):           # cette boucle s'execute 10* pour créer 10 lignes
        ligne = []                # A chaque tour une ligne vide est créer  
        for j in range(10):       # cette boucle s'execute 10* pour ajouter un . dans la ligne, il represente une case vide 
            ligne.append(".")     
        grille.append(ligne)      #  ceci ajoute chaque ligne à la grille
    return grille

grille_joueur1 = creer_grille()
grille_joueur2 = creer_grille()

# Fonction pour afficher la grille
def afficher_grille(grille):
    """
    Affiche la grille de jeu carrée 10x10 dans la console.

    Chaque ligne de la grille est précédée de son numéro (de 1 à 10).
    La fonction parcourt les 10 premières lignes de la grille et affiche
    le contenu de chaque case, suivi d'un retour à la ligne.
    """
    print("  A B C D E F G H I J ") # ceci represente les coordonées de chaque case sur l'axe horizontal
    for i in range(10):
        print(f"{i + 1:2}", end=" ")  
        for case in grille[i]:
            print(case, end=" ")
        print()

#  Fonction pour placer un bateau 
def placer_les_bateaux(grille):
    bateaux = {
        "Porte-avions": 5,
        "Croiseur": 4,
        "Contre-torpilleur": 3,
        "Sous-marin": 3,
        "Torpilleur": 2
    }
    for nom, taille in bateaux.items():
        print(f"\nPlace ton {nom} de {taille} cases")
        placement_fait = False
        while not placement_fait:
            coordonée_saisie = False
            while not coordonée_saisie:
                colonne = input("Entre une colonne de départ (A-J) : ").upper()
                ligne_str = input("Entre une ligne de départ (1-10) : ")
                orientation = input("Orientation (H pour horizontal, V pour vertical) : ").upper()
                # Vérification de la ligne qui doit être un nombre entre 1 et 10
                if ligne_str.isdigit():
                    ligne = int(ligne_str)    
                    if 1 <= ligne <= 10:
                        # Vérification de la colonne qui doit être une lettre entre A et J 
                        if 'A' <= colonne <= 'J' and len(colonne) == 1:
                            # Vérification de l'orientation qui doit être H ou V 
                            if orientation in ["H", "V"]:
                                coordonée_saisie = True  # Toutes les entrées utilisateur sont valides !
                            else:
                                print("Erreur de saisie: L'orientation doit être 'H' (Horizontal) ou 'V' (Vertical).")
                    else:
                        print("Erreur de saisie: La colonne doit être une seule lettre entre A et J.")
                else:
                    print("Erreur de saisie: La ligne doit être un nombre entre 1 et 10.")
            if coordonée_saisie:
                colonne_index = ord(colonne) - ord("A")  # Conversion de la colonne en indice numérique
                ligne_index = ligne - 1  # car les listes commencent par l'indixe 0
                    # 'placement_ok' devient True si placer_bateau réussit (critères 2 et 3)
                placement_fait = placer_bateau(grille, ligne_index, colonne_index, taille, orientation)
                afficher_grille(grille)

# Exécution de la phase de placement des bateaux par joueurs
print("\n--- Joueur 1 : Placez vos bateaux ---")
placer_les_bateaux(grille_joueur1)

print("\n--- Joueur 2 : Placez vos bateaux ---")
placer_les_bateaux(grille_joueur2)




def attaquer(grille, ligne, colonne):
    if grille[ligne][colonne] == "B":
        grille[ligne][colonne] = "X"    # les coordonnées données sont représentées par X
        print("Touché !")
    elif grille[ligne][colonne] == ".":
        grille[ligne][colonne] = "O"
        print("Manqué !")
    else:
        print("Cette case a déjà été jouée.")

colonne = input("Entre une colonne (A-J) : ").upper()
ligne = int(input("Entre un numéro de ligne (1-10) : "))

 