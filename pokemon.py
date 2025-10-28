class Pokemon:
    
    def __init__(self, nom, type_, pv, attaque):
        self.nom = nom              # Nom du Pokémon
        self.type = type          # Type : Feu / Eau / Plante
        self.pv_max = pv            # Points de vie maximum
        self.pv = pv                # Points de vie actuels
        self.attaque = attaque      # Puissance d'attaque

    def est_vivant(self):
        return self.pv > 0
    
    def soigner(self, montant):
        self.pv = min(self.pv + montant, self.pv_max)
        print(f"{self.nom} récupère {montant} PV. ({self.pv}/{self.pv_max})")