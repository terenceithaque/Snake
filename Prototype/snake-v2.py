"""
Programme Snake version 2

"""
from tkinter import * # Importation de la bibliothèque  Tkinter 

# On crée un environnement Tkinter
tk = Tk()

def right(event):
    # Modification de la variable globale direction
    global direction
    direction = 'right'
    
def left(event):
    # Modification de la variable globale direction
    global direction
    direction = 'left'
    
def down(event):
    # Modification de la variable globale direction
    global direction
    direction = 'down'
    
def up(event):
    # Modification de la variable globale direction
    global direction
    direction = 'up'

# Calcule la nouvelle frame de jeu
def computeNextFrame(numFrame,coordonnee):
    global direction
    # Affiche le numérod de la frame
    #print(numFrame)
    numFrame = numFrame + 1
    
    # Effacer le canevas
    can.delete('all')
    
    # Mise à jour des coordonnées
    if direction == 'right':
        coordonnee[0] += 20
        if coordonnee[0] > 500:
            coordonnee[0] = 0
    if direction == 'left':
        coordonnee[0] += -20
        if coordonnee[0] < 0:
            coordonnee[0] = 480
    if direction == 'up':
        coordonnee[1] += -20
        if coordonnee[1] < 0:
            coordonnee[1] = 480
    if direction == 'down':
        coordonnee[1] += 20
        if coordonnee[1] > 500:
            coordonnee[1] = 0

    # Dessin de la tête du serpent
    can.create_rectangle(coordonnee[0], coordonnee[1], coordonnee[0] + 20, 
                         coordonnee[1] + 20, outline='yellow', fill='red')
    
    # Calcule une nouvelle frame dans 100 ms
    tk.after(100, lambda:computeNextFrame(numFrame,coordonnee))


# On crée un canevas dans l'environnement Tkinter d'une taille de 500x500
# Ce constructeur prend comme premier paramètre l'objet dans lequel il sera
# intégré (ici l'environnement Tkinter)
# Les trois autres paramètres permettent de spécifier la taille et la couleur
# de fond du canevas
can = Canvas(tk, width=500, height=500, bg='black')

# On affiche le canevas
can.pack()

# Direction par défaut
direction = 'up' 

# Construction de la première étape de simulation
computeNextFrame(0,[200,200])

# Appuyer sur la touche 'd' appellera la fonction right()
tk.bind('<d>', right) 
tk.bind('<q>', left) 
tk.bind('<s>', down) 
tk.bind('<z>', up) 

# lancement de la boucle principale qui écoute les évènements (claviers...)
tk.mainloop() # Cet appel doit être la derniere instruction du programme




