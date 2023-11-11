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
    
    def __attr__(self):
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
    
    def __attr__(self):
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
    
    def __attr__(self):
        return "Tank"

selection = ""
playerChoice = None
computerChoice = None

def computerSelection():
    randNum = random.randint(1, 2)
    if playerChoice == "Tank":
        if randNum == 1:
            computerChoice = Ship()
        elif randNum == 2:
            computerChoice = Plane()
        else:
            print("An error has occured")
    elif playerChoice == "Ship":
        if randNum == 1:
            computerChoice = Tank()
        elif randNum == 2:
            computerChoice = Plane()
        else:
            print("An error has occured")
    elif playerChoice == "Plane":
        if randNum == 1:
            computerChoice = Ship()
        elif randNum == 2:
            computerChoice = Tank()
        else:
            print("An error has occured")
    else:
        print("An error has occured.")

def initSelection(choice):
    if choice == "Tank":
        playerChoice = Tank()
    elif choice == "Plane":
        playerChoice = Plane()
    elif choice == "Ship":
        playerChoice = Ship()
    else: 
        print("Please choose on of the three options and try again.")
        selection = input()    
    
    
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

initSelection(selection)

print("You have selected {choice}! Great choice!".format(choice=selection))
print("Now the computer will choose its weapon.")


