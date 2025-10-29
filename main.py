from pokemon import Pokemon, PokemonFeu, PokemonEau, PokemonPlante
from combat import lancer_combat
from arene import Arene, CombattantArene
from items import Potion, SuperPotion, Revive, PokeBall
import random

# ---------------------------------
# INVENTAIRE INITIAL DU JOUEUR
# ---------------------------------
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


# ---------------------------------
# CHOIX DU DRESSEUR
# ---------------------------------
print("MINI JEU POKÉMON ")

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

# ---------------------------------
# CHOIX DU STARTER
# ---------------------------------
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

# ---------------------------------
# DÉBUT DE L'AVENTURE
# ---------------------------------
equipe = [pokemon]
pokemons_sauvages = [
    Pokemon("Rattata", "Normal", 39, [("Charge", 8), ("Morsure", 10), ("Coup de tête", 12), ("Griffe", 10)]),
    Pokemon("Psykokwak", "Eau", 40, [("Pistolet à O", 10), ("Coup de tête", 11), ("Bec Vrille", 13), ("Hydroqueue", 15)]),
    Pokemon("Evoli", "Normal", 40, [("Charge", 8), ("Morsure", 10), ("Coup d’Boule", 12), ("Vive-Attaque", 14)])
]

explorations = 0
arene_disponible = False

