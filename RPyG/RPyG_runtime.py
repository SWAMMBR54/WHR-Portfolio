#Setup - Module Imports
import math
import random
import os
import time
from enemy_compendium import *
from spell_compendium import *
from item_compendium import *

#Setup - Starting Variables
player_baseMaxHP = 10
player_baseATK = 2
player_baseDEF = 2
player_baseATKSPD = 1 
player_baseMaxMP = 0

#Setup - Game Start Variables
roundCount = 0

player_currentmaxHP = player_baseMaxHP
player_currentHP = player_baseMaxHP
player_currentATK = player_baseATK
player_currentDEF = player_baseDEF
player_currentATKSPD = player_baseATKSPD
player_currentMaxMP = player_baseMaxMP
player_currentMP = player_baseMaxMP

enemyChoice = 0
enemyHealth = 0
enemyATKSPD = 0

itemINV = []
spellINV= []

#Setup - Functions
def nextRound():
    global enemyChoice
    global enemyHealth
    global enemyATKSPD
    global roundCount
    roundCount += 1
    if roundCount in range(1,3):
        enemyChoice = random.randint(0,2)
        enemyHealth = enemy_forest[1][enemyChoice]
        enemyATKSPD = enemy_forest[4][enemyChoice]

def playerAction():
    global enemyHealth
    playerAction = input("Choose an Action: \n > Attack \n > Magic \n > Item \n > Flee \n \n > ")
    os.system("cls")
    if playerAction == "Attack" or playerAction == "attack":
        print("Hit!")
        print()
        enemyHealth -= player_currentATK
    elif playerAction == "Magic" or playerAction == "magic":
        if player_currentMaxMP > 0:
            openSpellMenu()
        else: 
            print("You can't cast magic!")
            print()
    elif playerAction == "Item" or playerAction == "item":
        os.system("cls")
        if len(itemINV) > 0:
            openItemMenu()
        else:
            print("You don't have any items!")
        print()
    elif playerAction == "Flee" or playerAction == "flee":
        print("You run away!")
        print()

def openSpellMenu():
    if len(spellINV) > 0:
        print("Choose a Spell:")
        for i in range(len(spellINV[0])):
            print("> " + spellINV[0][i])
        print()
        input("> ")
        print()
        time.sleep(5)
    else:
        print("You don't know any spells!")
        print()
        time.sleep(5)

def openItemMenu():
    print("Choose an item:")
    for i in range(len(itemINV[0])):
        print("> " + itemINV[0][i])
    print()
    input("> ")
    print()

def determineTurnOrder():
    global enemyATKSPD
    if player_currentATKSPD > enemyATKSPD:
        return "p1"
    else:
        return "e1"

def enemyAttack():
    global enemyChoice
    global player_currentHP
    enemyDMG = enemy_forest[2][enemyChoice]
    os.system("cls")
    print("You take " + str(enemyDMG) + " damage!")
    player_currentHP -= enemyDMG

#Game - Runtime
os.system("cls")
nextRound()
while enemyHealth > 0 and player_currentHP > 0:
    if player_currentMaxMP > 0:
        print()
        print(enemy_forest[0][enemyChoice])
        print("HP: " + str(enemyHealth) + "/" + str(enemy_forest[1][enemyChoice]) + "\n\n")
        print("You:")
        print("HP: " + str(player_currentHP) + "/" + str(player_baseMaxHP) + "    MP: " + str(player_currentMP) +"/" + str(player_currentMaxMP))
        print("-----------")
        playerAction()
        enemyAttack()
    else:
        print()
        print(enemy_forest[0][enemyChoice])
        print("HP: " + str(enemyHealth) + "/" + str(enemy_forest[1][enemyChoice]) + "\n\n")
        print("You:")
        print("HP: " + str(player_currentHP) + "/" + str(player_baseMaxHP))
        print("-----------")
        playerAction()
        enemyAttack()
if enemyHealth <= 0:
    print("The " + str(enemy_forest[0][enemyChoice]) + " has been slain!")
    print()
elif player_currentHP <= 0:
    print("GAME OVER")
    print("You were slain by " + str(enemy_forest[0][enemyChoice]) + ".")
    print()