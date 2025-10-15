"""
    ### Le jeu ce deroule dans la console ###
"""
print("Bonjour")
p = input("Votre Pseudo?  ")
print(f"Bienvenue dans le jeu {p}")
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

def placer_bateau(grille, ligne, colonne, taille, orientation): # la fonction prends en paramètre 5 arguments
    if orientation == "H":
        # Vérifie que le bateau ne dépasse pas la grille à droite
        if colonne + taille > 10:
            print("Le bateau dépasse à droite de la grille.")
            return False
        # Vérifie que toutes les cases sont libres
        for j in range(taille):
            if grille[ligne][colonne + j] != ".":
                print("Il y a déjà un bateau ici.")
                return False
        # Place le bateau
        for j in range(taille):
            grille[ligne][colonne + j] = "#"
    else:
        # Vérifie que le bateau ne dépasse pas en bas
        if ligne + taille > 10:
            print("Le bateau dépasse en bas de la grille.")
            return False
        # Vérifie que les cases sont libres
        for i in range(taille):
            if grille[ligne + i][colonne] != ".":
                print("Il y a déjà un bateau ici.")
                return False
                
        # Place le bateau
        for i in range(taille):
            grille[ligne + i][colonne] = "#"

    print("Bateau placé avec succès !")
    return True


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
                
                # Vérification 1 : La ligne doit être un nombre
                if ligne_str.isdigit():
                    ligne = int(ligne_str)
                    
                    # Vérification 2 : La ligne est dans les limites 1-10
                    if 1 <= ligne <= 10:
                        
                        # Vérification 3 : La colonne est dans les limites A-J
                        if 'A' <= colonne <= 'J' and len(colonne) == 1:
                            
                            # Vérification 4 : L'orientation est H ou V
                            if orientation in ["H", "V"]:
                                coordonée_saisie = True # Saisie OK
                            else:
                                print("Erreur de saisie: L'orientation doit être 'H' (Horizontal) ou 'V' (Vertical).")
                        else:
                            print("Erreur de saisie: La colonne doit être une seule lettre entre A et J.")
                    else:
                        # CORRECTION du message d'erreur
                        print("Erreur de saisie: La ligne doit être un nombre entre 1 et 10.")
                else:
                    # CORRECTION du message d'erreur
                    print("Erreur de saisie: La ligne doit être un nombre.")

            if coordonée_saisie:
                colonne_index = ord(colonne) - ord("A")
                ligne_index = ligne - 1
                
                # Appelle la fonction de placement
                placement_fait = placer_bateau(grille, ligne_index, colonne_index, taille, orientation)
                afficher_grille(grille)

""" # Exécution de la phase de placement des bateaux par joueurs
print("\n--- Joueur 1 : Placez vos bateaux ---")
placer_les_bateaux(grille_joueur1)

print("\n--- Joueur 2 : Placez vos bateaux ---")
placer_les_bateaux(grille_joueur2) """


def attaquer(grille, ligne, colonne):
    if grille[ligne][colonne] == "#":
        grille[ligne][colonne] = "X"    # les coordonnées données sont représentées par X
        print("Touché !")
    elif grille[ligne][colonne] == ".":
        grille[ligne][colonne] = "O"
        print("Manqué !")
    else:
        print("Cette case a déjà été jouée.")

colonne = input("Entre une colonne (A-J) : ").upper()
ligne = int(input("Entre un numéro de ligne (1-10) : "))

#  Initialisation du jeu

# Initialisation des grilles
grille_joueur1 = creer_grille()
grille_joueur2 = creer_grille()
grille_tirs_joueur1 = creer_grille() # Grille pour enregistrer les tirs du J1
grille_tirs_joueur2 = creer_grille() # Grille pour enregistrer les tirs du J2

# Exécution de la phase de placement des bateaux par joueurs
print("\n--- Joueur 1 : Placez vos bateaux ---")
placer_les_bateaux(grille_joueur1)

print("\n--- Joueur 2 : Placez vos bateaux ---")
""" # Pause pour que le J1 ne puisse pas voir la grille du J2 sur le même écran
time.sleep(2)
print("Veuillez demander au Joueur 1 de ne pas regarder l'écran...")
time.sleep(3)
placer_les_bateaux(grille_joueur2)
print("\nPlacement terminé pour les deux joueurs.") """
