def calculer_interets(capital, taux, duree):
    if capital < 0 or taux < 0 or duree < 0:
        raise ValueError("Les valeurs doivent être positives")
    return capital * taux * duree