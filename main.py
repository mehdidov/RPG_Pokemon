# main.py
from pokemon import Pokemon #PokemonFeu, PokemonEau, PokemonPlante
import random

print(" MINI JEU POKÉMON ")

# Liste des dresseurs 
dresseurs = ["Sacha", "Pierre", "Mehdi", "Iris"]

# Boucle tant qu’aucun choix valide n’a été fait
while True:
    print("\nChoisis ton dresseur :")
    for i, nom in enumerate(dresseurs, 1):
        print(f"{i}. {nom}")

    choix = input("-> ")

    # Si on tape un chiffre
    if choix.isdigit():
        index = int(choix) - 1
        if 0 <= index < len(dresseurs):
            dresseur = dresseurs[index]
            break  
        else:
            print("Veuillez choisir un numéro valide entre 1 et 4.")
    
    
    elif choix.lower() in [n.lower() for n in dresseurs]:
        for nom in dresseurs:
            if nom.lower() == choix.lower():
                dresseur = nom
                break
        break  

    else:
        print("Nom invalide. Essaie encore !")


print(f"\nBienvenue {dresseur} 👋 ! Ton aventure commence maintenant.")



starters = {
    "1": {"nom": "Poussifeu", "type": "Feu"},
    "2": {"nom": "Grenouss", "type": "Eau"},
    "3": {"nom": "Bulbizarre", "type": "Plante"}
}

print("\nC’est le moment de choisir ton premier Pokémon !")

while True:
    print("1. Poussifeu (Feu)")
    print("2. Grenouss (Eau)")
    print("3. Bulbizarre (Plante)")
    choix_pokemon = input("-> ").lower()  # 👈 on convertit en minuscules

    # Cas 1 : le joueur tape un chiffre
    if choix_pokemon in starters:
        pokemon = starters[choix_pokemon]
        break

    # Cas 2 : le joueur tape un nom
    noms_pokemons = [p["nom"].lower() for p in starters.values()]
    if choix_pokemon in noms_pokemons:
        for p in starters.values():
            if p["nom"].lower() == choix_pokemon:
                pokemon = p
                break
        break

    print("Choix invalide. Essaie encore !")

print(f"\nTu as choisi {pokemon['nom']} ({pokemon['type']})")


equipe = [pokemon]
pokemons_sauvages = [
    Pokemon("Arcanin", "Feu", 25, 9),
    Pokemon("Psykokwak", "Eau", 32, 5),
    Pokemon("Mystherbe", "Plante", 30, 7)
    
]

while True:
    print("\nQue veux-tu faire ?")
    print("1. Explorer la route")
    print("2. Voir ton équipe")
    print("3. Quitter le jeu")
    action = input("-> ")


if action == "1":
    print("\nTu explores la route...")
    if random.random() < 0.7:
        sauvage = random.choice(pokemons_sauvages)
        print(f"Un {sauvage.nom} sauvage apparaît ! ...")
        reponse = input("... capturer ? (o/n) -> ").lower()
        if reponse == "o":
            if len(equipe) < 6:
                equipe.append(sauvage)
                print(f"Tu as capturé {sauvage.nom} !")
            else:
                print("Ton équipe est déjà pleine (6 Pokémon max) !")
        else:
            print("Tu laisses le Pokémon tranquille.")
    else:
        print("Rien à signaler...")

