# -*- coding: utf-8 -*-
"""
Created on 1.17.2020

@author: cargillb (Banks Cargill)
"""

import Dominion
import testUtility

#Get player names
player_names = testUtility.GetNames()

#number of curses and victory cards
nV = testUtility.VictoryCards(len(player_names))
nC = testUtility.CurseCards(len(player_names))

box = testUtility.GetBoxes(nV)

#supply_order = testUtility.GetSupplyOrder()
#Introducing bug: Copper in 0 and 2
supply_order = {0: ['Curse', 'Copper'], 2: ['Estate', 'Cellar', 'Chapel', 'Moat', 'Copper'],
                3: ['Silver', 'Chancellor', 'Village', 'Woodcutter', 'Workshop'],
                4: ['Gardens', 'Bureaucrat', 'Feast', 'Militia', 'Moneylender', 'Remodel', 'Smithy', 'Spy', 'Thief',
                    'Throne Room'],
                5: ['Duchy', 'Market', 'Council Room', 'Festival', 'Laboratory', 'Library', 'Mine', 'Witch'],
                6: ['Gold', 'Adventurer'], 8: ['Province']}

#Pick 10 cards from box to be in the supply.
#The supply always has these cards
supply = testUtility.SupplyBox(nV, nC, len(player_names), box)


#initialize the trash
trash = []

#Costruct the Player objects
players = testUtility.PlayerObject(player_names)

#Play the game
turn  = 0
while not Dominion.gameover(supply):
    turn += 1    
    print("\r")    
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))    
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)
            

#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)