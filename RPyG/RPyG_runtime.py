#Setup - Module Imports
import math
import random
import os
import time
from enemy_compendium import *
from spell_compendium import *
from item_compendium import *
from class_compendium import *

#Setup - Variables
roundCount = 0
turnOrder = ""
interCheck = "false"

player_HP = 0
player_MP = 0
player_maxHP = 0
player_maxMP = 0
player_ATK = 0
player_DEF = 0
player_ATKSPD = 0
player_shield = 0

enemyChoice = 0
enemyName = ""
enemyHealth = 0
enemyATKSPD = 0

itemINV = [["null"],["null"]]
spellINV= []

#Setup - Functions
def inputCheck(inp,comp):
    inpCheck = inp.lower()
    compCheck = comp.lower()
    if inpCheck == compCheck:
        return "true"
    else: 
        return "false"

def chooseClass():
    global player_HP
    global player_MP
    global player_maxHP
    global player_maxMP
    global player_ATK
    global player_DEF
    global player_ATKSPD
    global spellINV
    os.system("cls")
    print("Choose your class: \n > Knight \n > Rogue \n > Mage \n \n")
    classChoice = input("> ")
    for i in range(len(classes[0])):
        if inputCheck(classChoice, classes[0][i]) == "true": 
            player_HP = classes[1][i]
            player_MP = classes[2][i]
            player_maxHP = classes[1][i]
            player_maxMP = classes[2][i]
            player_ATK = classes[3][i]
            player_DEF = classes[4][i]
            player_ATKSPD = classes[5][i]
    if inputCheck(classChoice, classes[0][2]) == "true":
        for i in range(len(spells[0])):
            spellINV.append(spells[0][i])

def nextRound():
    global player_shield
    global enemyChoice
    global enemyName
    global enemyHealth
    global enemyATKSPD
    global roundCount
    global turnOrder
    global interCheck
    if roundCount != 0:
        interCheck = "true"
        interRound()
    interCheck = "false"
    roundCount += 1
    if player_shield > 0:
        player_shield -= 1
    if roundCount == 1:
        os.system("cls")
        print("You enter the forest...")
        time.sleep(1.5)
    if roundCount in range(1,6):
        enemyChoice = random.randint(0,2)
        enemyName = enemy_forest[0][enemyChoice]
        enemyHealth = enemy_forest[1][enemyChoice]
        enemyATKSPD = enemy_forest[4][enemyChoice]
    turnOrder = determineTurnOrder()
    if enemyName[0] == "a" or enemyName[0] == "e" or enemyName[0] == "i" or enemyName[0] == "o" or enemyName[0] == "u":
        os.system("cls")
        print("You encounter an " + enemyName + "!")
        print()
        time.sleep(1.5)
    else:
        os.system("cls")
        print("You encounter a " + enemyName + "!")
        print()
        time.sleep(1.5)

def playerAction():
    global enemyName
    global enemyHealth
    global player_ATK
    global player_maxMP
    if player_maxMP > 0:
        os.system("cls")
        print(enemyName)
        print("HP: " + str(enemyHealth) + "/" + str(enemy_forest[1][enemyChoice]) + "\n\n")
        print("You:")
        print("HP: " + str(player_HP) + "/" + str(player_maxHP) + "    MP: " + str(player_MP) +"/" + str(player_maxMP))
        print("-----------")
    else:
        os.system("cls")
        print(enemyName)
        print("HP: " + str(enemyHealth) + "/" + str(enemy_forest[1][enemyChoice]) + "\n\n")
        print("You:")
        print("HP: " + str(player_HP) + "/" + str(player_maxHP))
        print("-----------")
    action = input("Choose an Action: \n > Attack \n > Magic \n > Item \n \n > ")
    if action == "Attack" or action == "attack":
        os.system("cls")
        print("You hit the " + str(enemyName) + " for " + str(player_ATK) + " damage!")
        print()
        time.sleep(1.5)
        enemyHealth -= player_ATK
    elif action == "Magic" or action == "magic":
        os.system("cls")
        if player_maxMP > 0:
            if len(spellINV) > 0:
                if player_MP != 0:
                    openSpellMenu()
                else:
                    print("You don't have any Mana!")
            else:
                print("You don't know any spells!")
                print()
                time.sleep(1.5)
            print()
            playerAction()
        else: 
            print("You can't cast magic!")
            print()
            time.sleep(1.5)
            playerAction()
    elif action == "Item" or action == "item":
        os.system("cls")
        if len(itemINV) > 0:
            if itemINV[0][0] != "null":
                openItemMenu()
            else:
                print("You don't have any items!")
                print()
                time.sleep(1.5)  
        else:
            print("You don't have any items!")
            print()
            time.sleep(1.5)
        print()
        playerAction()
    else:
        os.system("cls")
        print("Please enter a valid action! \n")
        time.sleep(1.5)
        playerAction()

