import requests
import json
summonername="IlIIIIlIll"
accountname="zBQt3mpf7jSLaPoE5dAdRr80a0yEhfc4npB7MrRn2LjKEnzHx4SQsz0H"
APIkey="RGAPI-126d845f-4bbf-4092-9c7b-a145caf92e82"

listematch=requests.get("https://euw1.api.riotgames.com/lol/match/v4/matchlists/by-account/"+ accountname +"?api_key="+APIkey)
listematch=listematch.json()

listeidmatch=[]


for i in listematch['matches']:
    listeidmatch.append(i['gameId'])

champduree={}
fichiertemps = open("Tempsgames.txt", "w")

for matchid in listeidmatch:
    detailsmatch=requests.get("https://euw1.api.riotgames.com/lol/match/v4/matches/" + str(matchid) + "?api_key=" + APIkey)
    detailsmatch=detailsmatch.json()
    duree=detailsmatch['gameDuration']
    participants=detailsmatch['participantIdentities']
    if len(participants)>1 and detailsmatch['queueId']==840:
        fichiertemps.write("\n"+str(duree//60)+":"+str(duree%60))
        for num in range(5,10):
            nom=participants[num]['player']['summonerName']
            if nom in champduree:
                champduree[nom].append(duree)
            else:
                champduree[nom]=[duree]

fichiertemps.close()


moyennebot={}

for champ in champduree.keys():
    somme=0
    for temps in champduree[champ]:
        somme+=temps
    moyenne=int(somme/len(champduree[champ]))
    moyennebot[champ]=moyenne
    

moyennebot=sorted(moyennebot.items(), key=lambda t: t[1])


fichierbots = open("TempsChampBot.txt", "w")
for i in moyennebot:
    fichierbots.write("\n"+ i[0] + ";" +str(i[1]//60)+":"+str(i[1]%60))
fichierbots.close()

print("---Script terminé---")