import random

class Item:
    def __init__(self, nom):
        self.nom = nom

    def utiliser(self, pokemon=None, inventaire=None):
        pass


# --- Potion ---
class Potion(Item):
    def __init__(self):
        super().__init__("Potion")

    def utiliser(self, pokemon, inventaire):
        if not pokemon.est_vivant():
            print(f"{pokemon.nom} est K.O., tu ne peux pas utiliser une Potion.")
            return False

        if pokemon.soigner(20):
            print(f"{pokemon.nom} récupère 20 PV ! ({pokemon.pv}/{pokemon.pv_max})")
            inventaire.remove(self)
            return True
        else:
            print(f"{pokemon.nom} est déjà au maximum de ses PV.")
            return False


# --- Super Potion ---
class SuperPotion(Item):
    def __init__(self):
        super().__init__("Super Potion")

    def utiliser(self, pokemon, inventaire):
        if not pokemon.est_vivant():
            print(f"{pokemon.nom} est K.O., tu ne peux pas utiliser une Super Potion.")
            return False

        if pokemon.soigner(50):
            print(f"{pokemon.nom} récupère 50 PV ! ({pokemon.pv}/{pokemon.pv_max})")
            inventaire.remove(self)
            return True
        else:
            print(f"{pokemon.nom} est déjà au maximum de ses PV.")
            return False


# --- Rappel ---
class Revive(Item):
    def __init__(self):
        super().__init__("Rappel")

    def utiliser(self, pokemon, inventaire):
        if pokemon.est_vivant():
            print(f"{pokemon.nom} n’a pas besoin de Rappel.")
            return False
        pokemon.pv = pokemon.pv_max // 2
        print(f"{pokemon.nom} est réanimé à {pokemon.pv} PV !")
        inventaire.remove(self)
        return True


# --- Poké Ball ---
class PokeBall(Item):
    def __init__(self):
        super().__init__("Poké Ball")

    def utiliser(self, cible, inventaire):
        print(f"Tu lances une Poké Ball sur {cible.nom}...")
        chance_capture = random.random()
        inventaire.remove(self)
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
