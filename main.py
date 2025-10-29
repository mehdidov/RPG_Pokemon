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
# AIDES
# ---------------------------------
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
        CombattantArene("Erable la Championne", Pokemon("Empiflor", "Plante", 53, [("Tranch’Feuille", 18), ("Canon Graine", 18), ("Vampigraine", 0), ("Mégafouet", 20)])),
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


def pool_sauvage_etape(etape):
    """
    etape:
      0 -> avant l'Arène Feu (donner un avantage contre Feu) => +Eau
      1 -> avant l'Arène Plante (donner un avantage contre Plante) => +Feu
     2+ -> avant l'Arène Eau (donner un avantage contre Eau) => +Plante
    """
    if etape == 0:
        return [
            Pokemon("Psykokwak", "Eau", 40, [("Pistolet à O", 10), ("Coup de tête", 11), ("Bec Vrille", 13), ("Hydroqueue", 15)]),
            Pokemon("Carapuce", "Eau", 41, [("Écume", 10), ("Pistolet à O", 12), ("Coup de Queue", 14), ("Hydroqueue", 16)]),
            Pokemon("Evoli", "Normal", 40, [("Charge", 8), ("Morsure", 10), ("Coup d’Boule", 12), ("Vive-Attaque", 14)]),
        ]
    elif etape == 1:
        return [
            Pokemon("Caninos", "Feu", 44, [("Charge", 10), ("Crocs Feu", 14), ("Flammèche", 12), ("Bélier", 15)]),
            Pokemon("Goupix", "Feu", 44, [("Flammèche", 12), ("Rugissement", 0), ("Lance-Flamme", 18), ("Queue de Fer", 14)]),
            Pokemon("Roucool", "Normal", 43, [("Tornade", 12), ("Cru-Aile", 14), ("Vive-Attaque", 14), ("Jet de Sable", 0)]),  # Vol (type non géré mais ok en "Normal" ici)
        ]
    else:
        return [
            Pokemon("Chétiflor", "Plante", 48, [("Fouet Lianes", 12), ("Tranch’Herbe", 14), ("Tranch’Feuille", 16), ("Canon Graine", 16)]),
            Pokemon("Mystherbe", "Plante", 49, [("Poudre Dodo", 0), ("Méga-Sangsue", 16), ("Tranch’Herbe", 16), ("Acide", 12)]),
            Pokemon("Bulbizarre", "Plante", 50, [("Fouet Lianes", 12), ("Tranch’Herbe", 14), ("Canon Graine", 16), ("Vampigraine", 0)]),
        ]


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
# ÉTAT D’AVANCEMENT
# ---------------------------------
equipe = [pokemon]

# etape 0 = avant arène Feu ; 1 = avant arène Plante ; 2 = avant arène Eau ; 3 = toutes faites
etape = 0
explorations = 0

# arènes disponibles selon l’étape
def arene_disponible_nom(etape):
    if etape == 0:
        return None  # pas encore Pyronis
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
    if nom_arene is None:
        print("5. Quitter le jeu")
    else:
        print(f"5. Aller à {nom_arene}")
        print("6. Quitter le jeu")


