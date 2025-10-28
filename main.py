from pokemon import Pokemon, PokemonFeu, PokemonEau, PokemonPlante
from combat import lancer_combat
import random

print("MINI JEU POKÉMON ")

# Choix du dresseur 
dresseurs = ["Sacha", "Pierre", "Mehdi", "Iris"]

while True:
    print("\nChoisis ton dresseur :")
    for i, nom in enumerate(dresseurs, 1):
        print(f"{i}. {nom}")

    choix = input("-> ").strip()

    
    if choix.isdigit():
        index = int(choix) - 1
        if 0 <= index < len(dresseurs):
            dresseur = dresseurs[index]
            break
        else:
            print("Numéro invalide, réessaie.")
    
    elif choix.lower() in [n.lower() for n in dresseurs]:
        for nom in dresseurs:
            if nom.lower() == choix.lower():
                dresseur = nom
                break
        break
    else:
        print("Nom invalide, réessaie.")

print(f"\nBienvenue {dresseur} 👋 ! Ton aventure commence maintenant.")

# Choix du starter
print("\nC’est le moment de choisir ton premier Pokémon !")
print("1. Poussifeu (Feu)")
print("2. Grenouss (Eau)")
print("3. Bulbizarre (Plante)")

while True:
    choix_pokemon = input("-> ").lower()
    if choix_pokemon in ["1", "poussifeu"]:
        pokemon = PokemonFeu()
        break
    elif choix_pokemon in ["2", "grenouss"]:
        pokemon = PokemonEau()
        break
    elif choix_pokemon in ["3", "bulbizarre"]:
        pokemon = PokemonPlante()
        break
    else:
        print("Choix invalide. Essaie encore !")

print(f"\nTu as choisi {pokemon.nom} ({pokemon.type}) !")

# Début de l'aventure
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
    action = input("-> ").lower()

    if action == "1":
        print("\nTu explores la route... ")

    
        if random.random() < 0.7:
            modele = random.choice(pokemons_sauvages)
            sauvage = Pokemon(modele.nom, modele.type, modele.pv_max, modele.attaque)
            print(f"Un {sauvage.nom} sauvage apparaît ! (Type {sauvage.type}, {sauvage.pv} PV)")

            
            while True:
                print("\nQue veux-tu faire ?")
                print("1. Combattre")
                print("2. Capturer")
                print("3. Fuir" )
                choix_action = input("-> ").lower()

                # Combat
                if choix_action in ["1", "combattre"]:
                    if not equipe[0].est_vivant():
                        print(f"\n{equipe[0].nom} est K.O. ! Il faut le soigner avant de combattre.")
                        break
                    lancer_combat(equipe[0], sauvage)
                    break  

                # Capture 
                elif choix_action in ["2", "capturer"]:
                    chance_capture = random.random()
                    if chance_capture < 0.60:
                        if len(equipe) < 6:
                            equipe.append(sauvage)
                            print(f"Tu as capturé {sauvage.nom} !")
                        else:
                            print("Ton équipe est déjà pleine (6 Pokémon max) !")
                            print("Voici ton équipe actuelle :")
                            for i, p in enumerate(equipe, 1):
                                print(f"{i}. {p.nom} ({p.type}) - {p.pv}/{p.pv_max} PV")

                            remp = input("Souhaites-tu remplacer un Pokémon ? (o/n) -> ").lower()
                            if remp == "o":
                                index = input("Quel Pokémon veux-tu remplacer (1-6) ? -> ")
                                if index.isdigit():
                                    index = int(index) - 1
                                    if 0 <= index < len(equipe):
                                        ancien = equipe[index]
                                        equipe[index] = sauvage
                                        print(f"Tu as remplacé {ancien.nom} par {sauvage.nom} !")
                                    else:
                                        print("Numéro invalide.")
                                else:
                                    print("Entrée invalide, capture annulée.")
                            else:
                                print(f"Tu laisses {sauvage.nom} repartir.")
                    else:
                        print(f"{sauvage.nom} s’est échappé de la Pokéball !")
                    break  

                # Fuite 
                elif choix_action in ["3", "fuir"]:
                    print("Tu fuis en sécurité.")
                    break

                else:
                    print("Choix invalide, réessaie.")

        else:
            print("Rien à signaler... ")

    elif action == "2":
        print(f"\nÉquipe de {dresseur} :")
        for i, p in enumerate(equipe, 1):
            print(f"{i}. {p.nom} ({p.type}) - {p.pv}/{p.pv_max} PV")
        print(f"Total : {len(equipe)}/6 Pokémon")

    elif action == "3":
        print("\nMerci d’avoir joué, à bientôt ")
        break

    else:
        print("Choix invalide, réessaie.")
