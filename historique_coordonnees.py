"historique_coordonnees.py contient une classe HistoriqueCoords qui enregistre les position de chaque membre du serpent pour chaque moment du jeu."

class HistoriqueCoords:
    "Historique des coordonnées de chaque membre du serpent."
    def __init__(self) -> None:
        "Constructeur de l'historique"

        # Contenu de l'historique
        self.contenu = {}