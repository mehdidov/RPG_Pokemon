# =====================================================
# Fichier : main.py
# Point d’entrée du jeu Pokémon (exploration, arènes, inventaire, etc.)
# =====================================================

from pokemon import Pokemon, PokemonFeu, PokemonEau, PokemonPlante
from combat import lancer_combat
from arene import Arene, CombattantArene
from items import Potion, SuperPotion, Revive, PokeBall
import random

# =====================================================
# INVENTAIRE INITIAL DU JOUEUR
# =====================================================
inventaire = []

# Ajout de potions et objets de départ
for i in range(7):
    inventaire.append(Potion())
for i in range(3):
    inventaire.append(SuperPotion())
inventaire.append(Revive())
for i in range(15):
    inventaire.append(PokeBall())


# =====================================================
# FONCTION D’AFFICHAGE DE L’INVENTAIRE
# =====================================================
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


# =====================================================
# CRÉATION DES ARÈNES
# =====================================================
def creer_arene_feu():
    dresseurs_feu = [
        CombattantArene("Steven", Pokemon("Caninos", "Feu", 42, [("Charge", 10), ("Crocs Feu", 13), ("Flammèche", 12), ("Bélier", 15)])),
        CombattantArene("Aulne", Pokemon("Goupix", "Feu", 43, [("Flammèche", 12), ("Rugissement", 0), ("Lance-Flamme", 18), ("Queue de Fer", 14)])),
        CombattantArene("Cynthia", Pokemon("Magby", "Feu", 44, [("Poing Feu", 15), ("Crocs Feu", 14), ("Jet de Flamme", 18), ("Charge", 10)])),
        CombattantArene("Cendre", Pokemon("Salamèche", "Feu", 45, [("Griffe", 10), ("Flammèche", 12), ("Crocs Feu", 14), ("Lance-Flamme", 18)])),
        CombattantArene("Rouge le Champion", Pokemon("Simiabraz", "Feu", 47, [("Roue de Feu", 20), ("Poing Feu", 18), ("Lame de Roc", 16), ("Mach Punch", 14)]))
    ]
    return Arene("Arène Pyronis", "Feu", "Badge Flamme", dresseurs_feu)


def creer_arene_plante():
    dresseurs_plante = [
        CombattantArene("Violaine", Pokemon("Germignon", "Plante", 48, [("Charge", 10), ("Fouet Lianes", 12), ("Tranch’Herbe", 15), ("Vampigraine", 0)])),
        CombattantArene("Théo", Pokemon("Chétiflor", "Plante", 49, [("Fouet Lianes", 12), ("Tranch’Herbe", 14), ("Tranch’Feuille", 16), ("Canon Graine", 15)])),
        CombattantArene("Flora", Pokemon("Ortide", "Plante", 50, [("Poudre Dodo", 0), ("Acide", 12), ("Tranch’Herbe", 16), ("Giga-Sangsue", 18)])),
        CombattantArene("Léa", Pokemon("Rosélia", "Plante", 51, [("Méga-Sangsue", 16), ("Tranch’Herbe", 16), ("Canon Graine", 17), ("Dard-Venin", 12)])),
        CombattantArene("Érable la Championne", Pokemon("Empiflor", "Plante", 53, [("Tranch’Feuille", 18), ("Canon Graine", 18), ("Vampigraine", 0), ("Mégafouet", 20)])),
    ]
    return Arene("Arène Verdania", "Plante", "Badge Verdure", dresseurs_plante)


def creer_arene_eau():
    dresseurs_eau = [
        CombattantArene("Nilo", Pokemon("Têtarte", "Eau", 54, [("Écume", 12), ("Pistolet à O", 14), ("Bulles d’O", 16), ("Hypnose", 0)])),
        CombattantArene("Ondine Jr", Pokemon("Stari", "Eau", 55, [("Pistolet à O", 14), ("Bulles d’O", 16), ("Tour Rapide", 12), ("Rayon Gemme", 18)])),
        CombattantArene("Mira", Pokemon("Krabby", "Eau", 56, [("Bulles d’O", 16), ("Pince-Masse", 18), ("Coup d’Boule", 14), ("Écume", 12)])),
        CombattantArene("Soren", Pokemon("Psykokwak", "Eau", 57, [("Pistolet à O", 16), ("Hydroqueue", 20), ("Coup de Tête", 14), ("Amnésie", 0)])),
        CombattantArene("Hydra la Championne", Pokemon("Lokhlass", "Eau", 60, [("Surf", 22), ("Hydroqueue", 20), ("Grincement", 0), ("Laser Glace", 22)])),
    ]
    return Arene("Arène Hydrolys", "Eau", "Badge Cascade", dresseurs_eau)


