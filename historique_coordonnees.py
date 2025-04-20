"historique_coordonnees.py contient une classe HistoriqueCoords qui enregistre les position de chaque membre du serpent pour chaque moment du jeu."

class HistoriqueCoords:
    "Historique des coordonnées de chaque membre du serpent."
    def __init__(self) -> None:
        "Constructeur de l'historique"

        # Contenu de l'historique
        self.contenu = {}


    def ajouter(self, coordonnees: list, n_mouvements:int) -> dict:
        """Ajoute les coordonnées fournies à l'historique et les associant à la clé n_mouvements.
        
        - n_mouvements: nombre de mouvements effectués par le serpent depuis le début du jeu."""

        # Assertions
        assert (type(n_mouvements).__name__ == "int"), "Le nombre de mouvements doit être un nombre entier."

        if n_mouvements <= 1:
            n_mouvements = 1

        self.contenu[n_mouvements] = coordonnees


    def coordonnees(self, n_mouvement:int) -> list:
        """Obtient et renvoie les coordonnées du serpent au mouvement n_mouvement. Renvoie une liste.
        n_mouvement est un entier. Si sa valeur est inférieure ou égale à la clé la plus petite, renvoie le contenu de cette dernière.
        Si la valeur est supérieure ou égale à la clé la plus grande, renvoie le contenu de cette dernière."""

        # Assertions
        assert (type(n_mouvement).__name__ == "int"), "Le numéro du mouvement doit être un nombre entier."

        # S'assurer que le numéro de la clé entre dans les limites de l'historique
        if n_mouvement <= 1:
            n_mouvement = 1

        elif n_mouvement > len(self.contenu):
            n_mouvement = len(self.contenu)

        # Finalement, renvoyer la liste de coordonnées correspondante
        return self.contenu[n_mouvement]        
