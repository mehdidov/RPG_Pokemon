# On importe les fonctions nécessaires
from combat import lancer_combat   # Sert à lancer un combat contre un dresseur
from items import afficher_inventaire   # Sert à afficher le sac du joueur


# --- Classe représentant un dresseur dans une arène ---
class CombattantArene:
    def __init__(self, nom, pokemon):
        # Chaque dresseur a un nom et un Pokémon
        self.nom = nom
        self.pokemon = pokemon


# --- Classe représentant une arène complète ---
class Arene:
    def __init__(self, nom, type_, badge, dresseurs):
        # Chaque arène a un nom, un type, un badge et une liste de dresseurs à affronter
        self.nom = nom
        self.type = type_
        self.badge = badge
        self.dresseurs = dresseurs

    # Fonction principale pour démarrer le défi dans l’arène
    def demarrer_defi(self, equipe, inventaire):
        print(f"\nBienvenue dans l'{self.nom} ! Type : {self.type}")

        # Boucle sur tous les dresseurs de l’arène
        for i, dresseur in enumerate(self.dresseurs, 1):
            print(f"\nÉtage {i} : {dresseur.nom} t’attend avec {dresseur.pokemon.nom} !")

            # On lance un combat contre le dresseur
            resultat = lancer_combat(equipe, dresseur.pokemon, inventaire)

            # Si le joueur perd, le défi s'arrête
            if resultat != "victoire":
                print(f"\nTu as perdu contre {dresseur.nom}.")
                return False

            # Si le joueur gagne et qu’il reste encore des dresseurs à battre
            if i < len(self.dresseurs):
                print("\nSouhaites-tu faire quelque chose avant le prochain combat ?")
                print("1. Utiliser un objet")
                print("2. Continuer")
                choix = input("-> ").strip()
                # Le joueur peut accéder à son inventaire entre deux combats
                if choix == "1":
                    afficher_inventaire(inventaire)

        # Si tous les dresseurs sont vaincus → badge gagné
        print(f"\nTu as vaincu tous les dresseurs et remporté le badge {self.badge} !")
        return True
