from players.models import Player, Item, File
from django.db.models import F
import logging
from django.conf import settings
import re
minLevel = 60
dkpPerRaid = 50

def parseRaid(f):
    #f = request.FILES['file']
    lines = f

    for x in lines:
        words = x.split()
        
        person = Player.objects.filter(playerName=words[1].decode())
        if person:
            logging.debug("giving check to: " + words[1].decode())
            person.update(currentDKP=F('currentDKP') + dkpPerRaid)
            person.update(checksEarned=F('checksEarned') + 1)
    #Update all players potential checks     
    Player.objects.all().update(checksAvail=F('checksAvail')+1)
    logging.debug("Raid Dump Parsed")

def parseGuild(request):
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
def parseWins(request):
    f = request.FILES['file']
    lines = f.readlines()
    items = []
    with open('E:\Programs\Python\Web\mysite\mysite\out.txt', 'w') as destination:
        #Clean the line and take out needed info
        for x in lines:
            x = x.decode() #cast from byte-form to string
            words = x.split()
            if "You say to your guild" in x:
                words.remove("You")
                #logging.debug(words)
            index = 9 #where we start parsing for item name
            item = ""

            month = words[1]
            #need python 3.10+ for match statements
            if month == "Jan":
                month = "01"
            elif month == "Feb":
                month = "02"
            elif month ==  "Mar":
                month = "03"
            elif month ==  "Apr":
                month = "04"
            elif month ==  "May":
                month = "05"
            elif month ==  "Jun":
                month = "06"
            elif month ==  "Jul":
                month = "07"
            elif month ==  "Aug":
                month = "08"
            elif month ==  "Sep":
                month = "09"
            elif month ==  "Oct":
                month = "10"
            elif month ==  "Nov":
                month = "11"
            elif month ==  "Dec":
                month = "12"

            day = words[2]
            year = words[4][:-1] #removes end '

            dateForm = day + "/" + month + "/" + year
            
            #pieces together the item name
            while words[index] != ';':
                item = item + words[index]
                item = item + ' '
                index = index + 1
            item = item[1:] #removes first '
            item = item[:-1]#removes extra space
            amount = words[index + 1]
            winner = words[index + 3].capitalize()

            person = Player.objects.filter(playerName=winner)
            if not person: #THROW ERROR OF SOME KIND HERE, getting misspelled names as new characters
                person = Player(playerName=winner, playerClass="Warrior", playerType="New")
                person.save()
            person.update(currentDKP=F('currentDKP') - amount)
            newItem = {'winner': winner, 'item': item, 'amount' : amount, 'date' : dateForm}
            items.append(newItem)

            #logging.debug(dateForm)
            #logging.debug(item)
            #logging.debug(amount)
            #logging.debug(winner)

    return items

    #OLD FORMAT, NO LONGER USED
    # words = x.split()
    # itemIndex = len(words) - 13
    # item = ""
    # winner = words[12].decode().capitalize()
    # destination.write("[Winner: " + winner)
    # for y in range(itemIndex):
    #     item = item + words[13 + y].decode()
    #     if y < itemIndex:
    #         item = item + " "
    # item = item[:-2]
    # destination.write(" Item: " + item + "]")
    # person = Player.objects.filter(playerName=winner)
    # if person:
    #     newItem = {'winner': winner, 'item': item}
    #     items.append(newItem)

def applyWins(request):
    logging.debug("INSIDE APPLYWINS FUNC")
    logging.debug(request.session['winsList'])
    #THIS IS WHERE WE NEED TO APPLY THE CHANGES!
    for entry in request.session['winsList']:
        winnerName = entry['winner']
        item = entry['item']
        amount = entry['amount']
        date = entry['date']
        #play nice with required date formatting, this puts into YYYY-DD-MM
        dateForm = date[6:] + '-' + date[3:5] + '-' + date[0:2]
        newItem = Item(itemName=item,winner=winnerName, price=amount, itemDate=dateForm)
        newItem.save()
    return request