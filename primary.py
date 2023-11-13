#import neccessary modules
import random
import time
from termcolor import colored
import os

#configure the termcolor module for the appropriate device
os.system('color')

#class definitions
class Ship:
    def __init__(self):
        #define starting health, skip function (primarily for tank class), and weapon information
        self.health = 75
        self.skip = False
        self.attackInfo = "(1) Standard Shot: 25 Damage \n(2) Target Strike: 45 Damage (50% chance you miss!)"
    
    #This is for the 25 damage shot. It reads which user is utilizing the class and deducts the appropriate amount  .  
    def function1(self):
        if self == computerChoice:
            playerChoice.health -= 25
        elif self == playerChoice:
            computerChoice.health -= 25
        else: 
            print("An error has occured.")
        time.sleep(1.2)
        print("A standard shot has been fired!")
    
    #This is for the 45 Damage shot with a 50% chance of missing. Similarly, it reads which entity should be deducted and
    #uses random to determine the hit or miss
    def function2(self):
        getRandInt = random.randint(1,2)
        if getRandInt == 1:
            if self == computerChoice:
                playerChoice.health -= 45
            elif self == playerChoice:
                computerChoice.health -= 45
            else: 
                print("An error has occured.")
            time.sleep(1.2)
            print("Mega Shot Succesful!")
        elif getRandInt == 2:
            time.sleep(1.2)
            print("Mega Shot Failed!")
        else:
            print("An error has occured")
    
    #represent the class for string purposes
    def __repr__(self):
        return "Ship"
    
#all other classes follow similar structure unless otherwise noted
class Plane:
    def __init__(self):
        self.health = 50
        self.skip = False
        self.attackInfo = "(1) Refuel: adds 20 health \n(2) Air Strike: 35 damage."
     
    #unlike other functions, this adds health instead of deducting it. It follows a similar syntax    
    def function1(self):
        if self == computerChoice:
            computerChoice.health += 20
        elif self == playerChoice:
            playerChoice.health += 20
        else: 
            print("An error has occured.")
        time.sleep(1.2)
        print(colored("Refuel Succesful", "green"))
    
    #this removes 35 health
    def function2(self):
        if self == computerChoice:
            playerChoice.health -= 35
        elif self == playerChoice:
            computerChoice.health -= 35
        else: 
            print("An error has occured.")
        time.sleep(1.2)
        print(colored("Air Strike Succesful", "green"))
    
    #for string purposes
    def __repr__(self):
        return "Plane"
    
class Tank:
    def __init__(self):
        self.health = 100
        self.skip = False
        self.attackInfo = "(1) Standard Shot: 20 damage \n(2) Mega Shot: 35 damage, but skips your next turn"
    
    #deducts 20 health, the tank functions also check for the skip attribute as a mega shot requires that the next turn be skipped    
    def function1(self):
        if self.skip == False:
            if self == computerChoice:
                playerChoice.health -= 20
            elif self == playerChoice:
                computerChoice.health -= 20
            else: 
                print("An error has occured.")
            time.sleep(1.2)
            print(colored("Standard Shot fired!", "green"))
        elif self.skip == True:
            time.sleep(1)
            print(colored("Your turn was skipped because of your Mega Shot", "red"))
            self.skip = False
    
    #when used, this function require the next turn to be skipped, the function is adjusted accordingly with if statement checks
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
            time.sleep(1.2)
            print(colored("Mega Shot Successful! Your next turn will be skipped", "green"))
        elif self.skip == True:
            self.skip = False
            time.sleep(1.2)
            print("Your turn was skipped because of your Mega Shot")
        else:
            print("An error has occured")
    
    #for strings
    def __repr__(self):
        return "Tank"

#global variable declerations for inputs and class instances appropriately
selection = ""
playerChoice = None
computerChoice = None

#this function operates the computer weapon selection process. Takes in 'choice' which is the input string
def computerSelection(choice):
    #create random number to pick between two remaining weapon types
    randNum = random.randint(1, 2)
    theChoice = "" #inner variable to return
    #iterates through options based on the user's weapon selection
    if choice == "3":
        if randNum == 1:
            theChoice = "Ship"
        elif randNum == 2:
            theChoice = "Plane"
        else:
            print("An error has occured1")
    elif choice == "1":
        if randNum == 1:
            theChoice = "Tank"
        elif randNum == 2:
            theChoice = "Plane"
        else:
            print("An error has occured2")
    elif choice == "2":
        if randNum == 1:
            theChoice = "Ship"
        elif randNum == 2:
            theChoice = "Tank"
        else:
            print("An error has occured3")
    else:
        print("An error has occured4")
    return theChoice

