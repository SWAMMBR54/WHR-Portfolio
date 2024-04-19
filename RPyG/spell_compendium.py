#Spell Matrix
spells = [["Firebolt","Shield","Heal"],
            ["enemy","self","self"],
            [1,0,0],
            [1,3,1],
            [3,0,0],
            [3,5,7],
            ["burning","shielding","healing"],
            [2,3,5]]

#Spells
    #Spell - Firebolt
        #Launch a bolt of fire at an enemy, dealing damage
        #spellTAR = enemy (1)
        #spellDUR = instantaneous
        #spellDMG = 3
        #spellMP = 3
        #spellEFFECT = burning (2)

    #Spell - Shield
        #Shield yourself with magic, reducing the damage you take
        #spellTAR = self
        #spellDUR = 3 turns
        #spellDMG = 0
        #spellMP = 5
        #spellEFFECT = shielding (3)

    #Spell - Healing Word
        #Heal yourself with magic
        #spellTAR = self
        #spellDUR = instantaneous
        #spellDMG = 0
        #spellMP = 7
        #spellEFFECT = healing (5)