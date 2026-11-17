import pyxel
from projet_jeu import Jeu

class Menu:
    def __init__(self):
        pyxel.init(256, 256, title="SPACE DEFENDER")
        pyxel.load("images.pyxres")
        pyxel.images[1].load(0, 0, "fond_menu.png")
        pyxel.images[2].load(0, 0, "fond_commande.png")
        pyxel.mouse(True)
        self.etat = "menu"
        self.jeu_instance = None
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.etat == "menu":
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                if 58 <= pyxel.mouse_x <= 198 and 105 <= pyxel.mouse_y <= 135:
                    self.etat = "intro"
                    self.temps_intro = pyxel.frame_count
                elif 58 <= pyxel.mouse_x <= 198 and 148 <= pyxel.mouse_y <= 178:
                    self.etat = "commandes"

        elif self.etat == "commandes":
            if pyxel.btnp(pyxel.KEY_Q):
                self.etat = "menu"

        elif self.etat == "intro":
            if pyxel.frame_count - self.temps_intro >= 120:
                self.jeu_instance = Jeu()
                self.etat = "jeu"

        elif self.etat == "jeu":
            self.jeu_instance.update()

    def draw(self):
        if self.etat == "menu":
            pyxel.blt(0, 0, 1, 0, 0, 256, 256)
            self.menu()

        elif self.etat == "commandes":
            pyxel.cls(0)
            self.commandes()

        elif self.etat == "intro":
            pyxel.cls(0)
            pyxel.text(9, 120, "PUISSE LE SORT VOUS ETRE FAVORABLE DURANT CE LONG PERIPLE...", 11)

        elif self.etat == "jeu":
            self.jeu_instance.draw()

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
        pyxel.text(95, 40, "Histoire", 15)                      # x, y, titre, couleur
        pyxel.text(95, 100, "Commandes", 11)                     # x, y, titre, couleur

        #L'histoire du jeu
        pyxel.text(20, 60, "Ce jeu est l'histoire d'un ", 7)
        pyxel.text(20, 67,"vaisseau spatial qui doit detruire les asteroides pour", 7)
        pyxel.text(20, 74, "se proteger, durant son long, tres long voyage...", 7)

        #Les touches
        pyxel.text(55, 120, "FLECHES : DEPLACER", 7)           # x, y, titre, couleur
        pyxel.text(55, 140, "ESPACE : TIRER", 7)               # x, y, titre, couleur
        pyxel.text(55, 160, "'Q' : RETOUR", 7)                 # x, y, titre, couleur
        pyxel.text(55, 200, "ECHAP : QUITTER", 7)               # x, y, titre, couleur

    def jeu(self):
        pyxel.text(105, 120, "BONNE CHANCE !", 11)              # x, y, titre, couleur
        Jeu()

Menu()