# =====================================================
# RENCONTRES SAUVAGES SELON L’ÉTAPE
# =====================================================
def pool_sauvage_etape(etape):
    if etape == 0:  # avant l’arène Feu → Pokémon Eau
        return [
            Pokemon("Psykokwak", "Eau", 40, [("Pistolet à O", 10), ("Coup de Tête", 11), ("Bec Vrille", 13), ("Hydroqueue", 15)]),
            Pokemon("Carapuce", "Eau", 41, [("Écume", 10), ("Pistolet à O", 12), ("Coup de Queue", 14), ("Hydroqueue", 16)]),
            Pokemon("Evoli", "Normal", 40, [("Charge", 8), ("Morsure", 10), ("Coup d’Boule", 12), ("Vive-Attaque", 14)]),
        ]
    elif etape == 1:  # avant l’arène Plante → Pokémon Feu
        return [
            Pokemon("Caninos", "Feu", 44, [("Charge", 10), ("Crocs Feu", 14), ("Flammèche", 12), ("Bélier", 15)]),
            Pokemon("Goupix", "Feu", 44, [("Flammèche", 12), ("Rugissement", 0), ("Lance-Flamme", 18), ("Queue de Fer", 14)]),
            Pokemon("Roucool", "Normal", 43, [("Tornade", 12), ("Cru-Aile", 14), ("Vive-Attaque", 14), ("Jet de Sable", 0)]),
        ]
    else:  # avant l’arène Eau → Pokémon Plante
        return [
            Pokemon("Chétiflor", "Plante", 48, [("Fouet Lianes", 12), ("Tranch’Herbe", 14), ("Tranch’Feuille", 16), ("Canon Graine", 16)]),
            Pokemon("Mystherbe", "Plante", 49, [("Poudre Dodo", 0), ("Méga-Sangsue", 16), ("Tranch’Herbe", 16), ("Acide", 12)]),
            Pokemon("Bulbizarre", "Plante", 50, [("Fouet Lianes", 12), ("Tranch’Herbe", 14), ("Canon Graine", 16), ("Vampigraine", 0)]),
        ]


# =====================================================
# CHOIX DU DRESSEUR ET DU STARTER
# =====================================================
print("MINI JEU POKÉMON 🎮")

dresseurs = ["Sacha", "Pierre", "Mehdi", "Iris"]
while True:
    print("\nChoisis ton dresseur :")
    for i, nom in enumerate(dresseurs, 1):
        print(f"{i}. {nom}")
    choix = input("-> ").strip()
    if choix.isdigit() and 1 <= int(choix) <= len(dresseurs):
        dresseur = dresseurs[int(choix) - 1]
        break
    elif choix.lower() in [n.lower() for n in dresseurs]:
        dresseur = choix.capitalize()
        break
    else:
        print("Choix invalide, réessaie.")

print(f"\nBienvenue {dresseur} ! Ton aventure commence maintenant.")
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

# =====================================================
# VARIABLES DE PROGRESSION
# =====================================================
equipe = [pokemon]
etape = 0
explorations = 0


def arene_disponible_nom(etape):
    if etape == 0:
        return None
    elif etape == 1:
        return "Arène Pyronis"
    elif etape == 2:
        return "Arène Verdania"
    elif etape == 3:
        return "Arène Hydrolys"
    else:
        return None


def afficher_menu(etape):
    print("\nQue veux-tu faire ?")
    print("1. Explorer la route")
    print("2. Voir ton équipe")
    print("3. Voir ton inventaire")
    print("4. Utiliser un objet")
    nom_arene = arene_disponible_nom(etape)
    if nom_arene:
        print(f"5. Aller à {nom_arene}")
        print("6. Quitter le jeu")
    else:
        print("5. Quitter le jeu")


