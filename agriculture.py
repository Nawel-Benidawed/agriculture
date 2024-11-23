def indice_sante_plante(temperature, humidite_sol, luminosite):
    """
    Calcule un indice de santé de la plante basé sur 3 paramètres.
    """
    # Plage optimale pour chaque paramètre
    temp_optimale = (18, 30)  # en degrés Celsius
    humidite_optimale = (40, 70)  # en pourcentage
    luminosite_optimale = (200, 1000)  # en lux

    # Vérification des écarts par rapport à l'optimum
    score = 0

    if temp_optimale[0] <= temperature <= temp_optimale[1]:
        score += 1
    if humidite_optimale[0] <= humidite_sol <= humidite_optimale[1]:
        score += 1
    if luminosite_optimale[0] <= luminosite <= luminosite_optimale[1]:
        score += 1

    # Retourner un indice basé sur le score
    indice = (score / 3) * 100
    return indice


# Exemple d'utilisation
temperature = 25  # en °C
humidite_sol = 60  # en %
luminosite = 500  # en lux

indice = indice_sante_plante(temperature, humidite_sol, luminosite)

print(f"L'indice de santé de la plante est de : {indice:.2f}%")