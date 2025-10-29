from combat import lancer_combat
from pokemon import Pokemon

class Arene :
    def __init__(self, nom, type, badge, dresseurs ):
        self.nom = nom
        self.type= type
        self.badge = badge
        self.dresseurs = dresseurs

    def demarrer_defi(self, equipe) :
        print(f"\nDébut du défi de l'{self.nom} !")
        print("Ton premier Pokémon se prépare à combattre")

        etage = 0
        while etage < len(self.dresseurs):
            dresseur = self.dresseurs[etage]
            print(f"\nÉtage {etage + 1} : tu affrontes {dresseur.nom} avec son {dresseur.pokemon.nom} ({dresseur.pokemon.type}) !")

            print("\nQue veux-tu faire ?")
            print("1. Affronter ce dresseur")
            if etage > 0:
                print("2. Descendre d’un étage")
            else:
                print("2. Quitter l’arène")

            choix = input("-> ")

            if choix == "2":
                if etage == 0:
                    print("\nTu quittes l’arène pour te reposer et t’entraîner davantage.")
                    return False  # sortie complète
                else:
                    etage -= 1
                    print(f"\nTu redescends prudemment à l’étage {etage + 1}...")
                    continue

            elif choix != "1":
                print("Choix invalide. Essaie encore.")
                continue
        
            resultat = lancer_combat(equipe, dresseur.pokemon, choix_libre=False)

            if resultat != "victoire":
                print(f"\nTu as perdu contre {dresseur.nom} à l’étage {etage + 1}... Tu es expulsé de l’arène.")
                return False
            else:
                print(f"\nTu as battu {dresseur.nom} !")

                # AJOUT : pause et narration avant de monter au prochain étage
                if etage < len(self.dresseurs) - 1:
                    print("\nTu reprends ton souffle avant de gravir les marches vers le prochain étage...")
                    input("\n(Appuie sur Entrée pour continuer)")
                    etage += 1
                else:
                    print(f"\nTu as vaincu le champion {dresseur.nom} !")
                    print(f"\nFélicitations ! Tu remportes le badge {self.badge} !")
                    return True

        
        
class CombattantArene : 
    def __init__(self, nom, pokemon):
        self.nom = nom
        self.pokemon = pokemon

