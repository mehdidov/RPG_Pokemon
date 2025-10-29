from combat import lancer_combat
from pokemon import Pokemon
from items import Potion, SuperPotion, Revive, PokeBall


class Arene:
    def __init__(self, nom, type, badge, dresseurs):
        self.nom = nom
        self.type = type
        self.badge = badge
        self.dresseurs = dresseurs

    def demarrer_defi(self, equipe, inventaire):
        print(f"\nBienvenue dans l'{self.nom} !")
        print(f"Type de l'arène : {self.type}")
        print("Tu devras battre tous les dresseurs pour obtenir le badge.")
        print("Les fuites sont interdites ici !")
        print("\nTon premier Pokémon se prépare à combattre...")

        for i, dresseur in enumerate(self.dresseurs, 1):
            print(f"\nÉtage {i} : tu affrontes {dresseur.nom} avec son {dresseur.pokemon.nom} ({dresseur.pokemon.type}) !")

            # === AJOUT : menu avant le combat ===
            while True:
                print("\nQue veux-tu faire avant le combat ?")
                print("1. Affronter le dresseur")
                print("2. Utiliser un objet")
                print("3. Voir ton équipe")
                choix_precombat = input("-> ")

                if choix_precombat == "1":
                    break

                elif choix_precombat == "2":
                    if not inventaire:
                        print("Ton sac est vide !")
                        continue

                    print("\nObjets disponibles :")
                    for j, item in enumerate(inventaire, 1):
                        print(f"{j}. {item.nom} - {item.description}")

                    choix_objet = input("\nQuel objet veux-tu utiliser ? (numéro ou 0 pour annuler) -> ")
                    if choix_objet.isdigit():
                        choix_objet = int(choix_objet)
                        if choix_objet == 0:
                            continue
                        elif 1 <= choix_objet <= len(inventaire):
                            objet = inventaire[choix_objet - 1]

                            # Si c’est un objet de soin
                            if isinstance(objet, (Potion, SuperPotion, Revive)):
                                print("\nSur quel Pokémon veux-tu l’utiliser ?")
                                for k, p in enumerate(equipe, 1):
                                    print(f"{k}. {p.nom} ({p.pv}/{p.pv_max} PV)")
                                choix_poke = input("-> ")
                                if choix_poke.isdigit():
                                    choix_poke = int(choix_poke)
                                    if 1 <= choix_poke <= len(equipe):
                                        objet.utiliser(equipe[choix_poke - 1])
                                        inventaire.remove(objet)
                                    else:
                                        print("Numéro invalide.")
                                else:
                                    print("Entrée invalide.")
                            else:
                                print("Cet objet ne peut pas être utilisé ici.")
                        else:
                            print("Choix invalide.")
                    else:
                        print("Entrée invalide.")
                    continue  # Repropose le menu avant combat

                elif choix_precombat == "3":
                    print("\nTon équipe actuelle :")
                    for j, p in enumerate(equipe, 1):
                        print(f"{j}. {p.nom} ({p.type}) - {p.pv}/{p.pv_max} PV")
                    continue

                else:
                    print("Choix invalide.")
                    continue

            # === Combat ===
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
