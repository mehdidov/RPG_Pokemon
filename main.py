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

# Message final
print(f"\nBienvenue {dresseur} 👋 ! Ton aventure commence maintenant.")
