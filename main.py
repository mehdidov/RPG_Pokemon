# main.py
from dresseur import Dresseur
from arene import Arene
from combat import combat   # <-- ajoute cette ligne
import random


def jeu():
    print("===== L'Épreuve des Trois Arènes =====\n")

    # Choisir le dresseur
    noms = ["Mehdi", "Ayla", "Noah", "Lina"]
    print("Choisis ton dresseur (nom ou numéro) :")
    for i, nom in enumerate(noms, 1):
        print(f"{i}. {nom}")

    choix = input("> ")

    if choix.isdigit():
        joueur = Dresseur(noms[int(choix) - 1])
    elif choix in noms:
        joueur = Dresseur(choix)
    else:
        print("Choix invalide, on te donne Mehdi par défaut.")
        joueur = Dresseur("Mehdi")

    # Choisir le Pokémon
    joueur.choisir_creature()

    # Sélectionner une arène aléatoire
    types_arenes = ["Feu", "Eau", "Plante"]
    type_choisi = random.choice(types_arenes)
    arene = Arene(type_choisi)
    arene.presenter()

    # Combat
    combat(joueur, arene.champion)

    print("\nMerci d’avoir joué 👋")

if __name__ == "__main__":
    jeu()
