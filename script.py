from dictionnaire import villes
import argparse

def calculRoutier():
    print("Entrez la ville de départ : ")
    start = input()
    print("Entrez la ville d'arrivée : ")
    end = input()
    ## Gestion de la casse
    start = start.lower().capitalize()
    end = end.lower().capitalize()
    ## Déclaration variables
    timeDuringAcc = 9
    timeDuringDecc = 9
    timeOutTime = 15
    ## Conversion en km/h à m/s
    maxSpeed = 90/3.6
    ## Conversion de kilomètres à mètres
    distance = villes[start][end] * 1000
    ## Temps si la vitesse et constante et sans pause
    maxTime = (distance / maxSpeed) / 60
    ## Nombre de pauses
    nbPause = (maxTime // 60) // 2
    ## Distance parcourue sans la distance parcourus avec la décelération et l'accélération
    distance = distance - ((acceleration() + decceleration()) * nbPause + 1)
    ## Temps mis sans les pauses en minutes
    timeWithoutPause = (distance / maxSpeed) / 60
    ## Temps en minutes avec les pauses
    time =  timeWithoutPause + (timeDuringAcc + timeDuringDecc + timeOutTime) * nbPause + 1
    ## Conversion temps en heure pleines
    heures = int(time/60)
    minutes = int(round(((time/60) % 1),2) * 60)
    print("-------------------------")
    print("Le temps nécessaire pour faire {} - {} est de {} heures {} minutes.".format(start, end, heures, minutes))
    print("-------------------------")
    return int(time)

def acceleration():
    averageSpeed = 50/3.6
    time = 9*60
    distanceTravelled = averageSpeed * time
    return distanceTravelled

def decceleration():
    averageSpeed = 50/3.6
    time = 9*60
    distanceTravelled = averageSpeed * time
    return distanceTravelled

def travelwithStep(numberOfCities):
    cities = []
    for i in range(numberOfCities):
        cities.append(input('Veuillez entrer la nom de la ville numéro {} :\n'.format(i+1)))
    print(cities)


if __name__ == "__main__":
    # travelwithStep(4)
    print(calculRoutier())