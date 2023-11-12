import random

class Ship:
    def __init__(self):
        self.health = 75
        self.standardShot = 25
        self.targetedMissile = 45
        self.selected = False
        
    def StandardShot(self):
        pass
    
    def TargetedMissile(self):
        pass
    
    def __repr__(self):
        return "Ship"
    
    
class Plane:
    def __init__(self):
        self.health = 50
        self.refHealth = 20
        self.attack = 35
        self.selected = False
        
    def refuel(self):
        pass
    
    def attack(self):
        pass
    
    def __repr__(self):
        return "Plane"
    
class Tank:
    def __init__(self):
        self.health = 100
        self.stdShot = 20
        self.pwrShot = 45
        self.selected = False
        
    def takeShot(self):
        pass
    
    def bigShot(self):
        pass
    
    def __repr__(self):
        return "Tank"

selection = ""
playerChoice = None
computerChoice = None

def computerSelection(choice):
    randNum = random.randint(1, 2)
    theChoice = ""
    if choice == "Tank":
        if randNum == 1:
            theChoice = "Ship"
        elif randNum == 2:
            theChoice = "Plane"
        else:
            print("An error has occured")
    elif choice == "Ship":
        if randNum == 1:
            theChoice = "Tank"
        elif randNum == 2:
            theChoice = "Plane"
        else:
            print("An error has occured")
    elif choice == "Plane":
        if randNum == 1:
            theChoice = "Ship"
        elif randNum == 2:
            theChoice = "Tank"
        else:
            print("An error has occured")
    else:
        print("An error has occured")
    return theChoice

def initSelection(choice):
    theChoice = ""
    if choice == "Tank":
        theChoice = "Tank"
    elif choice == "Plane":
        theChoice = "Plane"
    elif choice == "Ship":
        theChoice = "Ship"
    else: 
        print("Please choose on of the three options and try again.")
        selection = input()    
        
    return theChoice
    
    
#Game Initilization 
print("Welcome to PyWar!")
print("To begin, what is your name?")
name = input()
print("Hello, " + name)

#Choose Weapon
print("Now it is time to choose your weapon! Here are your choices:")
print("Battleship: 75 Health, 25 Damage Standard Shot, 45 Damage on Target Strikes but there is a 50% chance you miss! To choose the Battleship, enter 'Ship'")
print("Fighter Plane: 50 Health, Refueling Ability which adds 20 health, and an attack that does 35 damage. Enter 'Plane' to choose the Fighter Plane.")
print("Tank: 100 Health, Standard Shot does 20 damage, Mega Shot does 45 damage, but skips your next turn")
selection = input()

if initSelection(selection) == "Tank":
    playerChoice = Tank()
elif initSelection(selection) == "Plane":
    playerChoice = Plane()
elif initSelection(selection) == "Ship":
    playerChoice = Ship()
else:
    print("An error has occured.")

print("You have selected {choice}! Great choice!".format(choice=playerChoice))
print("Now the computer will choose its weapon.")

if computerSelection(selection) == "Tank":
    computerChoice = Tank()
elif computerSelection(selection) == "Plane":
    computerChoice = Plane()
elif computerSelection(selection) == "Ship":
    computerChoice = Ship()
else:
    print("An error has occured.")

print("The Computer has chosen {choice}".format(choice=computerChoice))
print("Let the battle begin!")
