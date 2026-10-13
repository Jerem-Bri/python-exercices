produit = "Clavier"
prix_ht = 19.90 
quantite = 3
taux_tva = 0.2

total_ht = prix_ht * quantite
total_ttc = total_ht * (1 + taux_tva)

print(f"{quantite} x {produit} : {round(total_ttc, 2)} euros TTC")