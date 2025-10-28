class Pokemon:
    
    def __init__(self, nom, type, pv, attaque):
        self.nom = nom              # Nom du Pokémon
        self.type = type          # Type : Feu / Eau / Plante
        self.pv_max = pv            # Points de vie maximum
        self.pv = pv                # Points de vie actuels
        self.attaque = attaque      # Puissance d'attaque

    def est_vivant(self):
        return self.pv > 0
    
    def attaquer(self, autre):
        print(f"\n{self.nom} attaque {autre.nom} !")
        autre.pv -= self.attaque
        if autre.pv < 0:
            autre.pv = 0
        print(f"{autre.nom} a maintenant {autre.pv} PV.")

    
    def soigner(self, montant):
        self.pv = min(self.pv + montant, self.pv_max)
        print(f"{self.nom} récupère {montant} PV. ({self.pv}/{self.pv_max})")


class PokemonFeu(Pokemon):
    def __init__(self):
        super().__init__("Poussifeu", "Feu", 41, 10)

class PokemonEau(Pokemon):
    def __init__(self):
        super().__init__("Grenouss", "Eau", 42, 9)

class PokemonPlante(Pokemon):
    def __init__(self):
        super().__init__("Bulbizarre", "Plante", 40, 11)