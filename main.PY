# on crée un tableau vide 'grille' qui represente la grille du jeu

grille = []
for i in range(10):           # cette boucle s'execute 10* pour créer 10 lignes
    ligne = []                # A chaque tour une ligne vide est créer  
    for j in range(10):       # cette boucle s'execute 10* pour ajouter un . dans la ligne, il represente une case vide 
        ligne.append(".")     
    grille.append(ligne)      #  ceci ajoute chaque ligne à la grille

print("  A B C D E F G H I J ") # ceci represente les coordonées de chaque case sur l'axe horizontal
# Pour afficher la grille
for i in range(10):
    print(i + 1, end="  ")
    for case in grille[i]:
        print(case, end=" ")
    print()

colonne = input("Entre une colonne (A-J) : ").upper()
ligne = int(input("Entre un numéro de ligne (1-10) : "))

# Conversion de la colonne en indice numérique
colonne_index = ord(colonne) - ord("A")
ligne_index = ligne - 1  # car les listes commencent à 0

grille[ligne_index][colonne_index] = "X" # les coordonnées données sont représentées par X