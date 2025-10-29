from combat import lancer_combat
from pokemon import Pokemon

class Arene:
    def __init__(self, nom, type, badge, dresseurs):
        self.nom = nom
        self.type = type
        self.badge = badge
        self.dresseurs = dresseurs

    def demarrer_defi(self, equipe):
        print(f"\nBienvenue dans l'{self.nom} !")
        print(f"Type de l'arène : {self.type}")
        print("Tu devras battre tous les dresseurs pour obtenir le badge.")
        print("Les fuites sont interdites ici !")
        print("\nTon premier Pokémon se prépare à combattre...")

        for i, dresseur in enumerate(self.dresseurs, 1):
            print(f"\nÉtage {i} : tu affrontes {dresseur.nom} avec son {dresseur.pokemon.nom} ({dresseur.pokemon.type}) !")

            resultat = lancer_combat(equipe, dresseur.pokemon, choix_libre=False)

            if resultat != "victoire":
                print(f"\nTu as perdu contre {dresseur.nom} à l’étage {i}... Tu es expulsé de l’arène.")
                return False
            else:
                if i < len(self.dresseurs):
                    print(f"\nTu as battu {dresseur.nom} ! Tu montes à l’étage suivant...")
                    input("\n(Appuie sur Entrée pour continuer)")
                else:
                    print(f"\nTu as vaincu le champion {dresseur.nom} !")
                    print(f"\nFélicitations ! Tu remportes le badge {self.badge} !")
                    return True


class CombattantArene:
    def __init__(self, nom, pokemon):
        self.nom = nom
        self.pokemon = pokemon
