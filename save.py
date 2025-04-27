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



def sauvegarder_partie(points:int, max_points:int, ligne_tete:int, col_tete:int, taille_serpent:int, direction_serpent:int) -> None:
    """Sauvegarde l'entièreté de l'état du jeu à un moment donné au format JSON"""
    # Dictionnaire de l'état du jeu
    etat =  {"points":points,
             "max_points":max_points,
             "ligne_tete":ligne_tete,
             "col_tete":col_tete,
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


def recuperer_partie() -> dict:
    """Récupère les données de la partie sauvegardée au format JSON.
     Si l'état du jeu est irrécupérrable, il est remis à zéro. Renvoie un dictionnaire."""

    # Construire déjà le dictionnaire à partir des données de départ d'une nouvelle partie
    # ce qui permet de remettre l'état du jeu à zéro si le fichier de sauvegarde est introuvable
    etat =  {"points":0,
             "max_points":0,
             "ligne_tete":7,
             "col_tete":7,
             "taille_serpent":5,
             "direction_serpent":"gauche"}

    # Dossier courant
    dossier = os.path.dirname(os.path.abspath(__file__))

    # Fichier de sauvegarde
    fichier = os.path.join(dossier, "save.json")

    # Tenter d'ouvrir le fichier
    try:
        with open(fichier, "r") as f:
            etat = json.load(f)

    except:
        pass

    return etat           




        
