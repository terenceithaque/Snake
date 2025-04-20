"jeu.py contient la classe Jeu qui représente une partie."
# Importations nécessaires
import pygame
pygame.init()
from serpent import *
from pomme import *


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


        # Définir le groupe des pommes
        self.pommes = pygame.sprite.Group()
        # Ajouter une première pomme au groupe
        self.pommes.add(Pomme(0, 0, 700, 700, "assets/images/pomme.png", self.fenetre))


        # Messages affichés sur l'état de la pause
        self.messages_pause = {
            False: "Appuyez espace pour mettre en pause",
            True : "Appuyez sur espace pour reprendre"
        }
        



        # Evénements personnalisés
        self.mouvement_serpent = pygame.USEREVENT + 1
        pygame.time.set_timer(self.mouvement_serpent, 100)



        self.pause = False


    def afficher_message_pause(self):
        "Affiche le message de pause selon l'état actuel du jeu."
        # Afficher le message de pause approprié
        message_pause = self.messages_pause[self.pause]
        self.police_pause = pygame.font.Font(None, 25)
        affichage = self.police_pause.render(message_pause, True, (255, 255, 255))
        self.fenetre.blit(affichage, (0, 0))


    def pauser(self) -> bool:
        "Met le jeu en pause ou le sort de la pause"
        self.pause = not self.pause
        print("Etat de la pause :", self.pause)
        
        
        return self.pause    


    def executer(self):
        "Exécute la boucle de jeu."
        # Mettre la variable d'exécution à True
        execution = True

        # Commencer la boucle de jeu
        while execution:
            #self.fenetre.fill((0, 0, 0))

            print("Nombre de membres du serpent :", len(self.serpent.membres))


            
            

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


                # Détecter les touches pressées ET relâchées
                if evenement.type == pygame.KEYUP:
                    print("Touche pressée et relâchée !")
                    # Changer la direction du serpent en fonction de la touche pressée et relâchée

                    # Haut
                    if evenement.key == pygame.K_UP:
                        if not self.pause:
                            self.serpent.changer_direction("haut")

                    # Bas
                    elif evenement.key == pygame.K_DOWN:
                        # Changer la direction du serpent
                        if not self.pause:
                            self.serpent.changer_direction("bas")

                    # Gauche
                    elif evenement.key == pygame.K_LEFT:
                        # Changer la direction du serpent
                        if not self.pause:
                            self.serpent.changer_direction("gauche")

                    # Droite
                    elif evenement.key == pygame.K_RIGHT:
                        # Changer la direction du serpent
                        if not self.pause:
                            self.serpent.changer_direction("droite")

                    # Pause
                    elif evenement.key == pygame.K_SPACE:
                        self.pauser()    



                if evenement.type == self.mouvement_serpent:
                     # Déplacer le serpent en fonction de la direction
                    if self.serpent.direction == "haut":
                        if not self.pause:
                            self.serpent.deplacer_haut()

                    elif self.serpent.direction == "bas":
                        if not self.pause:
                            self.serpent.deplacer_bas()

                    elif self.serpent.direction == "gauche":
                        if not self.pause:
                            self.serpent.deplacer_gauche()

                    elif self.serpent.direction == "droite":
                        if not self.pause:
                            self.serpent.deplacer_droite()                                


            if self.serpent.hors_ecran():
                print("Le serpent est hors de l'écran !")
                # Positions x et y de la tête du serpent
                x, y = self.serpent.tete.position()
                if x < 0:
                    x = 700
                    self.serpent.tete.positionner_x(x)
                    self.serpent.ajuster_membres("verticale")

                elif x > 700:
                    x = 0
                    self.serpent.tete.positionner_x(x)
                    self.serpent.ajuster_membres("verticale")

                if y < 0:
                    y = 700
                    self.serpent.tete.positionner_y(y)
                    self.serpent.ajuster_membres("horizontale")

                elif y > 700:
                    y = 0
                    self.serpent.tete.positionner_y(y)
                    self.serpent.ajuster_membres("horizontale")


            # Afficher le serpent
            self.serpent.afficher()


            # Afficher les pommes
            for pomme in self.pommes:
                pomme.afficher()   


            self.afficher_message_pause()

            
            pygame.display.flip()        