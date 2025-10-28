def lancer_combat(pokemon_joueur, pokemon_sauvage):
    

    print(f"\nCombat entre ton {pokemon_joueur.nom} ({pokemon_joueur.pv} PV)"
          f" et {pokemon_sauvage.nom} ({pokemon_sauvage.pv} PV) !")

    while pokemon_joueur.est_vivant() and pokemon_sauvage.est_vivant():
        
        pokemon_joueur.attaquer(pokemon_sauvage)

        if not pokemon_sauvage.est_vivant():
            print(f"{pokemon_sauvage.nom} est K.O. !")
            break

    
        pokemon_sauvage.attaquer(pokemon_joueur)

        if not pokemon_joueur.est_vivant():
            print(f"{pokemon_joueur.nom} est K.O. !")
            break

    
    if not pokemon_joueur.est_vivant():
        pokemon_joueur.soigner(20)
        print(f"{pokemon_joueur.nom} reprend un peu de forces. "
              f"({pokemon_joueur.pv}/{pokemon_joueur.pv_max} PV)")
