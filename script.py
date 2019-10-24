from dictionnaire import villes
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-nc", "--numbers-cities", metavar = '', help="Number of cities you want to go", type=int)
args = parser.parse_args()

def calculRoutier(start, end):
    global distance
    ## Déclaration variables
    timeDuringAcc = 9
    timeDuringDecc = 9
    timeOutTime = 15
    distance = villes[start][end]
    ## Conversion en km/h à m/s
    maxSpeed = 90/3.6
    ## Conversion de kilomètres à mètres
    distanceMètres = distance * 1000
    ## Temps si la vitesse et constante et sans pause
    maxTime = (distance / maxSpeed) / 60
    ## Nombre de pauses
    nbPause = (maxTime // 60) // 2
    ## Distance parcourue sans la distance parcourus avec la décelération et l'accélération
    distanceMètres = distanceMètres - ((acceleration() + decceleration()) * nbPause + 1)
    ## Temps mis sans les pauses en minutes
    timeWithoutPause = (distanceMètres / maxSpeed) / 60
    ## Temps en minutes avec les pauses
    time =  timeWithoutPause + (timeDuringAcc + timeDuringDecc + timeOutTime) * nbPause + 1
    ## Conversion temps en heure pleines
    hours = int(time/60)
    minutes = int(round(((time/60) % 1),2) * 60)
    print("--------- Récapitulatif trajet -------------")
    print("{} ---> {} | {:02d}:{:02d} | {} kilomètres\n".format(start, end, hours, minutes, distance))
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
    global distance
    cities = []
    travelTime = 0
    totalDistance = 0
    for i in range(numberOfCities):
        cities.append(input('Veuillez entrer la nom de la ville numéro {} :\n'.format(i+1)).lower().title())
    for i in range(numberOfCities-1):
        travelTime += calculRoutier(cities[i], cities[i+1])
        totalDistance += distance
    travelTime += 45 * (numberOfCities-2)
    travelTimeH = travelTime/60
    hours = int(travelTimeH)
    minutes = int(round(((travelTimeH) % 1),2) * 60)
    print("--------------- Total trajet ---------------")
    return "{} <<<>>> {} | {:02d}:{:02d} | {} kilomètres".format(cities[0], cities[numberOfCities-1], hours, minutes, totalDistance)



if __name__ == "__main__":
    if(args.numbers_cities > 1):
        print(travelwithStep(args.numbers_cities))
    else:
        print("Veuillez entrer le bon argument")