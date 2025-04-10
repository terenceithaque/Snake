"""
Programme Snake version 3

"""
from tkinter import * # Importation de la bibliothèque  Tkinter 
from random import randint

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
def computeNextFrame(numFrame,coordonnee, objet):
    global direction
    # Affiche le numérod de la frame
    #print(numFrame)
    numFrame = numFrame + 1
    
    # Effacer le canevas
    can.delete('all')
    
    # Propagation du déplacement des noeuds
    for n in range (len(coordonnee)-1,0,-1):
        coordonnee[n][0] = coordonnee[n-1][0]
        coordonnee[n][1] = coordonnee[n-1][1]
        
    # Mise à jour des coordonnées
    if direction == 'right':
        coordonnee[0][0] += 20
        if coordonnee[0][0] > 480:
            coordonnee[0][0] = 0
    if direction == 'left':
        coordonnee[0][0] += -20
        if coordonnee[0][0] < 0:
            coordonnee[0][0] = 480
    if direction == 'up':
        coordonnee[0][1] += -20
        if coordonnee[0][1] < 0:
            coordonnee[0][1] = 480
    if direction == 'down':
        coordonnee[0][1] += 20
        if coordonnee[0][1] > 480:
            coordonnee[0][1] = 0

    # Dessin de la tête du serpent et de noeuds
    can.create_rectangle(coordonnee[0][0], coordonnee[0][1], coordonnee[0][0] + 20, 
                         coordonnee[0][1] + 20, outline='yellow', fill='red')
    
    for n in range(1,len(coordonnee)):
        if n%2 == 0: 
            ligne = 'blue'
            couleur = 'green'
        else:
            ligne = 'green'
            couleur = 'blue'
        can.create_rectangle(coordonnee[n][0], coordonnee[n][1], coordonnee[n][0] + 20, 
                         coordonnee[n][1] + 20, outline= ligne, fill= couleur)    
    # Dessine les objets
    for p in range(len(objet)):
        can.create_oval(objet[p][0], objet[p][1], objet[p][0] + 20, 
                         objet[p][1] + 20, outline= 'red', fill= 'green')   
 
    # Calcule une nouvelle frame dans 100 ms
    tk.after(100, lambda:computeNextFrame(numFrame,coordonnee, objet))


if __name__ == "__main__":
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
    
    coordonnee = [ [200, 200], [200, 220], [200, 240], [220, 240] ]
    objet = []
    
    # Premier objet (la pomme)
    x = randint(1,24)
    y = randint(1,24)
    objet.append([x*20, y*20, 0])
    
    # Construction de la première étape de simulation
    computeNextFrame(0,coordonnee, objet)
    
    # Appuyer sur la touche 'd' appellera la fonction right()
    tk.bind('<d>', right) 
    tk.bind('<q>', left) 
    tk.bind('<s>', down) 
    tk.bind('<z>', up) 
    
    # lancement de la boucle principale qui écoute les évènements (claviers...)
    tk.mainloop() # Cet appel doit être la derniere instruction du programme