# on crée un tableau vide 'grille' qui represente la grille du jeu

grille = []
for i in range(10):           # cette boucle s'execute 10* pour créer 10 lignes
    ligne = []                # A chaque tour une ligne vide est créer  
    for j in range(10):       # cette boucle s'execute 10* pour ajouter un . dans la ligne, il represente une case vide 
        ligne.append(".")     
    grille.append(ligne)      #  ceci ajoute chaque ligne à la grille

print("  A B C D E F G H I J ") # ceci represente les coordonées de chaque case sur l'axe horizontal
# Pour afficher la grille
def afficher_grille(grille):
    for i in range(10):
        print(i + 1, end="  ")  
        for case in grille[i]:
            print(case, end=" ")
        print()

#  Fonction pour placer un bateau 
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
            grille[ligne + i][colonne] = "B"

    print("Bateau placé avec succès !")
    return True

# --- Placement de chaque beauteau dans la grille ---
# Bateau 1 Porte-avions (5 cases)
print("\nPlace ton Porte-avions à 5 cases")
placement_ok = False
while not placement_ok:
    colonne = input("Entre une colonne de départ (A-J) : ").upper()
    ligne = int(input("Entre une ligne de départ (1-10) : "))
    orientation = input("Orientation (H pour horizontal, V pour vertical) : ").upper()

    colonne_index = ord(colonne) - ord("A")
    ligne_index = ligne - 1

    placement_ok = placer_bateau(grille, ligne_index, colonne_index, 5, orientation)
    afficher_grille(grille)

# Bateau 2 Croiseur (4 cases)
print("\nPlace ton Croiseur à 4 cases")
placement_ok = False
while not placement_ok:
    colonne = input("Entre une colonne de départ (A-J) : ").upper()
    ligne = int(input("Entre une ligne de départ (1-10) : "))
    orientation = input("Orientation (H pour horizontal, V pour vertical) : ").upper()

    colonne_index = ord(colonne) - ord("A")
    ligne_index = ligne - 1

    placement_ok = placer_bateau(grille, ligne_index, colonne_index, 4, orientation)
    afficher_grille(grille)

# Bateau 3 Contre-torpilleur (3 cases)
print("\nPlace ton Contre-torpilleur (3 cases)")
placement_ok = False
while not placement_ok:
    colonne = input("Entre une colonne de départ (A-J) : ").upper()
    ligne = int(input("Entre une ligne de départ (1-10) : "))
    orientation = input("Orientation (H pour horizontal, V pour vertical) : ").upper()

    colonne_index = ord(colonne) - ord("A")
    ligne_index = ligne - 1

    placement_ok = placer_bateau(grille, ligne_index, colonne_index, 3, orientation)
    afficher_grille(grille)

# Bateau 4 Sous-marin (3 cases)
print("\nPlace ton Sous-marin (3 cases)")
placement_ok = False
while not placement_ok:
    colonne = input("Entre une colonne de départ (A-J) : ").upper()
    ligne = int(input("Entre une ligne de départ (1-10) : "))
    orientation = input("Orientation (H pour horizontal, V pour vertical) : ").upper()

    colonne_index = ord(colonne) - ord("A")
    ligne_index = ligne - 1

    placement_ok = placer_bateau(grille, ligne_index, colonne_index, 3, orientation)
    afficher_grille(grille)

# Bateau 5 Torpilleur (2 cases)
print("\nPlace ton Torpilleur (2 cases)")
placement_ok = False
while not placement_ok:
    colonne = input("Entre une colonne de départ (A-J) : ").upper()
    ligne = int(input("Entre une ligne de départ (1-10) : "))
    orientation = input("Orientation (H pour horizontal, V pour vertical) : ").upper()
    
    colonne_index = ord(colonne) - ord("A")  # Conversion de la colonne en indice numérique
    ligne_index = ligne - 1  # car les listes commencent par l'indixe 0

    placement_ok = placer_bateau(grille, ligne_index, colonne_index, 2, orientation)
    afficher_grille(grille)

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

 