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
    "1": {"nom": "Flammion", "type": "Feu"},
    "2": {"nom": "Aquabulle", "type": "Eau"},
    "3": {"nom": "Feuillette", "type": "Plante"}
}

print("\nC’est le moment de choisir ton premier Pokémon !")

while True:
    print("1. Flammion (Feu)")
    print("2. Aquabulle (Eau)")
    print("3. Feuillette (Plante)")
    choix_pokemon = input("-> ").strip().lower()  # 👈 on convertit en minuscules

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


