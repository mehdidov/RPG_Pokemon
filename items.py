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
        soin = 20
        avant = pokemon.pv
        pokemon.soigner(soin)
        inventaire.remove(self)
        print(f"{pokemon.nom} récupère {pokemon.pv - avant} PV grâce à une Potion !")


class SuperPotion(Item):
    def __init__(self):
        super().__init__("Super Potion")

    def utiliser(self, pokemon, inventaire):
        soin = 50
        avant = pokemon.pv
        pokemon.soigner(soin)
        inventaire.remove(self)
        print(f"{pokemon.nom} récupère {pokemon.pv - avant} PV grâce à une Super Potion !")


class Revive(Item):
    def __init__(self):
        super().__init__("Rappel")

    def utiliser(self, pokemon, inventaire):
        if pokemon.est_vivant():
            print(f"{pokemon.nom} n’est pas K.O., le rappel ne sert à rien.")
            return
        pokemon.pv = pokemon.pv_max // 2
        inventaire.remove(self)
        print(f"{pokemon.nom} est réanimé avec {pokemon.pv} PV !")


class PokeBall(Item):
    def __init__(self):
        super().__init__("Poké Ball")

    def utiliser(self, pokemon, inventaire):
        chance_capture = random.random()
        inventaire.remove(self)
        return chance_capture < 0.6
