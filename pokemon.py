import random

class Pokemon:
    def __init__(self, nom, type_, pv_max, attaques):
        self.nom = nom
        self.type = type_
        self.pv_max = pv_max
        self.pv = pv_max
        self.attaques = attaques  # Liste de tuples (nom, puissance)

    def est_vivant(self):
        return self.pv > 0

    def soigner(self, montant):
        if self.pv == self.pv_max:
            print(f"{self.nom} a déjà tous ses PV.")
            return False
        avant = self.pv
        self.pv = min(self.pv + montant, self.pv_max)
        print(f"{self.nom} est soigné ({avant} → {self.pv} PV).")
        return True

    def subir_degats(self, degats):
        self.pv = max(0, self.pv - degats)

    def choisir_attaque(self):
        print("\nChoisis une attaque :")
        for i, (nom, puissance) in enumerate(self.attaques, 1):
            print(f"{i}. {nom} (puissance {puissance})")

        while True:
            choix = input("-> ").strip()
            if choix.isdigit() and 1 <= int(choix) <= len(self.attaques):
                return self.attaques[int(choix) - 1]
            else:
                print("Choix invalide.")

# Pokémons de base
class PokemonFeu(Pokemon):
    def __init__(self):
        attaques = [("Griffe", 10), ("Flammèche", 12), ("Crocs Feu", 15), ("Danseflamme", 18)]
        super().__init__("Poussifeu", "Feu", 41, attaques)

class PokemonEau(Pokemon):
    def __init__(self):
        attaques = [("Écume", 10), ("Pistolet à O", 12), ("Coup de Queue", 14), ("Hydroqueue", 18)]
        super().__init__("Grenouss", "Eau", 40, attaques)

class PokemonPlante(Pokemon):
    def __init__(self):
        attaques = [("Fouet Lianes", 10), ("Tranch’Herbe", 12), ("Canon Graine", 15), ("Vampigraine", 18)]
        super().__init__("Bulbizarre", "Plante", 42, attaques)
