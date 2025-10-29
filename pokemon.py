import random

class Pokemon:
    def __init__(self, nom, type_, pv_max, attaques, niveau=5, evolution=None, niveau_evolution=None):
        self.nom = nom
        self.type = type_
        self.pv_max = pv_max
        self.pv = pv_max
        self.attaques = attaques
        self.niveau = niveau
        self.xp = 0
        self.evolution = evolution
        self.niveau_evolution = niveau_evolution

    def est_vivant(self):
        return self.pv > 0

    def subir_degats(self, degats):
        self.pv = max(0, self.pv - degats)

    def soigner(self, quantite=None):
        if quantite is None:
            if self.pv == self.pv_max:
                return False
            self.pv = self.pv_max
            return True
        else:
            avant = self.pv
            self.pv = min(self.pv_max, self.pv + quantite)
            return self.pv > avant

    def choisir_attaque(self):
        print("\nChoisis une attaque :")
        for i, (nom, puissance) in enumerate(self.attaques, 1):
            print(f"{i}. {nom} ({puissance} dégâts)")
        choix = input("-> ").strip()
        if choix.isdigit() and 1 <= int(choix) <= len(self.attaques):
            return self.attaques[int(choix) - 1]
        else:
            print("Choix invalide. Attaque par défaut utilisée.")
            return self.attaques[0]

    def gagner_xp(self, quantite):
        self.xp += quantite
        xp_necessaire = 100 * self.niveau
        if self.xp >= xp_necessaire:
            self.niveau += 1
            self.xp = 0
            self.pv_max += 5
            self.pv = self.pv_max
            print(f"\n⭐ {self.nom} passe au niveau {self.niveau} ! PV max +5")
            if self.evolution and self.niveau_evolution and self.niveau >= self.niveau_evolution:
                self.evoluer()

    def evoluer(self):
        if not self.evolution:
            return
        ancien_nom = self.nom
        self.nom = self.evolution
        self.pv_max += 10
        self.pv = self.pv_max
        print(f"\n✨ {ancien_nom} évolue en {self.nom} ! ✨")


class PokemonFeu(Pokemon):
    def __init__(self):
        super().__init__(
            "Poussifeu", "Feu", 40,
            [("Flammèche", 10), ("Griffe", 8), ("Charge", 6), ("Danseflamme", 12)],
            niveau=5, evolution="Galifeu", niveau_evolution=16
        )


class PokemonEau(Pokemon):
    def __init__(self):
        super().__init__(
            "Grenouss", "Eau", 40,
            [("Pistolet à O", 10), ("Charge", 6), ("Bulles d’O", 8), ("Écume", 7)],
            niveau=5, evolution="Croâporal", niveau_evolution=16
        )


class PokemonPlante(Pokemon):
    def __init__(self):
        super().__init__(
            "Bulbizarre", "Plante", 42,
            [("Fouet Lianes", 10), ("Charge", 6), ("Tranch’Herbe", 12), ("Vampigraine", 0)],
            niveau=5, evolution="Herbizarre", niveau_evolution=16
        )