# ---------------------------------
# BOUCLE PRINCIPALE DU JEU
# ---------------------------------
while True:
    afficher_menu(etape)
    action = input("-> ").lower()

    # --- Explorer la route
    if action == "1":
        print("\nTu explores la route...")
        explorations += 1

        # Probabilité de rencontre
        if random.random() < 0.7:
            modele = random.choice(pool_sauvage_etape(etape if etape < 3 else 2))
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
                        # tu as vaincu le sauvage (gain d’XP non géré ici)
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
                    if reussi:
                        if len(equipe) < 6:
                            equipe.append(sauvage)
                            print(f"✨ Tu as capturé {sauvage.nom} !")
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

        # Déblocage des arènes par étape :
        # - etape 0 (début) -> après 3 explorations, Pyronis devient dispo => on passe à etape 1
        # - etape 1 -> Verdania devient dispo quand on a battu Pyronis (géré ailleurs)
        # - etape 2 -> Hydrolys devient dispo quand on a battu Verdania (géré ailleurs)
        if etape == 0 and explorations >= 3:
            print("\n🔥 Tu arrives devant une immense tour enflammée : l’Arène Pyronis !")
            etape = 1  # Pyronis accessible

    # --- Voir l’équipe
    elif action == "2":
        print(f"\nÉquipe de {dresseur} :")
        for i, p in enumerate(equipe, 1):
            etat = "K.O." if not p.est_vivant() else f"{p.pv}/{p.pv_max} PV"
            print(f"{i}. {p.nom} ({p.type}) - {etat}")
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
            # On passe la cible même si l'objet ne la nécessite pas
            res = objet.utiliser(cible, inventaire)
            # certains objets renvoient None (ex: Potion), c'est ok
        else:
            print("Choix invalide.")

    # --- Aller à l’Arène (selon l’étape)
    elif (action == "5" and arene_disponible_nom(etape) is not None):
        nom_arene = arene_disponible_nom(etape)

        if nom_arene == "Arène Pyronis":
            print("\nSouhaites-tu entrer dans l’Arène Pyronis ?")
            print("1. Oui, je veux défier les dresseurs")
            print("2. Non, je préfère continuer à explorer")
            choix_arene = input("-> ").lower()

            if choix_arene == "1":
                print("\nTu entres dans l'Arène Pyronis...")
                arene_feu = creer_arene_feu()
                victoire = arene_feu.demarrer_defi(equipe, inventaire)
                explorations = 0

                if victoire:
                    print("\n🔥 Tu sors victorieux de l'Arène Pyronis avec le Badge Flamme !")
                    # Débloquer la prochaine zone (Verdania) -> on revient au menu, mais etape passe à 2
                    print("\nLa route s’ouvre vers une forêt luxuriante... L’Arène Verdania (Plante) t’attend !")
                    etape = 2
                else:
                    print("\nTu quittes l’arène pour t’entraîner avant de revenir.")

            else:
                print("\nTu décides de ne pas entrer et continues ton aventure.")

        elif nom_arene == "Arène Verdania":
            print("\nSouhaites-tu entrer dans l’Arène Verdania ?")
            print("1. Oui, je veux défier les dresseurs")
            print("2. Non, je préfère continuer à explorer")
            choix_arene = input("-> ").lower()

            if choix_arene == "1":
                print("\nTu entres dans l'Arène Verdania...")
                arene_plante = creer_arene_plante()
                victoire = arene_plante.demarrer_defi(equipe, inventaire)
                explorations = 0

                if victoire:
                    print("\n🌿 Tu sors victorieux de l'Arène Verdania avec le Badge Verdure !")
                    # Débloquer Hydrolys
                    print("\nUn sentier longeant une rivière te mène à l’Arène Hydrolys (Eau) !")
                    etape = 3
                else:
                    print("\nTu quittes l’arène pour t’entraîner avant de revenir.")

            else:
                print("\nTu décides de ne pas entrer et continues ton aventure.")

        elif nom_arene == "Arène Hydrolys":
            print("\nSouhaites-tu entrer dans l’Arène Hydrolys ?")
            print("1. Oui, je veux défier les dresseurs")
            print("2. Non, je préfère continuer à explorer")
            choix_arene = input("-> ").lower()

            if choix_arene == "1":
                print("\nTu entres dans l'Arène Hydrolys...")
                arene_eau = creer_arene_eau()
                victoire = arene_eau.demarrer_defi(equipe, inventaire)
                explorations = 0

                if victoire:
                    print("\n💧 Tu sors victorieux de l'Arène Hydrolys avec le Badge Cascade !")
                    print("\n🏆 Félicitations ! Tu as remporté les trois premiers badges de la Ligue !")
                    print("Tu peux continuer à explorer, entraîner ton équipe, et compléter ton Pokédex !")
                    # etape > 3 => plus d'arènes, on garde l'exploration
                    etape = 4
                else:
                    print("\nTu quittes l’arène pour t’entraîner avant de revenir.")

            else:
                print("\nTu décides de ne pas entrer et continues ton aventure.")

        else:
            print("\nAucune arène accessible pour le moment.")

    # --- Quitter le jeu
    elif (action == "5" and arene_disponible_nom(etape) is None) or (action == "6" and arene_disponible_nom(etape) is not None):
        print("\nMerci d’avoir joué, à bientôt 👋")
        break

    else:
        print("Choix invalide, réessaie.")
