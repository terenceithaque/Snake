"save.py gère les sauvegardes au format JSON"
import os
import json

def sauvegarder_score(score=0) -> None:
    """Sauvegarde le score au format JSON"""
    # Dossier du script courant
    dossier = os.path.dirname(os.path.abspath(__file__))
    # Chemin du fichier de sauvegarde
    chemin_fichier = os.path.join(dossier, "score.json")

    # Ouvrir le fichier de sauvegarde en écriture
    with open(chemin_fichier, "w") as f:
        json.dump(score, f)



def recuperer_score() -> int:
    """Récupère le score depuis le fichier de sauvegarde JSON. Si le fichier n'existe pas, renvoie 0."""

    score = 0

    # Dossier du script courant
    dossier = os.path.dirname(os.path.abspath(__file__))
    # Chemin du fichier de sauvegarde
    chemin_fichier = os.path.join(dossier, "score.json")

    # Ouvrir le ficher en lecture
    if os.path.exists(chemin_fichier):
        with open(chemin_fichier, "r") as f:
            score = json.load(f)
    
    return score



def sauvegarder_partie(points:int, max_points:int, taille_serpent:int, direction_serpent:int) -> None:
    """Sauvegarde l'entièreté de l'état du jeu à un moment donné au format JSON"""
    # Dictionnaire de l'état du jeu
    etat =  {"points":points,
             "max_points":max_points,
             "taille_serpent": taille_serpent,
             "direction_serpent": direction_serpent}
    
    # Dossier courant
    dossier = os.path.dirname(os.path.abspath(__file__))

    # Fichier de sauvegarde
    fichier = os.path.join(dossier, "save.json")

    # Ouvrir le fichier de sauvegarde en écriture
    with open(fichier, "w") as f:
        # Enregistrer l'état actuel du jeu dans le fichier
        json.dump(etat, f)




        
