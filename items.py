import random

# --- Classe de base pour tous les objets ---
class Item:
    def __init__(self, nom):
        # Chaque objet possède un nom (ex : Potion, Poké Ball, etc.)
        self.nom = nom

    # Méthode à redéfinir dans les sous-classes
    def utiliser(self, pokemon=None, inventaire=None):
        pass


# --- Potion ---
class Potion(Item):
    def __init__(self):
        # Le nom de l'objet est "Potion"
        super().__init__("Potion")

    # Utilisation d'une potion sur un Pokémon
    def utiliser(self, pokemon, inventaire):
        # On vérifie que le Pokémon n’est pas K.O.
        if not pokemon.est_vivant():
            print(f"{pokemon.nom} est K.O., tu ne peux pas utiliser une Potion.")
            return False

        # Si le Pokémon n’est pas à 100% de ses PV, on le soigne
        if pokemon.soigner(20):
            print(f"{pokemon.nom} récupère 20 PV ! ({pokemon.pv}/{pokemon.pv_max})")
            inventaire.remove(self)  # On retire la potion de l’inventaire
            return True
        else:
            print(f"{pokemon.nom} est déjà au maximum de ses PV.")
            return False


# --- Super Potion ---
class SuperPotion(Item):
    def __init__(self):
        # Le nom de l'objet est "Super Potion"
        super().__init__("Super Potion")

    def utiliser(self, pokemon, inventaire):
        if not pokemon.est_vivant():
            print(f"{pokemon.nom} est K.O., tu ne peux pas utiliser une Super Potion.")
            return False

        # Soigne 50 PV au lieu de 20
        if pokemon.soigner(50):
            print(f"{pokemon.nom} récupère 50 PV ! ({pokemon.pv}/{pokemon.pv_max})")
            inventaire.remove(self)
            return True
        else:
            print(f"{pokemon.nom} est déjà au maximum de ses PV.")
            return False


# --- Rappel (Revive) ---
class Revive(Item):
    def __init__(self):
        # Le nom de l'objet est "Rappel"
        super().__init__("Rappel")

    def utiliser(self, pokemon, inventaire):
        # Si le Pokémon est déjà vivant, inutile de l’utiliser
        if pokemon.est_vivant():
            print(f"{pokemon.nom} n’a pas besoin de Rappel.")
            return False

        # Réanime le Pokémon à 50% de ses PV max
        pokemon.pv = pokemon.pv_max // 2
        print(f"{pokemon.nom} est réanimé à {pokemon.pv} PV !")
        inventaire.remove(self)
        return True


# --- Poké Ball ---
class PokeBall(Item):
    def __init__(self):
        # Le nom de l'objet est "Poké Ball"
        super().__init__("Poké Ball")

    def utiliser(self, cible, inventaire):
        # Lancer d’une Poké Ball sur un Pokémon sauvage
        print(f"Tu lances une Poké Ball sur {cible.nom}...")
        chance_capture = random.random()  # Nombre aléatoire entre 0 et 1
        inventaire.remove(self)  # Retire la Poké Ball du sac

        # 50% de chance de capturer le Pokémon
        if chance_capture < 0.5:
            print(f"✨ {cible.nom} est capturé !")
            return True
        else:
            print(f"{cible.nom} s’est échappé de la Poké Ball !")
            return False


# --- Fonction d'affichage de l'inventaire ---
def afficher_inventaire(inventaire):
    # Si le sac est vide, on le dit clairement
    if not inventaire:
        print("\nTon sac est vide.")
        return

    print("\n🎒 Inventaire :")
    compteur = {}

    # On compte combien d’objets de chaque type le joueur possède
    for item in inventaire:
        compteur[item.nom] = compteur.get(item.nom, 0) + 1

    # On affiche le contenu de l’inventaire
    for nom, qte in compteur.items():
        print(f"- {nom} x{qte}")