#function for creating an instance for the user weapon based on their input
def initSelection(choice):
    theChoice = ""
    if choice == "1":
        theChoice = "Ship"
    elif choice == "2":
        theChoice = "Plane"
    elif choice == "3":
        theChoice = "Tank"
    else: 
        print("Something went wrong.")
    return theChoice

#Game Initilization: Welcome, ask their name, say hello
print(colored("Welcome to PyWar!", "red"))
print("To begin, what is your name?")
name = input().strip()
print("Hello, " + name)
time.sleep(1.2)

#Choose Weapon: offer information about each weapon 
print(colored("Now it is time to choose your weapon! Here are your choices:", "yellow"))
time.sleep(1.2)
print("(1) Battleship: 75 Health, 25 Damage Attack, 45 Damage Target Strikes (50% chance you miss!)")
time.sleep(0.6)
print("(2) Fighter Plane: 50 Health, Refueling Ability (Adds 20 Health), 35 Damage Attack.")
time.sleep(0.6)
print("(3) Tank: 100 Health, 20 Damage Attack, 35 Damage Mega Shot (skips your next turn)")

#get input for selection
selection = input().strip()

#check to make sure the input matches an option, if it doesn't, it will keep asking until it does
while True:   
    if selection == "1":
        break
    elif selection == "2":
        break
    elif selection == "3":
        break
    else:
        print("Enter a number 1-3.")
        selection = input().strip()
        
#checks init function from above and associates the returned value with a class instance
if initSelection(selection) == "Tank":
    playerChoice = Tank()
elif initSelection(selection) == "Plane":
    playerChoice = Plane()
elif initSelection(selection) == "Ship":
    playerChoice = Ship()
    print("Not an error here")
else:
    print("An error has occured.7")

#confirm choice and announce the computer is selecting
print(colored("You have selected {choice}! Great choice!".format(choice=playerChoice), "green"))
time.sleep(1.2)
print("Now the computer will choose its weapon.")

#iterate through computer selection choices from above function then announces their weapon and battle start
if computerSelection(selection) == "Tank":
    computerChoice = Tank()
elif computerSelection(selection) == "Plane":
    computerChoice = Plane()
elif computerSelection(selection) == "Ship":
    computerChoice = Ship()
else:
    print("An error has occured.")
time.sleep(1.2)
print(colored("The Computer has chosen {choice}".format(choice=computerChoice), "red"))
time.sleep(1.2)
print("Let the battle begin!")

#Actual game loop
while playerChoice.health > 0 and computerChoice.health > 0:
    #prints points
    print(colored("Your Points: " + str(playerChoice.health), "yellow"))
    print("Computer Points: " + str(computerChoice.health))
    time.sleep(1.2)
    
    #checks if the turn should be skipped because of a Tank class option
    if playerChoice.skip == True:
        print(colored("Your turn was skipped because of your Mega Shot", "red"))
        playerChoice.skip = False
    else:
        #prints options for selected weapon then gives input option
        print(colored("Please choose your move:", "blue"))
        print(playerChoice.attackInfo)
        nextMove = input().strip()

        #checks to make sure the input is a valid selection
        while True:   
            if nextMove == "1":
                break
            elif nextMove == "2":
                break
            else:
                print("Enter a number 1-2.")
                nextMove = input().strip()
        
        #associates the input with the appropriate class function    
        if nextMove == "1":
            playerChoice.function1()
        elif nextMove == "2":
            playerChoice.function2()
        else:
            print("An error has occured.")
        
        #checks to see if the computer has no health, at which point the game ends    
        if computerChoice.health <= 0:
            break
        
    #accounces computer's turn
    time.sleep(1.2)
    print("Now it is the computer's turn!")
    time.sleep(1.2)
    
    #uses random number to choose the computer's action
    compRandChoice = random.randint(1,2)
    
    #checks to see if the turn should be skipped accoridng to Tank class function
    if computerChoice.skip == True:
        print(colored("The Computer's turn was skipped because of your Mega Shot", "red"))
        computerChoice.skip = False
    else:
    #executes function based on randum number
        if compRandChoice == 1:
            computerChoice.function1()
        elif compRandChoice == 2:
            computerChoice.function2()
        else:
            print("An error has occured")

#checks to see if either instance is out of health, at which point the game ends, if one has won, it announces it and ends the program        
if computerChoice.health <= 0:
    time.sleep(1.2)
    print(colored("You Win!", "green"))
elif playerChoice.health <= 0:
    time.sleep(1.2)
    print(colored("You lose! Computer Wins!", "red"))
else:
    print("An error has occured")