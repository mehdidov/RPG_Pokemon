import random

class Pokemon:
    def __init__(self, nom, type, pv, attaque):
        self.nom = nom
        self.type = type
        self.pv_max = pv
        self.pv = pv
        self.attaque = attaque
        self.attaques = [
            {"nom": "Charge", "puissance": 5, "type": "Normal"},
            {"nom": "Morsure", "puissance": 7, "type": "Normal"}
        ]

     

    def attaquer(self, autre, attaque_choisie=None):
        
        if attaque_choisie is None:
            attaque_choisie = random.choice(self.attaques)

        print(f"\n{self.nom} utilise {attaque_choisie['nom']} !")

        degats = attaque_choisie['puissance']
        autre.pv -= degats
        if autre.pv < 0:
            autre.pv = 0

        print(f"{autre.nom} a maintenant {autre.pv} PV.")

    def est_vivant(self):
        return self.pv > 0

    def soigner(self, montant):
        self.pv = min(self.pv + montant, self.pv_max)
        print(f"{self.nom} récupère {montant} PV. ({self.pv}/{self.pv_max})")


class PokemonFeu(Pokemon):
    def __init__(self):
        super().__init__("Poussifeu", "Feu", 41, 10)
        self.attaques = [
            {"nom": "Flammèche", "puissance": 10, "type": "Feu"},
            {"nom": "Griffe", "puissance": 6, "type": "Normal"}
        ]

class PokemonEau(Pokemon):
    def __init__(self):
        super().__init__("Grenouss", "Eau", 42, 9)
        self.attaques = [
            {"nom": "Pistolet à O", "puissance": 9, "type": "Eau"},
            {"nom": "Charge", "puissance": 7, "type": "Normal"}
        ]

class PokemonPlante(Pokemon):
    def __init__(self):
        super().__init__("Bulbizarre", "Plante", 40, 11)
        self.attaques = [
            {"nom": "Fouet Lianes", "puissance": 9, "type": "Plante"},
            {"nom": "Charge", "puissance": 7, "type": "Normal"}
        ]