# ---------------------------------
# BOUCLE PRINCIPALE DU JEU
# ---------------------------------
while True:
    print("\nQue veux-tu faire ?")
    print("1. Explorer la route")
    print("2. Voir ton équipe")
    print("3. Voir ton inventaire")
    print("4. Utiliser un objet")
    if arene_disponible:
        print("5. Aller à l'Arène Pyronis")
        print("6. Quitter le jeu")
    else:
        print("5. Quitter le jeu")

    action = input("-> ").lower()

    # --- Explorer la route
    if action == "1":
        print("\nTu explores la route...")
        explorations += 1

        # 70 % de chance de rencontrer un Pokémon sauvage
        if random.random() < 0.7:
            modele = random.choice(pokemons_sauvages)
            sauvage = Pokemon(modele.nom, modele.type, modele.pv_max, modele.attaques)

            print(f"Un {sauvage.nom} sauvage apparaît ! (Type {sauvage.type}, {sauvage.pv} PV)")

            while sauvage.est_vivant() and any(p.est_vivant() for p in equipe):
                print("\nQue veux-tu faire ?")
                print("1. Combattre")
                print("2. Capturer (Poké Ball)")
                print("3. Fuir")
                choix_action = input("-> ").lower()

                # --- Combat
                if choix_action == "1":
                    if not equipe[0].est_vivant():
                        print(f"\n{equipe[0].nom} est K.O. ! Il faut le soigner avant de combattre.")
                        continue
                    resultat = lancer_combat(equipe, sauvage, inventaire, choix_libre=True)

                    if resultat == "victoire":
                        
                        break
                    elif resultat == "annule":
                        continue

                # --- Capture
                elif choix_action == "2":
                    pokeball = next((obj for obj in inventaire if obj.nom == "Poké Ball"), None)
                    if not pokeball:
                        print("Tu n’as plus de Poké Ball !")
                        continue

                    reussi = pokeball.utiliser(sauvage, inventaire)
                    # NE PAS supprimer manuellement ici : déjà fait dans .utiliser()

                    if reussi:
                        if len(equipe) < 6:
                            equipe.append(sauvage)
                            print(f"Tu as capturé {sauvage.nom} !")
                        else:
                            print(f"Ton équipe est pleine. {sauvage.nom} a été envoyé au PC.")
                        break
                    else:
                        print(f"{sauvage.nom} s’est échappé !")

                # --- Fuite
                elif choix_action == "3":
                    print("Tu fuis le combat en sécurité.")
                    break

                else:
                    print("Choix invalide.")

        else:
            print("Rien à signaler aujourd’hui.")

        # Après plusieurs explorations → arène débloquée
        if explorations >= 3 and not arene_disponible:
            print("\n🔥 Tu arrives devant une immense tour enflammée : l’Arène Pyronis !")
            arene_disponible = True

    # --- Voir l’équipe
    elif action == "2":
        print(f"\nÉquipe de {dresseur} :")
        for i, p in enumerate(equipe, 1):
            print(f"{i}. {p.nom} ({p.type}) - {p.pv}/{p.pv_max} PV")
        print(f"Total : {len(equipe)}/6 Pokémon")

    # --- Voir inventaire
    elif action == "3":
        afficher_inventaire(inventaire)

    # --- Utiliser un objet (hors combat)
    elif action == "4":
        if not inventaire:
            print("\nTon sac est vide.")
            continue

        compteur = {}
        for item in inventaire:
            compteur[item.nom] = compteur.get(item.nom, 0) + 1
        objets_dispo = list(compteur.keys())

        print("\n🎒 Objets disponibles :")
        for i, nom in enumerate(objets_dispo, 1):
            print(f"{i}. {nom} x{compteur[nom]}")

        choix = input("Quel objet veux-tu utiliser ? -> ").strip()
        if not choix.isdigit():
            print("Entrée invalide.")
            continue
        index = int(choix) - 1
        if index < 0 or index >= len(objets_dispo):
            print("Choix invalide.")
            continue

        nom_objet = objets_dispo[index]
        objet = next((it for it in inventaire if it.nom == nom_objet), None)

        print("\nSur quel Pokémon veux-tu utiliser l'objet ?")
        for i, p in enumerate(equipe, 1):
            print(f"{i}. {p.nom} ({p.pv}/{p.pv_max} PV)")

        choix_poke = input("-> ").strip()
        if not choix_poke.isdigit():
            print("Entrée invalide.")
            continue

        index_poke = int(choix_poke) - 1
        if 0 <= index_poke < len(equipe):
            cible = equipe[index_poke]
            objet.utiliser(cible, inventaire)
        else:
            print("Choix invalide.")

    # --- Entrer dans l'Arène Pyronis
    elif action == "5" and arene_disponible:
        print("\nSouhaites-tu entrer dans l’Arène Pyronis ?")
        print("1. Oui, je veux défier les dresseurs")
        print("2. Non, je préfère continuer à explorer")
        choix_arene = input("-> ").lower()

        if choix_arene == "1":
            print("\nTu entres dans l'Arène Pyronis...")

            dresseurs_feu = [
                CombattantArene("Steven", Pokemon("Caninos", "Feu", 42, [("Charge", 10), ("Crocs Feu", 13), ("Flammèche", 12), ("Bélier", 15)])),
                CombattantArene("Aulne", Pokemon("Goupix", "Feu", 43, [("Flammèche", 12), ("Rugissement", 0), ("Lance-Flamme", 18), ("Queue de Fer", 14)])),
                CombattantArene("Cynthia", Pokemon("Magby", "Feu", 44, [("Poing Feu", 15), ("Crocs Feu", 14), ("Jet de Flamme", 18), ("Charge", 10)])),
                CombattantArene("Cendre", Pokemon("Salamèche", "Feu", 45, [("Griffe", 10), ("Flammèche", 12), ("Crocs Feu", 14), ("Lance-Flamme", 18)])),
                CombattantArene("Rouge le Champion", Pokemon("Simiabraz", "Feu", 47, [("Roue de Feu", 20), ("Poing Feu", 18), ("Lame de Roc", 16), ("Mach Punch", 14)]))
            ]

            arene_feu = Arene("Arène Pyronis", "Feu", "Badge Flamme", dresseurs_feu)
            victoire = arene_feu.demarrer_defi(equipe, inventaire)
            explorations = 0

            if victoire:
                print("\n🔥 Tu sors victorieux de l'Arène Pyronis avec le Badge Flamme !")
            else:
                print("\nTu quittes l’arène pour t’entraîner avant de revenir.")

        else:
            print("\nTu décides de ne pas entrer et continues ton aventure.")

    # --- Quitter le jeu
    elif (action == "5" and not arene_disponible) or (action == "6" and arene_disponible):
        print("\nMerci d’avoir joué, à bientôt 👋")
        break

    else:
        print("Choix invalide, réessaie.")
