from players.models import Player, Item, File
from django.db.models import F
minLevel = 60
dkpPerRaid = 50

def parseRaid(request, form):
    f = request.FILES['file']
    lines = f.readlines()
    with open('E:\Programs\Python\Web\mysite\mysite\out.txt', 'w') as destination:
        for x in lines:
            words = x.split()
            for y in words:
                person = Player.objects.filter(playerName=y.decode())
                if person:
                    destination.write(y.decode() + "FOUND\n")
                    person.update(currentDKP=F('currentDKP') + dkpPerRaid)
                    person.update(checksEarned=F('checksEarned') + 1)
    #Update all players potential checks                
    Player.objects.all().update(checksAvail=F('checksAvail')+1)

def parseGuild(request, form):
    f = request.FILES['file']
    lines = f.readlines()
    with open('E:\Programs\Python\Web\mysite\mysite\out.txt', 'w') as destination:
        for x in lines:
            words = x.split()
            person = Player.objects.filter(playerName=words[0].decode())
            if person:
                person.update(playerType=words[3].decode())
            elif int(words[1].decode()) >= minLevel:
                if words[2].decode() == "Shadow":
                    words[2] = b"Shadowknight"
                    words.remove(b"Knight")
                destination.write("ADD " + words[0].decode() + " the " + words[2].decode() + " as " + words[3].decode() + "|||\n")
                newPlayer = Player(playerName=words[0].decode(), playerClass=words[2].decode(), playerType=words[3].decode())
                newPlayer.save()
#Winner = words[12]
#Item = words[13] -> words[end - 1]
#Cost = words[end]
def parseWins(request, form):
    f = request.FILES['file']
    lines = f.readlines()
    items = []
    with open('E:\Programs\Python\Web\mysite\mysite\out.txt', 'w') as destination:
        for x in lines:
            words = x.split()
            itemIndex = len(words) - 13
            item = ""
            winnerName = words[12].decode().capitalize()
            destination.write("[Winner: " + winnerName)
            for y in range(itemIndex):
                item = item + words[13 + y].decode()
                if y < itemIndex:
                    item = item + " "
            item = item[:-2]
            destination.write(" Item: " + item + "]")
            person = Player.objects.filter(playerName=winnerName)
            if person:
                newItem = Item(itemName=item, winner=winnerName)
                items.append(newItem)
    return items
