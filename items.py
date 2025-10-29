import random

class Item:
    def __init__(self, nom):
        self.nom = nom

    def utiliser(self, pokemon, inventaire):
        """Méthode générique à surcharger dans les sous-classes"""
        pass


class Potion(Item):
    def __init__(self):
        super().__init__("Potion")

    def utiliser(self, pokemon, inventaire):
        if pokemon.est_vivant():
            soin = 20
            avant = pokemon.pv
            pokemon.pv = min(pokemon.pv + soin, pokemon.pv_max)
            print(f"{pokemon.nom} regagne {pokemon.pv - avant} PV ! ({pokemon.pv}/{pokemon.pv_max})")
            inventaire.remove(self)
        else:
            print(f"{pokemon.nom} est K.O. ! Utilise plutôt un Rappel.")


class SuperPotion(Item):
    def __init__(self):
        super().__init__("Super Potion")

    def utiliser(self, pokemon, inventaire):
        if pokemon.est_vivant():
            soin = 50
            avant = pokemon.pv
            pokemon.pv = min(pokemon.pv + soin, pokemon.pv_max)
            print(f"{pokemon.nom} regagne {pokemon.pv - avant} PV ! ({pokemon.pv}/{pokemon.pv_max})")
            inventaire.remove(self)
        else:
            print(f"{pokemon.nom} est K.O. ! Utilise plutôt un Rappel.")


class Revive(Item):
    def __init__(self):
        super().__init__("Rappel")

    def utiliser(self, pokemon, inventaire):
        if not pokemon.est_vivant():
            pokemon.pv = pokemon.pv_max // 2
            print(f"{pokemon.nom} est réanimé avec {pokemon.pv} PV !")
            inventaire.remove(self)
        else:
            print(f"{pokemon.nom} est déjà en pleine forme.")



class PokeBall(Item):
    def __init__(self):
        super().__init__("Poké Ball")

    def utiliser(self, pokemon, inventaire):
        chance_capture = random.random()
        inventaire.remove(self)
        return chance_capture < 0.6