def openSpellMenu():
    global spellINV
    os.system("cls")
    print("Choose a Spell:")
    for i in range(len(spellINV)):
        print("> " + spellINV[i])
    print("> Cancel")
    print()
    spellChoice = input("> ")
    print()
    if inputCheck(spellChoice, "Cancel") == "false":
        castSpell(spellChoice)

def castSpell(sChoice):
    global spellINV
    global player_HP
    global player_MP
    global enemyHealth
    global player_shield
    for i in range(len(spellINV)):
        if inputCheck(sChoice, spellINV[i]) == "true":
            for j in range(len(spells[0])):
                if inputCheck(sChoice, spells[0][j]) == "true":
                    if player_MP >= spells[5][j]:
                        if spells[1][j] == "enemy":
                            if spells[4][j] > 0:
                                enemyHealth -= spells[4][j]
                                player_MP -= spells[5][j]
                                os.system("cls")
                                print("You cast " + spells[0][j]+ "! \n")
                                print("Your spell hits the " + enemyName + " for " + str(spells[4][j]) + " damage!")
                                time.sleep(1.5)
                        else:
                            if spells[6][j] == "shielding":
                                player_shield += spells[7][j]
                                player_MP = spells[5][j]
                                os.system("cls")
                                print("You cast " + spells[0][j]+ "! \n")
                                print("You gain a shield for " + str(spells[7][j]) + " turns!")
                                time.sleep(1.5)
                            elif spells[6][j] == "healing":
                                if (player_HP + spells[7][j]) <= player_maxHP:
                                    os.system("cls")
                                    print("You cast " + spells[0][j]+ "! \n")
                                    print("You heal " + str(spells[7][j]) + " HP!")
                                    player_HP += spells[7][j]
                                    player_MP -= spells[5][j]
                                elif player_HP < player_maxHP and (player_HP + spells[7][j]) > player_maxHP:
                                    os.system("cls")
                                    print("You cast " + spells[0][j]+ "! \n")
                                    print("You heal " + str(player_maxHP - player_HP) + " HP!")
                                    player_HP = player_maxHP
                                    player_MP -= spells[5][j]
                                else:
                                    os.system("cls")
                                    print("You're already at max HP!")
                                time.sleep(1.5)
                    else:
                        print("You don't have enough Mana!")
                        time.sleep(1.5)
                        openSpellMenu()

def openItemMenu():
    global itemINV
    os.system("cls")
    print("Choose an item:")
    for i in range(len(itemINV[0])):
        print("> " + itemINV[0][i] + " (" + str(itemINV[1][i]) + ")")
    print("> Cancel")
    print()
    itemChoice = input("> ")
    print()
    if inputCheck(itemChoice, "Cancel") == "true":
        if interCheck == "true":
            interRound()
    else:
        useItem(itemChoice)
        if interCheck == "true":
            interRound()

def useItem(iChoice):
    global itemINV
    global player_HP
    global player_maxHP
    global player_MP
    global player_maxMP
    for i in range(len(itemINV[0])):
        if inputCheck(iChoice, itemINV[0][i]) == "true":
            if len(itemINV[0]) > 1:
                if itemINV[1][i] > 1:
                        itemINV[1][i] -= 1
                else:
                        itemINV.pop([0][i])
                        itemINV.pop([1][i])
            else:
                if itemINV[1][i] > 1:
                        itemINV[1][i] -= 1
                else:
                        itemINV[0][i] = "null"
                        itemINV[1][i] = "null"
            for j in range(len(items[0])):
                if inputCheck(iChoice, items[0][j]) == "true":
                    if items[1][j] == "healing":
                        if (player_HP + items[2][j]) <= player_maxHP:
                            os.system("cls")
                            print("You heal " + str(items[2][j]) + " HP!")
                            player_HP += items[2][j]
                        elif player_HP < player_maxHP and (player_HP + items[2][j]) > player_maxHP:
                            os.system("cls")
                            print("You heal " + str(player_maxHP - player_HP) + " HP!")
                            player_HP = player_maxHP
                        else:
                            os.system("cls")
                            print("You're already at max HP!")
                        time.sleep(1.5)
                    elif items[1][j] == "MPrestore":
                        if (player_MP + items[2][j]) <= player_maxMP:
                            os.system("cls")
                            print("You replenish " + str(items[2][j]) + " MP!")
                            player_MP += items[2][j]
                        elif player_MP < player_maxMP and (player_MP + items[2][j]) > player_maxMP:
                            os.system("cls")
                            print("You replenish " + str(player_maxMP - player_MP) + " MP!")
                            player_MP = player_maxMP
                        else:
                            os.system("cls")
                            print("You're already at max MP!")
                        time.sleep(1.5)
        else:
            print("You don't have that item!")
            time.sleep(1.5)
            openItemMenu()

