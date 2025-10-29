from pokemon import Pokemon, PokemonFeu, PokemonEau, PokemonPlante
from combat import lancer_combat
from arene import Arene, CombattantArene
from items import Potion, SuperPotion, Revive, PokeBall

import random

# Inventaire du joueur
inventaire = []

# Ajoute 7 Potions
for i in range(7):
    inventaire.append(Potion())

# Ajoute 3 Super Potions
for i in range(3):
    inventaire.append(SuperPotion())

# Ajoute 1 Rappel
inventaire.append(Revive())

# Ajoute 15 Poké Balls par défaut
for i in range(15):
    inventaire.append(PokeBall())

def afficher_inventaire(inventaire):
    if not inventaire:
        print("\nTon sac est vide.")
        return

    print("\n🎒 Inventaire :")
    compteur = {}
    for item in inventaire:
        compteur[item.nom] = compteur.get(item.nom, 0) + 1

    for nom, quantite in compteur.items():
        print(f"- {nom} x{quantite}")


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

print(f"\nBienvenue {dresseur} ! Ton aventure commence maintenant.")

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
    Pokemon("Rattata", "Normal", 39, 12),
    Pokemon("Psykokwak", "Eau", 40, 12),
    Pokemon("Evoli", "Normal", 40, 11)
]

explorations = 0
arene_disponible = False

while True:
    print("\nQue veux-tu faire ?")
    print("1. Explorer la route")
    print("2. Voir ton équipe")
    print("3. Voir ton inventaire")
    if arene_disponible:
        print("4. Aller à l'Arène Pyronis")
        print("5. Quitter le jeu")
    else:
        print("4. Quitter le jeu")
    action = input("-> ").lower()

    if action == "1":
        print("\nTu explores la route...")
        explorations += 1

        if random.random() < 0.7:
            modele = random.choice(pokemons_sauvages)
            sauvage = Pokemon(modele.nom, modele.type, modele.pv_max, modele.attaque)
            print(f"Un {sauvage.nom} sauvage apparaît ! (Type {sauvage.type}, {sauvage.pv} PV)")

            combat_termine = False

            while sauvage.est_vivant() and any(p.est_vivant() for p in equipe):
                if combat_termine:
                    break

                print("\nQue veux-tu faire ?")
                print("1. Combattre")
                print("2. Capturer")
                print("3. Fuir")
                choix_action = input("-> ").lower()

                # --- Combattre ---
                if choix_action in ["1", "combattre"]:
                    if not equipe[0].est_vivant():
                        print(f"\n{equipe[0].nom} est K.O. ! Il faut le soigner avant de combattre.")
                        continue
                    resultat = lancer_combat(equipe, sauvage, choix_libre=True)

                    if resultat == "annule":
                        continue
                    elif resultat == "victoire":
                        print(f"Tu as vaincu {sauvage.nom} !")
                        combat_termine = True
                        break

                # --- Capturer (corrigé ici) ---
                elif choix_action in ["2", "capturer"]:
                    # Vérifie si le joueur a une Poké Ball
                    pokeball = None
                    for item in inventaire:
                        if isinstance(item, PokeBall):
                            pokeball = item
                            break

                    if not pokeball:
                        print("\nTu n’as plus de Poké Ball dans ton inventaire !")
                        continue

                    # Utilisation réelle de la Poké Ball
                    reussi = pokeball.utiliser(sauvage, inventaire)

                    if reussi:
                        if len(equipe) < 6:
                            equipe.append(sauvage)
                            print(f"Tu as capturé {sauvage.nom} !")
                            combat_termine = True
                            break
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
                                        combat_termine = True
                                        break
                                    else:
                                        print("Numéro invalide.")
                                else:
                                    print("Entrée invalide, capture annulée.")
                            else:
                                print(f"Tu laisses {sauvage.nom} repartir.")
                                combat_termine = True
                                break
                    else:
                        print(f"{sauvage.nom} s’est échappé de la Poké Ball !")

                # --- Fuir ---
                elif choix_action in ["3", "fuir"]:
                    print("Tu fuis en sécurité.")
                    combat_termine = True
                    break

                else:
                    print("Choix invalide, réessaie.")

            if combat_termine:
                print("Tu reprends ta route tranquillement...")
                continue
        else:
            print("Rien à signaler...")

        if explorations >= 3 and not arene_disponible:
            print("\nTu arrives devant une immense tour enflammée...")
            print("C’est l’Arène Pyronis, connue pour ses combats intenses !")
            arene_disponible = True

    elif action == "2":
        print(f"\nÉquipe de {dresseur} :")
        for i, p in enumerate(equipe, 1):
            print(f"{i}. {p.nom} ({p.type}) - {p.pv}/{p.pv_max} PV")
        print(f"Total : {len(equipe)}/6 Pokémon")

    elif action == "3":
        afficher_inventaire(inventaire)

    elif action == "4" and arene_disponible:
        print("\nSouhaites-tu entrer dans l’Arène Pyronis ?")
        print("1. Oui, je veux défier les dresseurs")
        print("2. Non, je préfère continuer à explorer")
        choix_arene = input("-> ").lower()

        if choix_arene == "1":
            print("\nTu entres dans l'Arène Pyronis.")

            dresseurs_feu = [
                CombattantArene("Steven", Pokemon("Caninos", "Feu", 42, 15)),
                CombattantArene("Aulne", Pokemon("Goupix", "Feu", 43, 13)),
                CombattantArene("Cynthia", Pokemon("Magby", "Feu", 44, 15)),
                CombattantArene("Cendre", Pokemon("Salamèche", "Feu", 45, 15)),
                CombattantArene("Rouge le Champion", Pokemon("Simiabraz", "Feu", 47, 17))
            ]

            arene_feu = Arene("Arène Pyronis", "Feu", "Flamme", dresseurs_feu)

            print(f"\nBienvenue dans l'{arene_feu.nom} (type {arene_feu.type}) !")
            print("Tu devras gravir les 5 étages et battre chaque dresseur pour atteindre le champion.")
            print("Les fuites sont interdites ici !")
            victoire = arene_feu.demarrer_defi(equipe, inventaire)
            explorations = 0

            if victoire:
                print("\nTu sors victorieux de l'Arène Pyronis avec le badge Flamme !")
            else:
                print("\nTu quittes l'arène pour t'entraîner avant de revenir.")

        else:
            print("\nTu décides de ne pas entrer et continues ton aventure.")

    elif (action == "4" and not arene_disponible) or (action == "5" and arene_disponible):
        print("\nMerci d’avoir joué, à bientôt")
        break

    else:
        print("Choix invalide, réessaie.")
