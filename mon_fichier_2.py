import pyxel

class Menu:

    def __init__(self):
        pyxel.init(256, 256, title="SPACE DEFENDER")

        # Récupère le fond du menu
        pyxel.images[0].load(0, 0, "fond_menu.png")

        pyxel.mouse(True)

        self.etat = "menu"

        # Variables pour l'animation du fond
        self.position_fond = 0
        self.vitesse_fond = 1
        self.morceau_actuel = 0

        # Chargement des deux premiers morceaux
        self.charger_fond()

        pyxel.run(self.update, self.draw)

    def charger_fond(self):

        # Charge le morceau actuel dans la banque 1
        pyxel.images[1].load(
            0, 0, f"fond_{self.morceau_actuel}.png"
        )

        # Calcule le numéro du morceau suivant
        morceau_suivant = (self.morceau_actuel + 1) % 6

        # Charge le morceau suivant dans la banque 2
        pyxel.images[2].load(
            0, 0, f"fond_{morceau_suivant}.png"
        )

    def update(self):

        if self.etat == "menu":

            # Bouton JOUER
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):

                if 58 <= pyxel.mouse_x <= 198 and 105 <= pyxel.mouse_y <= 135:

                    self.etat = "jeu"

                    # Remet le fond au début
                    self.position_fond = 0
                    self.morceau_actuel = 0
                    self.charger_fond()

                # Bouton COMMENT JOUER
                elif 58 <= pyxel.mouse_x <= 198 and 148 <= pyxel.mouse_y <= 178:

                    self.etat = "commandes"

        elif self.etat == "commandes":

            if pyxel.btnp(pyxel.KEY_ESCAPE):
                self.etat = "menu"

        elif self.etat == "jeu":

            # Animation du fond
            self.position_fond += self.vitesse_fond

            # Le fond recommence au début après 1536 pixels
            self.position_fond %= 1536

            # Détermine le morceau actuellement affiché
            nouveau_morceau = self.position_fond // 256

            # Si on change de morceau, on recharge les images
            if nouveau_morceau != self.morceau_actuel:

                self.morceau_actuel = nouveau_morceau
                self.charger_fond()

            # Retour au menu avec ECHAP
            if pyxel.btnp(pyxel.KEY_ESCAPE):
                self.etat = "menu"

    def draw(self):

        if self.etat == "menu":

            # Affichage du fond du menu
            pyxel.blt(0, 0, 0, 0, 0, 256, 256)
            self.menu()

        elif self.etat == "commandes":

            # Affichage du fond des commandes
            pyxel.blt(0, 0, 0, 0, 0, 256, 256)
            self.commandes()

        elif self.etat == "jeu":

            # Calcule le décalage du fond
            decalage = self.position_fond % 256

            # Affichage du morceau actuel
            pyxel.blt(
                0, -decalage, 1,
                0, 0, 256, 256
            )

            # Affichage du morceau suivant
            pyxel.blt(
                0, 256 - decalage, 2,
                0, 0, 256, 256
            )

            self.jeu()

    def menu(self):

        # Titre
        pyxel.text(100, 55, "SPACE DEFENDER", 11)

        # Bouton JOUER
        pyxel.rect(58, 105, 140, 30, 5)
        pyxel.rectb(58, 105, 140, 30, 7)
        pyxel.text(114, 117, "JOUER", 7)

        # Bouton COMMENT JOUER
        pyxel.rect(58, 148, 140, 30, 4)
        pyxel.rectb(58, 148, 140, 30, 7)
        pyxel.text(100, 160, "COMMENT JOUER", 7)

    def commandes(self):

        pyxel.text(95, 50, "COMMANDES", 11)
        pyxel.text(55, 100, "FLECHES : DEPLACER", 7)
        pyxel.text(55, 125, "ESPACE : TIRER", 7)
        pyxel.text(55, 180, "ECHAP : RETOUR", 6)

    def jeu(self):

        pyxel.text(105, 120, "BONNE CHANCE !", 11)


Menu()