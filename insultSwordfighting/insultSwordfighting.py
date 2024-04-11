#module_imports
import random
import time

#control_variables
phealth = 3
bhealth = 3

#functions
#categorized with "func/[section name]" for easy review

#func/game_control

#func/game_control/tutorial
def tutorialask():
    print("Before we begin, would you like a quick tutorial?")
    print("1) Yes")
    print("2) No")
    tuta = int(input())
    if tuta == 1:
        print("Captain Smirk: Let's go through a quick tutorial!")
        tutorial()
    elif tuta == 2:
        time.sleep(0.5)
        print("Its time for some Insult Swordfighting!")
        time.sleep(1)

def tutorial():
    time.sleep(1)
    tutorialtext()
    time.sleep(1.5)
    print("Captain Smirk: You need to hear that again?")
    time.sleep(0.5)
    print("1) Yes")
    time.sleep(0.5)
    print("2) No")
    tutresponse = int(input())
    if tutresponse == 1:
        time.sleep(1)
        print("Captain Smirk: Right then. Listen carefully this time!")
        tutorial()
    else:
        print("Captain Smirk: Now go on out there and hurt some feelings!")

def tutorialtext():
    time.sleep(2)
    print("Captain Smirk: On these waters, knowing how to swing a sword is great, but knowing how to disorient your oppoent is even more important!")
    time.sleep(2)
    print("Captain Smirk: We can cross blades all day, but what if I were to suddenly say...")
    time.sleep(2)
    print("Captain Smirk: My swordplay will amaze you!")
    time.sleep(2)
    print("Captain Smirk: See? I can already see the smoke coming out of your ears!")
    time.sleep(2)
    print("Captain Smirk: But insulting someone is only half the battle: You have to be able to dole out a retort as well!")
    time.sleep(2)
    print("Captain Smirk: When I say \"My swordplay will amaze you!\", you need to respond with something like...")
    time.sleep(2)
    print("Captain Smirk: \"Yeah - I'm amazed you've lasted this long\"")
    time.sleep(2)
    print("Captain Smirk: That's the gist of it. Insult, then Retort. And don't forget to stay on guard!\nYou might be insulting each other, but you're still swordfighting!")

#func/game_control/game_start
def gamestart():
    firststrike = first = random.randint(0, 1)
    if firststrike == 1:
        print("You'll make the first strike!")
        while phealth != 0 and bhealth != 0:
            offround()
            defround()
    elif firststrike == 0:
        print("You'll take the first blow!")
        while phealth != 0 and bhealth != 0:
            defround()
            offround()

#func/game_control/game_running
def runtime():
    tutorialask()
    gamestart()

#func/player_options
def insultoptions():
    print("Choose an insult:")
    time.sleep(0.75)
    print("1) My swordplay will amaze you!")
    time.sleep(0.75)
    print("2) My deeds are spoken of worldwide!")
    time.sleep(0.75)
    print("3) I've met pigs that are scarier than you!")
    pIns = int(input())
    if pIns == 1:
        print("You: My swordplay will amaze you!")
        return pIns
    elif pIns == 2:
        print("You: My deeds are spoken of worldwide!")
        return pIns
    elif pIns == 3:
        print("You: I've met pigs that are scarier than you!")
        return pIns

def retortoptions():
    print("Choose a retort:")
    time.sleep(0.75)
    print("1) Yeah - I'm amazed you've lasted this long.")
    time.sleep(0.75)
    print("2) Well, everyone loves a good joke.")
    time.sleep(0.75)
    print("3) Glad to hear you stay in touch with your parents.")
    pRet = int(input())
    if pRet == 1:
        print("You: Yeah, I'm amazed you've made it this far.")
        return pRet
    elif pRet == 2:
        print("You: Well, everyone loves a good joke.")
        return pRet
    elif pRet == 3:
        print("You: Glad to hear you stay in touch with your parents.")
        return pRet

#func/player_retort_controls
def playerretort(b, c):
    if b == c:
        botfail()
        return 0
        
    else:
        playerfail()
        return 1

#func/fail
def playerfail():
    pfaillist = ["Enemy Pirate: You're no good at this!", "Enemy Pirate: You call that an insult?", "Enemy Pirate: Let's hope yer not as bad with a sword as you are with words!",
    "Enemy Pirate: Yer no match for me!"]
    print(random.choice(pfaillist))

def playerloss():
        plosslist = ["Scram, you pirate wannabe!", "Yer not worth my time!", "Come back when you can put up a real fight!"]
        print(random.choice(plosslist))

def botfail():
    botfaillist = ["Enemy Pirate: That's so mean!", "Enemy Pirate: Oh! My feelings!", "Enemy Pirate: Shiver me Timbers!",
     "Enemy Pirate: *muffled crying*", "Enemy Pirate: How could you say that?"]
    print(random.choice(botfaillist))

def botloss():
    botlosslist = ["Enemy Pirate: I yield! I yield! No more insults!", "Enemy Pirate: I've never been so insulted!",
    "Enemy Pirate: Methinks I need t' go cry in a corner now..."]
    print(random.choice(botlosslist))

#func/bot_controls
def botretort(a):
    bresp = random.randint(0, 1)
    if bresp == 1:
        if a == 1:
            print("Enemy Pirate: Yeah - I'm amazed you've lasted this long.")
            return 1
        elif a == 2:
            print("Enemy Pirate: Well, everyone loves a good joke.")
            return 1
        elif a == 3:
            print("Enemy Pirate: Glad to hear you still keep up with your parents.")
            return 1
    elif bresp == 0:
        botfail()
        return 0

def botinsult():
    bins = random.randint(1, 3)
    if bins == 1:
        print("Enemy Pirate: My swordplay will amaze you!")
        return bins
    elif bins == 2:
        print("Enemy Pirate: My deeds are spoken of worldwide!")
        return bins
    elif bins == 3:
        print("Enemy Pirate: I've met pigs that are scarier than you!")
        return bins

#func/round_controls
def offround():
    global phealth
    global bhealth
    time.sleep(1.5)
    inschoice = insultoptions()
    time.sleep(1)
    failCheck = botretort(inschoice)
    if failCheck == 1:
        phealth = phealth - 1
    elif failCheck == 0:
        bhealth = bhealth - 1
    losscheck()

def defround():
    global phealth
    global bhealth
    time.sleep(1.5)
    insbot = botinsult()
    time.sleep(1.5)
    playret = retortoptions()
    failCheck = playerretort(playret, insbot)
    if failCheck == 1:
        phealth = phealth - 1
    elif failCheck == 0:
        bhealth = bhealth - 1
    losscheck()

#func/game_loss
def losscheck():
    if phealth == 0:
        print(playerfail())
        print("You've lost this bout!")
        quit()
    elif bhealth == 0:
        print(botloss())
        print("You've won this bout!")
        quit()

#main
runtime()