"jeu.py contient la classe Jeu qui représente une partie."
# Importations nécessaires
import pygame
pygame.init()
pygame.mixer.init()
from serpent import *
from pomme import *
from grille import *
from save import *
from tkinter import messagebox


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


         # Grille du jeu
        self.contenu_grille = [[0 for _ in range(20)] for _ in range(5)]
        self.grille = Grille(self.contenu_grille, 0, 700, 0,700, 4,15, self.fenetre)

        # Instancier le serpent du joueur
        self.serpent = Serpent(self.grille, self.fenetre)

        #self.serpent.ajuster_membres("verticale")
        #self.serpent.ajuster_membres("horizontale")


       


        # Définir le groupe des pommes
        self.pommes = pygame.sprite.Group()
        # Pommes piégées
        self.pommes_piegees = pygame.sprite.Group()
        # Ajouter une première pomme au groupe
        self.pommes.add(Pomme(self.grille, 0, 0, 7, 14, "assets/images/pomme.png", self.fenetre))
        #self.pommes_piegees.add(Pomme(self.grille, 0, 0, 7, 14, "assets/images/pomme_piege.png", self.fenetre))


        # Messages affichés sur l'état de la pause
        self.messages_pause = {
            False: "Appuyez espace pour mettre en pause",
            True : "Appuyez sur espace pour reprendre"
        }


        # Police pour le message de sauvegarde
        self.police_sauv = pygame.font.Font(None, 36)
        



        # Evénements personnalisés
        self.mouvement_serpent = pygame.USEREVENT + 1
        pygame.time.set_timer(self.mouvement_serpent, 500)



        self.pause = False


        # Musique du jeu
        
        pygame.mixer.music.load("assets/sons/Snake.mp3")
        pygame.mixer.music.play(-1)


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

    def game_over(self, message="Perdu !") -> None:
        """Affiche un message de game over.
        
        message: texte du message"""

        messagebox.showwarning("Game over !", message)




    def executer(self):
        "Exécute la boucle de jeu."
        # Mettre la variable d'exécution à True
        execution = True

        # Commencer la boucle de jeu
        while execution:
            self.fenetre.fill((0, 0, 0))
            print(self.serpent.direction)



            #print("Nombre de membres du serpent :", len(self.serpent.membres))


            #print("tete.position() =", self.serpent.tete.position())
            

            # Obtenir les touches pressées par le joueur
            self.touches = pygame.key.get_pressed()


            #print(self.serpent.positions)

            # Capturer tous les événements utilisateur de la fenêtre (clics de souris, touches pressées, etc.)
            for evenement in pygame.event.get():
                # Si le joueur souhaite quitter le jeu
                if evenement.type == pygame.QUIT:
                    # Arrêter la boucle de jeu$
                    execution = False

                if evenement.type == pygame.MOUSEMOTION:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    #print(x, ",", y)
                    #print(self.grille.coordonnees(x, y))


                # Si une seule touche est pressée
                if self.touches.count(True) == 1:    


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


                        # Sauvegarde
                        elif evenement.key == pygame.K_s:
                            tete = self.serpent.obtenir_tete()
                            ligne_tete = self.grille.coordonnees(self.serpent.tete.rect.x,
                                                                 self.serpent.tete.rect.y)[0]
                            col_tete = self.grille.coordonnees(self.serpent.tete.rect.x,
                                                                 self.serpent.tete.rect.y)[1]
                            print("Sauvegarde !")
                            sauvegarder_partie(self.serpent.points,
                                               self.serpent.max_points, ligne_tete, col_tete, self.serpent.taille,
                                               self.serpent.direction)




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
                self.serpent.tete = self.serpent.obtenir_tete()
                #print(self.serpent.tete.chemin_image)
                print("Le serpent est hors de l'écran !")
                # Positions x et y de la tête du serpent
                x, y = self.serpent.tete.position()
                ligne, col = self.grille.coordonnees(x, y)
                #print("Position de la tête du serpent :", (x, y), f" soit {(ligne, col)}")
                if ligne < 0:
                    ligne = 5
                    #self.serpent.repositionner(ligne, col, "verticale")
                    self.serpent.tete.positionner(ligne, col)
                    self.serpent.ajuster_membres("verticale")

                elif ligne > 5:
                    ligne = 0
                    self.serpent.tete.positionner(ligne, col)
                    self.serpent.ajuster_membres("verticale")

                if col < 0:
                    col = 5
                    self.serpent.tete.positionner(ligne, col)
                    self.serpent.ajuster_membres("horizontale")
                    #self.serpent.changer_direction("haut")

                elif col > 20:
                    col = 0
                    self.serpent.tete.positionner(ligne, col)
                    self.serpent.ajuster_membres("horizontale")


            self.grille.afficher()
            # Afficher le serpent
            self.serpent.afficher()


            
            for pomme in self.pommes:
                # Si le serpent est en train de manger une pomme
                if self.serpent.verifier_mange_pomme(pomme):
                    
                    self.serpent.augmenter_points(15)
                    # Ajouter un membre au serpent
                    queue = self.serpent.obtenir_queue()
                    if self.serpent.direction == "haut":
                        ligne = self.grille.coordonnees(queue.rect.x, queue.rect.y)[0] -1
                        col = self.grille.coordonnees(queue.rect.x, queue.rect.y)[1]
                        self.serpent.ajouter_membre(self.grille, self.fenetre, "assets/images/noeud1.png",ligne, col)
                        print("Taille du serpent :", self.serpent.taille)


                    elif self.serpent.direction == "bas":
                        ligne = self.grille.coordonnees(queue.rect.x, queue.rect.y)[0] + 1
                        col = self.grille.coordonnees(queue.rect.x, queue.rect.y)[1]
                        self.serpent.ajouter_membre(self.grille, self.fenetre, "assets/images/noeud1.png",ligne, col)
                        print("Taille du serpent :", self.serpent.taille)

                    elif self.serpent.direction == "gauche":
                        ligne = self.grille.coordonnees(queue.rect.x, queue.rect.y)[0]
                        col = self.grille.coordonnees(queue.rect.x, queue.rect.y)[1] - 1
                        self.serpent.ajouter_membre(self.grille, self.fenetre, "assets/images/noeud1.png",ligne, col)
                        print("Taille du serpent :", self.serpent.taille)

                    elif self.serpent.direction == "droite":
                        ligne = self.grille.coordonnees(queue.rect.x, queue.rect.y)[0]
                        col = self.grille.coordonnees(queue.rect.x, queue.rect.y)[1] + 1
                        self.serpent.ajouter_membre(self.grille, self.fenetre, "assets/images/noeud1.png",ligne, col)
                        print("Taille du serpent :", self.serpent.taille)        
                    
                    pomme.kill()
                    

                    # Ajouter une pomme normale ou piégée
                    
                    proba_piegee = random.randint(0, 100)
                    if proba_piegee >= 90:
                        self.pommes_piegees.add(Pomme(self.grille, 0, 0, 7, 14, "assets/images/pomme_piege.png", self.fenetre))

                    else:
                        self.pommes.add(Pomme(self.grille, 0, 0, 7, 14, "assets/images/pomme.png", self.fenetre))

                    # Ajouter un membre au serpent
                    #self.serpent.ajouter_membre(self.grille)    
                else:    
                    # Afficher les pommes
                    pomme.afficher()

            # Afficher les pommes piégées
            for pomme in self.pommes_piegees:
                # Si le serpent avale une pomme piégée
                if self.serpent.verifier_mange_pomme(pomme):
                    # Probabilité de 25 % que le joueur meure
                    pomme.kill()
                    proba_mort = random.randint(0, 100)
                    print("Probabilité de mort :", proba_mort)
                    if proba_mort >= 75:
                        
                        
                        self.game_over("Vous avez mangé une pomme piégée et vous êtes mort(e).")
                        self.serpent.tuer()
                        pygame.time.delay(1000)
                        execution = False

                    # Si le joueur n'est pas mort, générer une pomme normale ou piégée
                    proba_piegee = random.randint(0, 100)
                    if proba_piegee >= 90:
                        self.pommes_piegees.add(Pomme(self.grille, 0, 0, 7, 14, "assets/images/pomme_piege.png", self.fenetre))

                    else:
                        self.pommes.add(Pomme(self.grille, 0, 0, 7, 14, "assets/images/pomme.png", self.fenetre))


                pomme.afficher()


            # Si la tête entre en collision avec tout autre membre du corps
            for i in range(1, len(self.serpent.membres)):
                if self.serpent.se_mange(self.serpent.membres[i]):
                    
                    self.game_over("Vous vous êtes mangé et vous êtes mort(e).")
                    self.serpent.tuer()
                    pygame.time.delay(1000)
                    execution = False           



            self.serpent.afficher_points()
            self.afficher_message_pause()

            
            pygame.display.flip()        