"main.py lance le jeu."
# Importations nécessaires
import pygame
pygame.init()
from tkinter import messagebox
from jeu import *

# Instancier et exécuter une première partie, avec une fenêtre de dimebnsions 800x600
jeu = Jeu(800, 600)
jeu.executer()
# Quitter pygame quand la partie est finie.
pygame.quit()


# Entrer dans une boucle pour demander au joueur s'il souhaite rejouer
while True:
    rejouer = messagebox.askyesno("Rejouer ?", "Souhaitez-vous rejouer ?")
    # Si le joueur veut rejouer
    if rejouer:
        # Réinitialiser  pygame et relancer le jeu
        pygame.init()
        jeu = Jeu(800, 600)
        jeu.executer()
        # Quand la partie est finie, quitter pygame
        pygame.quit()


    # Si le joueur ne souhaite pas rejouer
    else:
        break    




