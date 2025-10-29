import random

class Item:
    def __init__(self, nom):
        self.nom = nom

    def utiliser(self, pokemon=None, inventaire=None):
        pass


class Potion(Item):
    def __init__(self):
        super().__init__("Potion")

    def utiliser(self, pokemon, inventaire):
        if pokemon.soigner(20):
            inventaire.remove(self)
            print(f"{pokemon.nom} profite de {self.nom} !")


class SuperPotion(Item):
    def __init__(self):
        super().__init__("Super Potion")

    def utiliser(self, pokemon, inventaire):
        if pokemon.soigner(50):
            inventaire.remove(self)
            print(f"{pokemon.nom} profite de {self.nom} !")


class Revive(Item):
    def __init__(self):
        super().__init__("Rappel")

    def utiliser(self, pokemon, inventaire):
        if pokemon.est_vivant():
            print(f"{pokemon.nom} n’a pas besoin de Rappel.")
            return
        pokemon.pv = pokemon.pv_max // 2
        inventaire.remove(self)
        print(f"{pokemon.nom} est réanimé à {pokemon.pv} PV !")


class PokeBall(Item):
    def __init__(self):
        super().__init__("Poké Ball")

    def utiliser(self, cible, inventaire):
        print(f"Tu lances une Poké Ball sur {cible.nom}...")
        inventaire.remove(self)
        chance_capture = random.random()
        if chance_capture < 0.5:
            print(f"✨ {cible.nom} est capturé !")
            return True
        else:
            print(f"{cible.nom} s’est échappé de la Poké Ball !")
            return False


def afficher_inventaire(inventaire):
    if not inventaire:
        print("\nTon sac est vide.")
        return

    print("\n🎒 Inventaire :")
    compteur = {}
    for item in inventaire:
        compteur[item.nom] = compteur.get(item.nom, 0) + 1

    for nom, qte in compteur.items():
        print(f"- {nom} x{qte}")


def utiliser_objet_en_combat(inventaire, equipe, pokemon_joueur):
    compteur = {}
    for item in inventaire:
        compteur[item.nom] = compteur.get(item.nom, 0) + 1

    print("\nObjets disponibles :")
    objets_uniques = list(compteur.keys())
    for i, nom in enumerate(objets_uniques, 1):
        print(f"{i}. {nom} x{compteur[nom]}")

    choix_obj = input("-> ").strip()
    if not choix_obj.isdigit() or not (1 <= int(choix_obj) <= len(objets_uniques)):
        print("Choix invalide.")
        return

    objet_nom = objets_uniques[int(choix_obj) - 1]
    for item in inventaire:
        if item.nom == objet_nom:
            item.utiliser(pokemon_joueur, inventaire)
            break
