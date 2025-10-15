"""
    ### Le jeu ce deroule dans la console ###
"""
import time

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
    """ 
    La fonction retourne True si le tir a été effectué (Touché ou Manqué)
    et False si le tir est sur une case déjà jouée.

    """
    if grille[ligne][colonne] == "#":
        grille[ligne][colonne] = "X"    # les coordonnées données sont représentées par X
        print("Touché !")
    elif grille[ligne][colonne] == ".":
        grille[ligne][colonne] = "O"
        print("Manqué !")
    else:
        print("Cette case a déjà été touchée.")

""" colonne = input("Entre une colonne (A-J) : ").upper()
ligne = int(input("Entre un numéro de ligne (1-10) : ")) """

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
time.sleep(2)
print("Passage au Joueur 2...")
time.sleep(3)
placer_les_bateaux(grille_joueur2)
print("\nPlacement terminé pour les deux joueurs. La partie commence !")


def jouer():
    joueur_tour = 1
    
    while True:
        # 1. Détermine le joueur actif et les grilles cibles/tirs
        if joueur_tour == 1:
            joueur_actif = 1
            grille_cible = grille_joueur2        
            grille_tirs_joueur_actif = grille_tirs_joueur1
        else:
            joueur_actif = 2
            grille_cible = grille_joueur1        
            grille_tirs_joueur_actif = grille_tirs_joueur2

        print(f"\n TOUR DU JOUEUR {joueur_actif}")
        
        # Affiche la grille des tirs (la grille de l'adversaire vue par le joueur)
        print("\nVoici votre grille de tirs (Adversaire) :")
        afficher_grille(grille_tirs_joueur_actif, cacher_bateaux=False) 

        tir_valide = False
        while not tir_valide:
            saisie_fait = False
            while not saisie_fait:
                colonne = input(f"J{joueur_actif}, entre une colonne de tir (A-J) : ").upper()
                ligne_str = input(f"J{joueur_actif}, entre un numéro de ligne de tir (1-10) : ")
                
                # Validation de la LIGNE (Doit être un nombre)
                if ligne_str.isdigit():
                    ligne = int(ligne_str) # Conversion en nombre
                    
                    # Validation des LIMITES (Colonne et Ligne)
                    if 'A' <= colonne <= 'J' and 1 <= ligne <= 10:
                        saisie_fait = True
                    else:
                        print("Erreur : Coordonnées hors limites (A-J, 1-10).")
                else:
                    print("Erreur : La ligne doit être un nombre.")

            # Conversion des indices (s'exécute uniquement si saisie_ok est True)
            colonne_index = ord(colonne) - ord("A")
            ligne_index = ligne - 1
            
            # Vérification du double tir (Story 7)
            if grille_tirs_joueur_actif[ligne_index][colonne_index] != '.':
                print("Cette case a déjà été ciblée. Choisissez une autre case.")
                continue 

            # Tente d'attaquer la grille adverse (Story 6)
            attaque_effectuee = attaquer(grille_cible, ligne_index, colonne_index)
            
            # Mettre à jour la grille de tirs du joueur
            if attaque_effectuee:
                # Transfère le résultat du tir ('X' ou 'O') sur la grille de tirs du joueur
                grille_tirs_joueur_actif[ligne_index][colonne_index] = grille_cible[ligne_index][colonne_index]
                tir_valide = True
            
            print("\nGrille de tirs après le coup :")
            afficher_grille(grille_tirs_joueur_actif)

        