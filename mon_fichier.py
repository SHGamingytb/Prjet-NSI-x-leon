import pyxel

class Menu:

    def __init__(self):
        pyxel.init(256, 256, title="SPACE DEFENDER")            # Affiche le titre
        pyxel.images[0].load(0, 0, "fond_menu.png")             # Récupère le fond du menu
        pyxel.images[1].load(0, 0, "fond_commande.png")         # Récupère le fond pour le jeu
        pyxel.mouse(True)                                       # Affiche la souris dans pyxel
        self.etat = "menu"                                      # Affichage du menu
        pyxel.run(self.update, self.draw)                       # Affichage du menu

    def update(self):
        if self.etat == "menu":

            # Bouton JOUER
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                if 58 <= pyxel.mouse_x <= 198 and 105 <= pyxel.mouse_y <= 135:          # Emplacement de la souris
                    self.etat = "jeu"                           # Lancement de jeu

                # Bouton COMMENT JOUER
                elif 58 <= pyxel.mouse_x <= 198 and 148 <= pyxel.mouse_y <= 178:        # Emplacement de la souris
                    self.etat = "commandes"                     # Lancement de commande
        #elif self.etat == "commandes":
            #if pyxel.btnp(pyxel.KEY_ESCAPE):
                #self.etat = "menu"
        #elif self.etat == "jeu":
            #if pyxel.btnp(pyxel.KEY_ESCAPE):
                #self.etat = "menu"

    def draw(self):
        if self.etat == "menu":

            # Affichage du fond du menu
            pyxel.blt(0, 0, 0, 0, 0, 256, 256)                  # Affichage du fond du menu
            self.menu()
        elif self.etat == "commandes":
            pyxel.blt(0, 0, 1, 0, 0, 256, 256)                  # Affichage du fond du jeu
            self.commandes()
        elif self.etat == "jeu":
            pyxel.blt(0, 0, 1, 0, 0, 256, 256)                  # Affichage du fond du jeu
            self.jeu()

    def menu(self):
        # Titre
        pyxel.text(100, 55, "SPACE DEFENDER", 11)               # x, y, titre, couleur

        # Bouton JOUER
        pyxel.rect(58, 105, 140, 30, 5)                         # Le rectangle bleu : x, y, longueur, largeur, couleur
        pyxel.rectb(58, 105, 140, 30, 7)                        # Le rectangle blanc : x, y, longueur, largeur, couleur
        pyxel.text(114, 117, "JOUER", 7)                        # x, y, titre, couleur

        # Bouton COMMENT JOUER
        pyxel.rect(58, 148, 140, 30, 4)                         # Le rectangle rouge : x, y, longueur, largeur, couleur
        pyxel.rectb(58, 148, 140, 30, 7)                        # Le rectangle blanc : x, y, longueur, largeur, couleur
        pyxel.text(100, 160, "COMMENT JOUER", 7)                # x, y, titre, couleur

    def commandes(self):
        #Les titres
        pyxel.text(95, 40, "Histoire", 11)                      # x, y, titre, couleur
        pyxel.text(95, 100, "Commande", 11)                     # x, y, titre, couleur

        #L'histoire du jeu
        pyxel.text(20, 60, "Ce jeu est l'histoire d'un ", 8)
        pyxel.text(20, 67,"vaisseau spatial qui doit detruir les asteroides pour", 8)
        pyxel.text(20, 74, "se proteger, durant son long, tres long trajet...", 8)

        #Les touches
        pyxel.text(55, 120, "FLECHES : DEPLACER", 10)           # x, y, titre, couleur
        pyxel.text(55, 140, "ESPACE : TIRER", 10)               # x, y, titre, couleur
        pyxel.text(55, 160, "'Q' : RETOUR", 10)                 # x, y, titre, couleur
        pyxel.text(55, 200, "ECHAP : QUITTER", 6)               # x, y, titre, couleur

    def jeu(self):
        pyxel.text(105, 120, "BONNE CHANCE !", 11)              # x, y, titre, couleur

Menu()