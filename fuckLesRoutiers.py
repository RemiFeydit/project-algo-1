from dictionnaire import villes

def salut(start, end):
    maxSpeed = 90/3.6
    start = start.lower().capitalize()
    end = end.lower().capitalize()
    distance = villes[start][end] / 1000
    maxTime = distance / maxSpeed
    # heures = int((distance / maxSpeed))
    # minutes = int(60 * (round((distance / maxSpeed), 2) % 1))
    # return "Le temps nécessaire pour faire {} - {} est de {} heures {} minutes.".format(start, end, heures, minutes)



print("Entrez la ville de départ : ")
ntm = input()
print("Entrez la ville d'arrivée : ")
fdp = input()


print("-------------------------")
print(salut(ntm, fdp))
print("-------------------------")