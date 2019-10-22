from dictionnaire import villes

def salut(start, end):
    ## Gestion de la casse
    start = start.lower().capitalize()
    end = end.lower().capitalize()
    timeDuringAccAndDecc = 18
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
    distance = distance - (timeOut() * nbPause)
    ## Temps mis sans les pauses en minutes
    timeWithoutPause = (distance / maxSpeed) / 60
    ## 
    time =  timeWithoutPause + (timeDuringAccAndDecc + timeOutTime) * nbPause
    ## Conversion temps en heure pleines
    heures = int(time/60)
    minutes = int(round(((time/60) % 1),2) * 60)
    return "Le temps nécessaire pour faire {} - {} est de {} heures {} minutes.".format(start, end, heures, minutes)

def timeOut():
    averageSpeed = 50/3.6
    time = 18*60
    distanceTravelled = averageSpeed * time
    return distanceTravelled

print("Entrez la ville de départ : ")
ntm = input()
print("Entrez la ville d'arrivée : ")
fdp = input()


print("-------------------------")
print(salut(ntm, fdp))
print("-------------------------")