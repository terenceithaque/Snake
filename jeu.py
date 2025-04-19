"jeu.py contient la classe Jeu qui représente une partie."
# Importations nécessaires
import pygame
pygame.init()
from serpent import *


class Jeu:
    "Représente une partie en cours avec sa propre fenêtre et éléments."
    def __init__(self, hauteur_fenetre = 800, largeur_fenetre = 600):
        """
        Initialise la partie.
        - hauteur_fenetre: hauteur de la fenêtre en pixels, par défaut 800px
        - largeur_fenetre: largeur de la fenêtre en pixels, par défaut 600px."""


        # Initialiser la fenêtre de jeu
        self.fenetre = pygame.display.set_mode((hauteur_fenetre, largeur_fenetre))
        pygame.display.set_caption("Python Snake !")

        # Instancier le serpent du joueur
        self.serpent = Serpent(self.fenetre)

        self.serpent.ajuster_membres("verticale")
        #self.serpent.ajuster_membres("horizontale")


        # Evénements personnalisés
        self.mouvement_serpent = pygame.USEREVENT + 1
        pygame.time.set_timer(self.mouvement_serpent, 100)


    def executer(self):
        "Exécute la boucle de jeu."
        # Mettre la variable d'exécution à True
        execution = True

        # Commencer la boucle de jeu
        while execution:
            self.fenetre.fill((0, 0, 0))

            # Obtenir les touches pressées par le joueur
            self.touches = pygame.key.get_pressed()

            # Capturer tous les événements utilisateur de la fenêtre (clics de souris, touches pressées, etc.)
            for evenement in pygame.event.get():
                # Si le joueur souhaite quitter le jeu
                if evenement.type == pygame.QUIT:
                    # Arrêter la boucle de jeu$
                    execution = False

                if evenement.type == pygame.MOUSEMOTION:
                    print(pygame.mouse.get_pos())


                # Si le joueur appuie sur la touche "flèche vers le haut"
                if self.touches[pygame.K_UP]:
                    # Changer la direction du serpent
                    self.serpent.changer_direction("haut")

                # Si le joueur appuie sur la touche "flèche vers le bas"
                elif self.touches[pygame.K_DOWN]:
                    # Changer la direction du serpent
                    self.serpent.changer_direction("bas")

                # Si le joueur appuie sur la touche "flèche vers la gauche"
                elif self.touches[pygame.K_LEFT]:
                    # Changer la direction du serpent
                    self.serpent.changer_direction("gauche")

                # Si le joueur appuie sur la touche "flèche vers la droite"
                elif self.touches[pygame.K_RIGHT]:
                    # Changer la direction du serpent
                    self.serpent.changer_direction("droite")



                if evenement.type == self.mouvement_serpent:
                     # Déplacer le serpent en fonction de la direction
                    if self.serpent.direction == "haut":
                        self.serpent.deplacer_haut()

                    elif self.serpent.direction == "bas":
                        self.serpent.deplacer_bas()

                    elif self.serpent.direction == "gauche":
                        self.serpent.deplacer_gauche()

                    elif self.serpent.direction == "droite":
                        self.serpent.deplacer_droite()                                


            if self.serpent.hors_ecran():
                print("Le serpent est hors de l'écran !")
                
            # Afficher le serpent
            self.serpent.afficher()   


            pygame.display.flip()        