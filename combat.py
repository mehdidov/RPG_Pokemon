import random

def lancer_combat(equipe, pokemon_sauvage, choix_libre=False):
    
    if not isinstance(equipe, list):
        equipe = [equipe]

    pokemon_joueur = equipe[0]


    print(f"\nCombat entre ton {pokemon_joueur.nom} ({pokemon_joueur.pv} PV)"
          f" et {pokemon_sauvage.nom} ({pokemon_sauvage.pv} PV) !")

    while pokemon_joueur.est_vivant() and pokemon_sauvage.est_vivant():
        print("\nTon tour")

        print(f"\nPokémon actif : {pokemon_joueur.nom} ({pokemon_joueur.pv}/{pokemon_joueur.pv_max} PV)")
        print("1. Attaquer")
        print("2. Changer de Pokémon")
        if choix_libre:
            print("3. Fuir")

        action = input("-> ").strip()

        # Attaque
        if action == "1":
            print("\nVoici tes attaques :")
            for i, atq in enumerate(pokemon_joueur.attaques, 1):
                print(f"{i}. {atq['nom']} ({atq['puissance']} dégâts, type {atq['type']})")

            choix = input("-> ").strip()

            if choix.isdigit() and 1 <= int(choix) <= len(pokemon_joueur.attaques):
                attaque_choisie = pokemon_joueur.attaques[int(choix) - 1]
            else:
                print("Choix invalide, une attaque aléatoire sera utilisée.")
                attaque_choisie = random.choice(pokemon_joueur.attaques)

            pokemon_joueur.attaquer(pokemon_sauvage, attaque_choisie)

        # Changement de pokemon
        elif action == "2":
            print("\nChoisis un autre Pokémon :")
            for i, p in enumerate(equipe, 1):
                etat = "(K.O.)" if not p.est_vivant() else f"({p.pv}/{p.pv_max} PV)"
                actif = " ← actif" if p == pokemon_joueur else ""
                print(f"{i}. {p.nom} {etat}{actif}")

            choix_pokemon = input("-> ").strip()

            if choix_pokemon.isdigit():
                index = int(choix_pokemon) - 1
                if 0 <= index < len(equipe):
                    if equipe[index].est_vivant():
                        pokemon_joueur = equipe[index]
                        print(f"\nTu envoies {pokemon_joueur.nom} au combat !")
                    else:
                        print(f"{equipe[index].nom} est K.O. ! Tu ne peux pas le choisir.")
                        continue
                else:
                    print("Numéro invalide.")
                    continue
            else:
                print("Choix invalide.")
                continue

        # Prendre la fuite
        elif action == "3" and choix_libre:
            print("Tu fuis le combat.")
            return "annule"

        else:
            print("Choix invalide.")
            continue

        # Vérifie si l'adversaire est vaincu
        if not pokemon_sauvage.est_vivant():
            print(f"{pokemon_sauvage.nom} est K.O. !")
            return "victoire"

        # Au tour de l'adversaire
        print("\nTour de l’adversaire")
        pokemon_sauvage.attaquer(pokemon_joueur)

        if not pokemon_joueur.est_vivant():
            print(f"{pokemon_joueur.nom} est K.O. !")

            vivants = [p for p in equipe if p.est_vivant()]
            if vivants:
                print("\nChoisis un autre Pokémon pour continuer le combat :")
                for i, p in enumerate(equipe, 1):
                    if p.est_vivant():
                        print(f"{i}. {p.nom} ({p.pv}/{p.pv_max} PV)")
                choix = input("-> ").strip()
                if choix.isdigit():
                    index = int(choix) - 1
                    if 0 <= index < len(equipe) and equipe[index].est_vivant():
                        pokemon_joueur = equipe[index]
                        print(f"\nTu envoies {pokemon_joueur.nom} au combat !")
                    else:
                        print("Choix invalide, fin du combat.")
                        return "defaite"
                else:
                    print("Entrée invalide, fin du combat.")
                    return "defaite"
            else:
                print("Tous tes Pokémon sont K.O. !")
                return "defaite"

    # Fin du combat 
    if not pokemon_joueur.est_vivant():
        pokemon_joueur.soigner(20)
        print(f"{pokemon_joueur.nom} reprend des forces ({pokemon_joueur.pv}/{pokemon_joueur.pv_max} PV)")
        return "defaite"

    return "fin"
