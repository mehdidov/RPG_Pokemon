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