# =====================================================
# BOUCLE PRINCIPALE DU JEU
# =====================================================
while True:
    afficher_menu(etape)
    action = input("-> ").lower()

    # --- Exploration ---
    if action == "1":
        print("\nTu explores la route...")
        explorations += 1
        if random.random() < 0.7:
            sauvage = random.choice(pool_sauvage_etape(min(etape, 2)))
            print(f"Un {sauvage.nom} sauvage apparaît ! (Type {sauvage.type}, {sauvage.pv} PV)")

            while sauvage.est_vivant() and any(p.est_vivant() for p in equipe):
                print("\nQue veux-tu faire ?")
                print("1. Combattre")
                print("2. Capturer (Poké Ball)")
                print("3. Fuir")
                choix_action = input("-> ").lower()

                if choix_action == "1":
                    lancer_combat(equipe, sauvage, inventaire)
                    break
                elif choix_action == "2":
                    pokeball = next((obj for obj in inventaire if obj.nom == "Poké Ball"), None)
                    if not pokeball:
                        print("Tu n’as plus de Poké Ball !")
                        continue
                    if pokeball.utiliser(sauvage, inventaire):
                        equipe.append(sauvage)
                        print(f"✨ Tu as capturé {sauvage.nom} !")
                        break
                    else:
                        print(f"{sauvage.nom} s’est échappé !")
                elif choix_action == "3":
                    print("Tu fuis le combat.")
                    break
                else:
                    print("Choix invalide.")
        else:
            print("Rien à signaler aujourd’hui.")

        if etape == 0 and explorations >= 3:
            print("\n🔥 Tu découvres l’Arène Pyronis ! Elle est maintenant accessible.")
            etape = 1

    # --- Voir équipe ---
    elif action == "2":
        print(f"\nÉquipe de {dresseur} :")
        for i, p in enumerate(equipe, 1):
            etat = "K.O." if not p.est_vivant() else f"{p.pv}/{p.pv_max} PV"
            print(f"{i}. {p.nom} ({p.type}) - Niv. {p.niveau} - {etat}")

    # --- Inventaire ---
    elif action == "3":
        afficher_inventaire(inventaire)

    # --- Utiliser un objet (hors combat) ---
        # --- Utiliser un objet (hors combat)
    elif action == "4":
        if not inventaire:
            print("\nTon sac est vide.")
            continue

        # --- Regroupement des objets similaires
        compteur = {}
        for item in inventaire:
            compteur[item.nom] = compteur.get(item.nom, 0) + 1
        objets_dispo = list(compteur.keys())

        print("\n🎒 Inventaire :")
        for i, nom in enumerate(objets_dispo, 1):
            print(f"{i}. {nom} x{compteur[nom]}")
        print("0. Annuler")

        # --- Choix de l'objet à utiliser
        choix = input("\nChoisis un objet à utiliser (ou 0 pour annuler)\n-> ").strip()
        if choix == "0":
            continue
        if not choix.isdigit() or int(choix) < 1 or int(choix) > len(objets_dispo):
            print("Choix invalide.")
            continue

        nom_objet = objets_dispo[int(choix) - 1]
        objet = next((it for it in inventaire if it.nom == nom_objet), None)

        # --- Choix du Pokémon cible
        print("\nSur quel Pokémon veux-tu utiliser l'objet ?")
        for i, p in enumerate(equipe, 1):
            print(f"{i}. {p.nom} ({p.type}) - {p.pv}/{p.pv_max} PV")
        print("0. Annuler")

        choix_poke = input("-> ").strip()
        if choix_poke == "0":
            continue
        if not choix_poke.isdigit():
            print("Entrée invalide.")
            continue

        index_poke = int(choix_poke) - 1
        if 0 <= index_poke < len(equipe):
            cible = equipe[index_poke]
            resultat = objet.utiliser(cible, inventaire)
            if resultat:
                print(f"{cible.nom} profite de {objet.nom} !")
            else:
                print("L’objet n’a pas été utilisé.")
        else:
            print("Choix invalide.")


    # --- Aller à une Arène ---
    elif action == "5" and arene_disponible_nom(etape):
        nom_arene = arene_disponible_nom(etape)

        # Arène Feu
        if nom_arene == "Arène Pyronis":
            print("\n🔥 Tu entres dans l’Arène Pyronis...")
            victoire = creer_arene_feu().demarrer_defi(equipe, inventaire)
            if victoire:
                print("\nTu gagnes le Badge Flamme ! 🌋")
                etape = 2

        # Arène Plante
        elif nom_arene == "Arène Verdania":
            print("\n🌿 Tu entres dans l’Arène Verdania...")
            victoire = creer_arene_plante().demarrer_defi(equipe, inventaire)
            if victoire:
                print("\nTu gagnes le Badge Verdure ! 🍃")
                etape = 3

        # Arène Eau
        elif nom_arene == "Arène Hydrolys":
            print("\n💧 Tu entres dans l’Arène Hydrolys...")
            victoire = creer_arene_eau().demarrer_defi(equipe, inventaire)
            if victoire:
                print("\nTu gagnes le Badge Cascade ! 🏆")
                etape = 4
                print("\nFélicitations, tu as terminé les trois premières arènes !")

    # --- Quitter le jeu ---
    elif (action == "5" and not arene_disponible_nom(etape)) or (action == "6" and arene_disponible_nom(etape)):
        print("\nMerci d’avoir joué, à bientôt 👋")
        break

    else:
        print("Choix invalide, réessaie.")
