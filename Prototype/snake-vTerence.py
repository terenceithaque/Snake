"""
Programme Snake version Terence

"""
from tkinter import * # Importation de la bibliothèque  Tkinter 

# On crée un environnement Tkinter
tk = Tk()
   






# Calcule la nouvelle frame du jeu
def computeNextFrame(numFrame, coordonnee):
    global direction
    # Affiche le numéro de la frame
    #print(numFrame, direction)
    numFrame = numFrame + 1
    
    # Effacer le canevas
    can.delete("all")
    
    x = coordonnee[0]
    y = coordonnee[1]
    
    # Mise à jour des coordonnées
    
    # Propagation du déplacement des noeuds
    for n in range(len(coordonnee) -1, 0, -1):
        coordonnee[n][0] = coordonnee[n-1][0]
        coordonnee[n][1] = coordonnee[n-1][1]
        
    """if direction == "up":
        y = y - 20
        #print("y:", y)
        
    elif direction == "down":
        y = y + 20
        #print("y:", y)
        
    elif direction == "right":
        x = x + 20
        #print("x:", x)
        
    elif direction == "left":
        x = x - 20
        #print("x:", x)
    
    # Si le serpent sort d'un côté de l'écran, il revient automatiquement par le côté opposé
    if x < 0:
        x = 500
    
    elif x > 500:
        x = 0
        
    if y < 0:
        y = 500
        
    elif y > 500:
        y = 0"""
    # Dessin de la tête du serpent
    can.create_rectangle(x, y, x + 20, y+20, outline = "yellow", fill="red")
    
    
    # Calcule une nouvelle frame dans les 100 ms
    tk.after(100, lambda:computeNextFrame(numFrame, [x, y]))







def right(event):
    # Modification de la variable globale direction
    global direction
    direction = "right"
    #print(direction)
    
    
def left(event):
    global direction
    direction = "left"
    #print(direction)
    
def down(event):
    global direction
    direction = "down"
    #print(direction)

def up(event):
    global direction
    direction = "up"
    #print(direction)



if __name__ == "__main__":
    # On crée un canevas dans l'environnement Tkinter d'une taille de 500x500
    # Ce constructeur prend comme premier paramètre l'objet dans lequel il sera
    # intégré (ici l'environnement Tkinter)
    # Les trois autres paramètres permettent de spécifier la taille et la couleur
    # de fond du canevas
    can = Canvas(tk, width=500, height=500, bg='black')
    # On affiche le canevas
    can.pack()
    
    
    direction = "up"
    
    # Coordonnées de chaque noeud du serpent (x, y)
    # En déplacement, elles doivent se propager: les coordonnées du noeud 3 deviennent celles du noeud 2
    # et celles du noeud 2 deviennent celles du noeud 1.
    # Enfin, les coordonnées du noeud 0 (la tête) sont modifiées selon la direction.
    coordonnee = [[200, 200], [200, 220], [200, 240], [220, 240]]


    # Construction de la première étape de simulation
    computeNextFrame(0, coordonnee)

    # Appuyer sur la touche "d" appellera la fonction right()
    tk.bind("<d>", right)

    # Appuyer sur la touche "q" appellera la fonction left()
    tk.bind("<q>", left)

    # Appuyer sur la touche "s" appellera la fonction down()
    tk.bind("<s>", down)

    # Appuyer sur la touche "z" appellera la fonction up()
    tk.bind("<z>", up)

    # lancement de la boucle principale qui écoute les évènements (claviers...)
    tk.mainloop() # Cet appel doit être la derniere instruction du programme





