import random

class Ship:
    def __init__(self):
        self.health = 75
        self.standardShot = 25
        self.targetedMissile = 45
        self.selected = False
        self.skip = False
        self.attackInfo = "(1) Standard Shot: 25 Damage \n(2) Target Strikes: 45 Damage but there is a 50% chance you miss!"
        
    def function1(self):
        if self == computerChoice:
            playerChoice.health -= 25
        elif self == playerChoice:
            computerChoice.health -= 25
        else: 
            print("An error has occured.")
        print("A standard shot has been fired!")
    
    def function2(self):
        getRandInt = random.randint(1,2)
        if getRandInt == 1:
            if self == computerChoice:
                playerChoice.health -= 45
            elif self == playerChoice:
                computerChoice.health -= 45
            else: 
                print("An error has occured.")
            print("Mega Shot Succesful!")
        elif getRandInt == 2:
            print("Mega Shot Failed!")
        else:
            print("An error has occured")
    
    def __repr__(self):
        return "Ship"
    
    
class Plane:
    def __init__(self):
        self.health = 50
        self.refHealth = 20
        self.attack = 35
        self.selected = False
        self.skip = False
        self.attackInfo = "(1) Refuel: adds 20 health \n(2) Air Strike: 35 damage."
        
    def function1(self):
        if self == computerChoice:
            computerChoice.health += 20
        elif self == playerChoice:
            playerChoice.health += 20
        else: 
            print("An error has occured.")
        print("Refuel Succesful")
    
    def function2(self):
        if self == computerChoice:
            playerChoice.health -= 35
        elif self == playerChoice:
            computerChoice.health -= 35
        else: 
            print("An error has occured.")
        print("Air Strike Succesful")
    
    def __repr__(self):
        return "Plane"
    
class Tank:
    def __init__(self):
        self.health = 100
        self.stdShot = 20
        self.pwrShot = 45
        self.selected = False
        self.skip = False
        self.attackInfo = "(1) Standard Shot: 20 damage \n(2) Mega Shot: 35 damage, but skips your next turn"
        
    def function1(self):
        if self.skip == False:
            if self == computerChoice:
                playerChoice.health -= 20
            elif self == playerChoice:
                computerChoice.health -= 20
            else: 
                print("An error has occured.")
            print("Standard Shot fired!")
        elif self.skip == True:
            print("Your turn was skipped because of your Mega Shot")
            self.skip = False
    
    def function2(self):
        if self.skip == False:
            if self == computerChoice:
                playerChoice.health -= 35
                self.skip = True
            elif self == playerChoice:
                computerChoice.health -= 35
                self.skip = True
            else: 
                print("An error has occured.")
            print("Mega Shot Successful! Your next turn will be skipped")
        elif self.skip == True:
            self.skip = False
            print("Your turn was skipped because of your Mega Shot")
        else:
            print("An error has occured")
    
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
print("Tank: 100 Health, Standard Shot does 20 damage, Mega Shot does 35 damage, but skips your next turn")
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

while playerChoice.health > 0 and computerChoice.health > 0:
    print("Your Points: " + str(playerChoice.health))
    print("Computer Points: " + str(computerChoice.health))
    print("Please choose your move:")
    print(playerChoice.attackInfo)
    nextMove = input()
    if nextMove == "1":
        playerChoice.function1()
    elif nextMove == "2":
        playerChoice.function2()
    else:
        print("An error has occured.")
        
    print("Now it is the computer's turn!")
    
    compRandChoice = random.randint(1,2)
    
    if compRandChoice == 1:
        computerChoice.function1()
    elif compRandChoice == 2:
        computerChoice.function2()
    else:
        print("An error has occured")
        
if computerChoice.health <= 0:
    print("You Win!")
elif playerChoice.health <= 0:
    print("You lose! Computer Wins!")
else:
    print("An error has occured")