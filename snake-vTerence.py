"""
Programme Snake version Terence

"""
from tkinter import * # Importation de la bibliothèque  Tkinter 

# On crée un environnement Tkinter
tk = Tk()
   
# On crée un canevas dans l'environnement Tkinter d'une taille de 500x500
# Ce constructeur prend comme premier paramètre l'objet dans lequel il sera
# intégré (ici l'environnement Tkinter)
# Les trois autres paramètres permettent de spécifier la taille et la couleur
# de fond du canevas
can = Canvas(tk, width=500, height=500, bg='black')





# Calcule la nouvelle frame du jeu
def computeNextFrame(numFrame, coordonnee):
    # Affiche le numéro de la frame
    print(numFrame)
    numFrame = numFrame + 1
    
    # Effacer le canevas
    can.delete("all")
    
    # Mise à jour des coordonnées
    coordonnee += -20
    
    if coordonnee < 0:
        coordonnee = 0
    
    elif coordonnee > 500:
        coordonnee = 0
    
    # Dessin de la tête du serpent
    can.create_rectangle(coordonnee, 200, coordonnee + 20, 220, outline = "yellow", fill="red")
    
    
    # Calcule une nouvelle frame dans les 100 ms
    tk.after(100, lambda:computeNextFrame(numFrame, coordonnee))



# On affiche le canevas
can.pack()



def right(event):
    # Modification de la variable globale direction
    global direction
    direction = "right"
    print(direction)


direction = "up"


# Construction de la première étape de simulation
computeNextFrame(0, 500)

# Appuyer sur la touche "d" appellera la fonction right()
tk.bind("d", right)

# lancement de la boucle principale qui écoute les évènements (claviers...)
tk.mainloop() # Cet appel doit être la derniere instruction du programme





