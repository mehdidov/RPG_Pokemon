import random

# =====================================================
# CLASSE PRINCIPALE : POKÉMON
# =====================================================
class Pokemon:
    def __init__(self, nom, type_, pv_max, attaques, niveau=5, evolution=None, niveau_evolution=None):
        # Nom du Pokémon (ex : Poussifeu, Grenouss, Bulbizarre)
        self.nom = nom
        # Type du Pokémon (Feu, Eau, Plante, etc.)
        self.type = type_
        # Points de vie maximum
        self.pv_max = pv_max
        # Points de vie actuels (commence au max)
        self.pv = pv_max
        # Liste des attaques (nom + puissance)
        self.attaques = attaques
        # Niveau actuel
        self.niveau = niveau
        # Expérience actuelle
        self.xp = 0
        # Nom de l’évolution (si le Pokémon peut évoluer)
        self.evolution = evolution
        # Niveau requis pour évoluer
        self.niveau_evolution = niveau_evolution

    # Vérifie si le Pokémon est encore en vie
    def est_vivant(self):
        return self.pv > 0

    # Réduit les PV du Pokémon lorsqu’il subit des dégâts
    def subir_degats(self, degats):
        self.pv = max(0, self.pv - degats)

    # Soigne le Pokémon
    def soigner(self, quantite=None):
        # Si aucune quantité précisée, on soigne à fond
        if quantite is None:
            if self.pv == self.pv_max:
                return False  # Rien à soigner
            self.pv = self.pv_max
            return True
        else:
            # On soigne partiellement (ex : Potion, Super Potion)
            avant = self.pv
            self.pv = min(self.pv_max, self.pv + quantite)
            return self.pv > avant  # True si le soin a bien augmenté les PV

    # Permet au joueur de choisir une attaque
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

    # Gérer l’expérience et le passage de niveau
    def gagner_xp(self, quantite):
        self.xp += quantite
        xp_necessaire = 100 * self.niveau  # Ex : niveau 5 → 500 XP nécessaires
        if self.xp >= xp_necessaire:
            self.niveau += 1
            self.xp = 0
            self.pv_max += 5  # Augmente les PV max à chaque montée de niveau
            self.pv = self.pv_max  # Restaure les PV au max
            print(f"\n⭐ {self.nom} passe au niveau {self.niveau} ! PV max +5")

            # Vérifie si le Pokémon peut évoluer
            if self.evolution and self.niveau_evolution and self.niveau >= self.niveau_evolution:
                self.evoluer()

    # Gérer l’évolution du Pokémon
    def evoluer(self):
        if not self.evolution:
            return  # Si pas d’évolution prévue, on quitte

        ancien_nom = self.nom
        self.nom = self.evolution
        self.pv_max += 10
        self.pv = self.pv_max
        print(f"\n✨ {ancien_nom} évolue en {self.nom} ! ✨")


# =====================================================
# POKÉMON DE DÉPART
# =====================================================

# --- POKÉMON FEU ---
class PokemonFeu(Pokemon):
    def __init__(self):
        super().__init__(
            "Poussifeu", "Feu", 40,
            [("Flammèche", 10), ("Griffe", 8), ("Charge", 6), ("Danseflamme", 12)],
            niveau=5, evolution="Galifeu", niveau_evolution=16
        )


# --- POKÉMON EAU ---
class PokemonEau(Pokemon):
    def __init__(self):
        super().__init__(
            "Grenouss", "Eau", 40,
            [("Pistolet à O", 10), ("Charge", 6), ("Bulles d’O", 8), ("Écume", 7)],
            niveau=5, evolution="Croâporal", niveau_evolution=16
        )


# --- POKÉMON PLANTE ---
class PokemonPlante(Pokemon):
    def __init__(self):
        super().__init__(
            "Bulbizarre", "Plante", 42,
            [("Fouet Lianes", 10), ("Charge", 6), ("Tranch’Herbe", 12), ("Vampigraine", 0)],
            niveau=5, evolution="Herbizarre", niveau_evolution=16
        )
