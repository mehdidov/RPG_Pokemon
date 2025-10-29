import random
class Item:
    def __init__(self, nom, description):
        self.nom = nom
        self.description = description

    def utiliser(self, pokemon):
        pass

class Potion(Item):
    def __init__(self):
        super().__init__("Potion", "Restaure 20 PV à un Pokémon")

    def utiliser(self, pokemon):
        if pokemon.pv == pokemon.pv_max:
            print(f"{pokemon.nom} a déjà tous ses PV.")
        else:
            pokemon.soigner(20)
            print(f"Tu utilises une Potion sur {pokemon.nom} !")

class SuperPotion(Item):
    def __init__(self):
        super().__init__("Super Potion", "Restaure 50 PV à un Pokémon")

    def utiliser(self, pokemon):
        if pokemon.pv == pokemon.pv_max:
            print(f"{pokemon.nom} a déjà tous ses PV.")
        else:
            pokemon.soigner(50)
            print(f"Tu utilises une Super Potion sur {pokemon.nom} !")

class Revive(Item):
    def __init__(self):
        super().__init__("Rappel", "Ranime un Pokémon K.O. à moitié de ses PV")

    def utiliser(self, pokemon):
        if pokemon.est_vivant():
            print(f"{pokemon.nom} est déjà en pleine forme.")
        else:
            pokemon.pv = pokemon.pv_max // 2
            print(f"{pokemon.nom} est ranimé avec {pokemon.pv} PV !")


class PokeBall(Item):
    def __init__(self):
        super().__init__("Poké Ball", "Permet de capturer un Pokémon sauvage")

    def utiliser(self, pokemon_sauvage):
        # Simule la probabilité de capture
        chance_capture = random.random()
        taux_base = 0.35  # 35 % de base
        if pokemon_sauvage.pv < pokemon_sauvage.pv_max * 0.3:
            taux_base += 0.25  # bonus si affaibli

        if chance_capture < taux_base:
            print(f"Le {pokemon_sauvage.nom} est capturé avec succès !")
            return True
        else:
            print(f"{pokemon_sauvage.nom} s’est échappé de la Poké Ball...")
            return False