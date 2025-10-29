from combat import lancer_combat
from items import afficher_inventaire

class CombattantArene:
    def __init__(self, nom, pokemon):
        self.nom = nom
        self.pokemon = pokemon


class Arene:
    def __init__(self, nom, type_, badge, dresseurs):
        self.nom = nom
        self.type = type_
        self.badge = badge
        self.dresseurs = dresseurs

    def demarrer_defi(self, equipe, inventaire):
        print(f"\nBienvenue dans l'{self.nom} ! Type : {self.type}")
        for i, dresseur in enumerate(self.dresseurs, 1):
            print(f"\nÉtage {i} : {dresseur.nom} t’attend avec {dresseur.pokemon.nom} !")
            resultat = lancer_combat(equipe, dresseur.pokemon, inventaire)
            if resultat != "victoire":
                print(f"\nTu as perdu contre {dresseur.nom}.")
                return False
            if i < len(self.dresseurs):
                print("\nSouhaites-tu faire quelque chose avant le prochain combat ?")
                print("1. Utiliser un objet")
                print("2. Continuer")
                choix = input("-> ").strip()
                if choix == "1":
                    afficher_inventaire(inventaire)
        print(f"\nTu as vaincu tous les dresseurs et remporté le badge {self.badge} !")
        return True
