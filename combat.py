import random

def lancer_combat(pokemon_joueur, pokemon_sauvage):
    print(f"\nCombat entre ton {pokemon_joueur.nom} ({pokemon_joueur.pv} PV)"
          f" et {pokemon_sauvage.nom} ({pokemon_sauvage.pv} PV) !")

    while pokemon_joueur.est_vivant() and pokemon_sauvage.est_vivant():
        print("\nTon tour")
        print("\nVoici tes attaques :")

        for i, atq in enumerate(pokemon_joueur.attaques, 1):
            print(f"{i}. {atq['nom']} ({atq['puissance']} dégâts,type {atq['type']})")

        choix = input("-> ").strip()

        # Choix de l'attaque
        if choix.isdigit() and 1 <= int(choix) <= len(pokemon_joueur.attaques):
            attaque_choisie = pokemon_joueur.attaques[int(choix) - 1]
        else:
            print("Choix invalide, une attaque aléatoire sera utilisée.")
            attaque_choisie = random.choice(pokemon_joueur.attaques)

        # Attaque du dresseur
        pokemon_joueur.attaquer(pokemon_sauvage, attaque_choisie)

        if not pokemon_sauvage.est_vivant():
            print(f"{pokemon_sauvage.nom} est K.O. !")
            break
         # Riposte de l’adversaire
        print("\nTour de l’adversaire")
        pokemon_sauvage.attaquer(pokemon_joueur)

        if not pokemon_joueur.est_vivant():
            print(f"{pokemon_joueur.nom} est K.O. !")
            break
        # Soin léger à la fin du combat
        if not pokemon_joueur.est_vivant():
            pokemon_joueur.soigner(20)
            print(f"{pokemon_joueur.nom} reprend des forces ({pokemon_joueur.pv}/{pokemon_joueur.pv_max} PV)")
    


       