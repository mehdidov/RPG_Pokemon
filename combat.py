import random

# --- Tableau d’efficacité des types ---
def calculer_multiplicateur(type_attaquant, type_defenseur):
    avantages = {
        "Feu": {"Plante": 2.0, "Eau": 0.5, "Feu": 0.5},
        "Eau": {"Feu": 2.0, "Plante": 0.5, "Eau": 0.5},
        "Plante": {"Eau": 2.0, "Feu": 0.5, "Plante": 0.5},
    }
    return avantages.get(type_attaquant, {}).get(type_defenseur, 1.0)


def lancer_combat(equipe, pokemon_adverse, inventaire=None, choix_libre=True):
    # Trouve le premier Pokémon vivant de l’équipe
    vivants = [p for p in equipe if p.est_vivant()]
    if not vivants:
        print("\nTous tes Pokémon sont K.O. ! Tu ne peux pas combattre.")
        return "defaite"

    pokemon_joueur = vivants[0]
    modificateur_global = 0.6  # ⚖️ Réduction générale des dégâts

    while any(p.est_vivant() for p in equipe) and pokemon_adverse.est_vivant():
        print("\n------------------------------")
        print(f"Ton Pokémon : {pokemon_joueur.nom} ({pokemon_joueur.pv}/{pokemon_joueur.pv_max} PV)")
        print(f"Adversaire : {pokemon_adverse.nom} ({pokemon_adverse.pv}/{pokemon_adverse.pv_max} PV)")
        print("------------------------------")

        print("\nQue veux-tu faire ?")
        print("1. Attaquer")
        print("2. Changer de Pokémon")
        print("3. Utiliser un objet")
        print("0. Annuler / Fuir le combat")
        choix = input("-> ").strip()

        # --- Attaquer
        if choix == "1":
            if not pokemon_joueur.est_vivant():
                print(f"\n{pokemon_joueur.nom} est K.O. et ne peut pas attaquer !")
                continue

            attaque_choisie = pokemon_joueur.choisir_attaque()
            nom_attaque, puissance = attaque_choisie

            mult = calculer_multiplicateur(pokemon_joueur.type, pokemon_adverse.type)
            degats = int(puissance * mult * modificateur_global)

            print(f"\n{pokemon_joueur.nom} attaque {pokemon_adverse.nom} !")
            print(f"{pokemon_joueur.nom} utilise {nom_attaque} !")

            if mult > 1:
                print("C’est super efficace ! 💥")
            elif mult < 1:
                print("Ce n’est pas très efficace...")

            print(f"{pokemon_joueur.nom} inflige {degats} dégâts à {pokemon_adverse.nom} !")
            pokemon_adverse.subir_degats(degats)

        # --- Changer de Pokémon
        elif choix == "2":
            print("\nChoisis un Pokémon à envoyer :")
            for i, p in enumerate(equipe, 1):
                etat = "K.O." if not p.est_vivant() else f"{p.pv}/{p.pv_max} PV"
                print(f"{i}. {p.nom} ({p.type}) - {etat}")

            choix_poke = input("-> ").strip()
            if choix_poke.isdigit():
                index = int(choix_poke) - 1
                if 0 <= index < len(equipe):
                    if equipe[index].est_vivant():
                        pokemon_joueur = equipe[index]
                        print(f"\nTu envoies {pokemon_joueur.nom} !")
                    else:
                        print(f"{equipe[index].nom} est K.O. et ne peut pas combattre !")
                else:
                    print("Choix invalide.")
            else:
                print("Entrée invalide.")

        # --- Utiliser un objet
        elif choix == "3" and inventaire:
            from items import utiliser_objet_en_combat

            print("\nObjets disponibles :")
            compteur = {}
            for item in inventaire:
                compteur[item.nom] = compteur.get(item.nom, 0) + 1
            objets_dispo = list(compteur.keys())

            for i, nom in enumerate(objets_dispo, 1):
                print(f"{i}. {nom} x{compteur[nom]}")

            choix_objet = input("-> ").strip()
            if not choix_objet.isdigit() or int(choix_objet) < 1 or int(choix_objet) > len(objets_dispo):
                print("Choix invalide.")
                continue

            objet_nom = objets_dispo[int(choix_objet) - 1]
            objet = next((it for it in inventaire if it.nom == objet_nom), None)

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
                if objet.utiliser(cible, inventaire):
                    print(f"{cible.nom} profite de {objet.nom} !")
                else:
                    print("L’objet n’a pas été utilisé.")
            else:
                print("Choix invalide.")

        # --- Fuir
        elif choix == "0":
            print("Tu fuis le combat...")
            return "annule"

        else:
            print("Choix invalide.")
            continue

        # --- L’adversaire attaque si toujours vivant
        if pokemon_adverse.est_vivant() and pokemon_joueur.est_vivant():
            attaque_adverse = random.choice(pokemon_adverse.attaques)
            nom_attaque, puissance = attaque_adverse
            mult = calculer_multiplicateur(pokemon_adverse.type, pokemon_joueur.type)
            degats = int(puissance * mult * modificateur_global)

            print(f"\n{pokemon_adverse.nom} attaque !")
            print(f"{pokemon_adverse.nom} utilise {nom_attaque} !")

            if mult > 1:
                print("C’est super efficace ! 💥")
            elif mult < 1:
                print("Ce n’est pas très efficace...")

            print(f"{pokemon_adverse.nom} inflige {degats} dégâts à {pokemon_joueur.nom} !")
            pokemon_joueur.subir_degats(degats)

        # --- Si le Pokémon du joueur tombe K.O.
        if not pokemon_joueur.est_vivant() and any(p.est_vivant() for p in equipe):
            print(f"\n{pokemon_joueur.nom} est K.O. !")
            vivants = [p for p in equipe if p.est_vivant()]
            print("Choisis un autre Pokémon pour continuer le combat :")
            for i, p in enumerate(vivants, 1):
                print(f"{i}. {p.nom} ({p.type}) - {p.pv}/{p.pv_max} PV")
            choix = input("-> ").strip()
            if choix.isdigit() and 1 <= int(choix) <= len(vivants):
                pokemon_joueur = vivants[int(choix) - 1]
                print(f"\nTu envoies {pokemon_joueur.nom} !")
            else:
                print("Choix invalide. Tu perds ton tour.")

    # --- Fin du combat
    if not any(p.est_vivant() for p in equipe):
        print("\nTous tes Pokémon sont K.O. ! Tu as perdu le combat.")
        return "defaite"
    else:
        print(f"\nTu as vaincu {pokemon_adverse.nom} !")
        return "victoire"
