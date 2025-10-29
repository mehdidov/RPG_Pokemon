import random

def lancer_combat(equipe, pokemon_adverse, inventaire=None, choix_libre=True):
    pokemon_joueur = equipe[0]

    while pokemon_joueur.est_vivant() and pokemon_adverse.est_vivant():
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
            attaque_choisie = pokemon_joueur.choisir_attaque()
            nom_attaque, puissance = attaque_choisie
            print(f"\n{pokemon_joueur.nom} attaque {pokemon_adverse.nom} !")
            print(f"{pokemon_joueur.nom} utilise {nom_attaque} et inflige {puissance} dégâts !")
            pokemon_adverse.subir_degats(puissance)

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
            # Import ici pour éviter dépendance circulaire
            from items import utiliser_objet_en_combat

            # Affiche les objets disponibles
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

            # Demande sur quel Pokémon utiliser l’objet
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
        if pokemon_adverse.est_vivant():
            attaque_adverse = random.choice(pokemon_adverse.attaques)
            nom_attaque, puissance = attaque_adverse
            print(f"\n{pokemon_adverse.nom} attaque !")
            print(f"{pokemon_adverse.nom} utilise {nom_attaque} et inflige {puissance} dégâts !")
            pokemon_joueur.subir_degats(puissance)

    # --- Fin du combat
    if pokemon_joueur.est_vivant():
        print(f"\nTu as vaincu {pokemon_adverse.nom} !")
        return "victoire"
    else:
        print(f"\n{pokemon_joueur.nom} est K.O. !")
        return "defaite"