def determineTurnOrder():
    global player_ATKSPD
    global enemyATKSPD
    if player_ATKSPD > enemyATKSPD or player_ATKSPD == enemyATKSPD:
        return 1
    else:
        return 0

def enemyAttack():
    global player_HP
    global player_shield
    global enemyChoice
    global enemyName
    enemyDMG = enemy_forest[2][enemyChoice]
    os.system("cls")
    if player_shield > 0:
        reducedEnemyDMG = int(enemyDMG/2)
        print("The " + enemyName + " hits you for " + str(reducedEnemyDMG) + " damage!")
    else:
        print("The " + enemyName + " hits you for " + str(enemyDMG) + " damage!")
    print()
    time.sleep(1.5)
    player_HP -= enemyDMG

def deathCheck():
    global enemyHealth
    global player_HP
    if enemyHealth <= 0:
        os.system("cls")
        print("The " + str(enemy_forest[0][enemyChoice]) + " has been slain!")
        print()
        time.sleep(1.5)
        lootDrops()
        os.system("cls")
    if player_HP <= 0:
        os.system("cls")
        print("GAME OVER")
        print("You were slain by " + str(enemy_forest[0][enemyChoice]) + ".")
        print()
        time.sleep(1.5)
        exit()

def lootDrops():
    global enemyName
    global itemINV
    dropChance = random.randint(0,10)
    if dropChance > 4:
        itemDropped = random.randint(1,10)
        if itemDropped in range(1,6):
            print("The " + enemyName + " dropped a Potion of Minor Healing!")
            if itemINV[0][0] == "null":
                itemINV[0][0] = items[0][0]
                itemINV[1][0] = 1
            elif items[0][0] in itemINV[0]:
                for i in range(len(itemINV[0])):
                    if itemINV[0][i] == items[0][0]:
                        itemINV[1][i] += 1
            else:
                itemINV[0].append(items[0][0])
                itemINV[1].append(1)
        elif itemDropped in range(6,9):
            print("The " + enemyName + " dropped a Potion of Mana!")
            if itemINV[0][0] == "null":
                itemINV[0][0] = items[0][2]
                itemINV[1][0] = 1
            elif items[0][2] in itemINV[0]: 
                for i in range(len(itemINV[0])):
                    if itemINV[0][i] == items[0][2]:
                        itemINV[1][i] += 1
            else:
                itemINV[0].append(items[0][2])
                itemINV[1].append(1)
        else:
            print("The " + enemyName + " dropped a Potion of Major Healing!")
            if itemINV[0][0] == "null":
                itemINV[0][0] = items[0][1]
                itemINV[1][0] = 1
            elif items[0][1] in itemINV[0]:
                for i in range(len(itemINV[0])):
                    if itemINV[0][i] == items[0][1]:
                        itemINV[1][i] += 1
            else:
                items[0].append(items[0][1])
                itemINV[1].append[1]
        time.sleep(1.5)

def interRound():
    global player_maxHP
    global player_maxMP
    if player_maxMP > 0:
        os.system("cls")
        print("You find a place to rest...")
        print()
        print("You:")
        print("HP: " + str(player_HP) + "/" + str(player_maxHP) + "    MP: " + str(player_MP) +"/" + str(player_maxMP))
        print("-----------")
    else:
        os.system("cls")
        print("You find a place to rest...")
        print()
        print("You:")
        print("HP: " + str(player_HP) + "/" + str(player_maxHP))
        print("-----------")
    action = input("Choose an Action: \n > Continue \n > Item \n \n > ")
    if action == "Continue" or action == "continue":
        os.system("cls")
        print("You keep going...")
        time.sleep(1.5)
        return
    elif action == "Item" or action == "item":
        os.system("cls")
        if len(itemINV) > 0:
            if itemINV[0][0] != "null":
                openItemMenu()
            else:
                print("You don't have any items!")
                time.sleep(1.5)  
                interRound()
        else:
            print("You don't have any items!")
            print()
            time.sleep(1.5)
    else:
        os.system("cls")
        print("Please enter a valid action! \n")
        time.sleep(1.5)
        interRound()

#Game - Runtime
os.system("cls")
gameStart = input("Start a new adventure? Y/N: \n \n > ")
if gameStart == "Y" or gameStart == "y":
    chooseClass()
    while player_HP > 0:
        nextRound()
        while enemyHealth > 0 and player_HP > 0:
            if turnOrder == 1:
                playerAction()
                deathCheck()
                if enemyHealth > 0:
                    enemyAttack()
                    deathCheck()
            else:
                if enemyHealth > 0:
                    enemyAttack()
                    deathCheck()
                playerAction()
                deathCheck()
else:
    print("Ok then, go home!")