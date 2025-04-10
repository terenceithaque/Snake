"""
Programme Snake version 5

"""
from tkinter import * # Importation de la bibliothèque  Tkinter 
from tkinter import font as tkfont
from random import randint

from PIL import Image, ImageTk 
# On crée un environnement Tkinter
tk = Tk()
im_teteN = Image.open("../assets/teteN.png") 
teteN = ImageTk.PhotoImage(im_teteN) 
im_teteS = Image.open("../assets/teteS.png") 
teteS = ImageTk.PhotoImage(im_teteS) 
im_teteE = Image.open("../assets/teteE.png") 
teteE = ImageTk.PhotoImage(im_teteE) 
im_teteW = Image.open("../assets/teteW.png") 
teteW = ImageTk.PhotoImage(im_teteW) 
im_noeud1 = Image.open("../assets/noeud1.png") 
noeud1 = ImageTk.PhotoImage(im_noeud1) 
im_noeud2 = Image.open("../assets/noeud2.png") 
noeud2 = ImageTk.PhotoImage(im_noeud2)
pomme = Image.open("../assets/pomme.png") 
pomme = ImageTk.PhotoImage(pomme)

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
        can.create_image(coordonnee[0][0], coordonnee[0][1], anchor = NW, image = teteE)
        if coordonnee[0][0] > 480:
            coordonnee[0][0] = 0
    if direction == 'left':
        coordonnee[0][0] += -20
        can.create_image(coordonnee[0][0], coordonnee[0][1], anchor = NW, image = teteW)
        if coordonnee[0][0] < 0:
            coordonnee[0][0] = 480
    if direction == 'up':
        coordonnee[0][1] += -20
        can.create_image(coordonnee[0][0], coordonnee[0][1], anchor = NW, image = teteN)
        if coordonnee[0][1] < 0:
            coordonnee[0][1] = 480
    if direction == 'down':
        coordonnee[0][1] += 20
        can.create_image(coordonnee[0][0], coordonnee[0][1], anchor = NW, image = teteS)
        if coordonnee[0][1] > 480:
            coordonnee[0][1] = 0

    
    for n in range(1,len(coordonnee)):
        if n%2 == 0: 
            can.create_image(coordonnee[n][0], coordonnee[n][1], anchor = NW, image = noeud1)
        else:
            can.create_image(coordonnee[n][0], coordonnee[n][1], anchor = NW, image = noeud2)
        
    # Dessine les objets
    for p in range(len(objet)):
        can.create_image(objet[0][0], objet[0][1], anchor = NW, image = pomme)   
        
    for p in range(len(objet)):
        if coordonnee[0][0] == objet [0][0] and coordonnee[p][1] == objet [p][1]:
            # Déplacement de la pomme
            objet[0][0] = randint(1,24)* 20
            objet[0][1] = randint(1,24)* 20
            # Ajout d'un noeud au serpent (à la même place que le dernier noeud)
            coordonnee.append([-20, -20]) # Caché pour l'instant

    game_over = False     
    # On test la position de la tête par rapport aux noeuds du serpent
    for n in range(1,len(coordonnee)): # L'indice 0 est exclu, c'est la tête
        if coordonnee[0][0] == coordonnee [n][0] and coordonnee[p][1] == coordonnee [n][1]:
            game_over = True # La partie est finie
            
    if game_over : 
        # Fin de partie
        TEXTE = "GAME OVER"
        normal_font = tkfont.Font(family="Helvetica", size=12, weight="bold")
        can.create_text(100,200,text = TEXTE, fill='red',  font=normal_font)
    else:
        # La partie n'est pas finie
        # Calcule une nouvelle frame dans 100 ms
        tk.after(50, lambda:computeNextFrame(numFrame,coordonnee, objet))


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