#import necessary modules
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
        self.attackInfo = "(1) Standard Shot: 25 Damage \n(2) Target Strike: 45 Damage (50% Chance You Miss!)"
    
    #This is for the 25 damage shot. It reads which user is utilizing the class and deducts the appropriate amount  .  
    def function1(self):
        if self == computerChoice:
            playerChoice.health -= 25
        elif self == playerChoice:
            computerChoice.health -= 25
        else: 
            print("An error has occurred. Could not identify which entity to deduct health from. Line 25")
        time.sleep(1.2)
        print("Shots Fired! 25 Damage!")
    
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
                print("An error has occurred. Could not identify which entity to deduct health from. Line 39")
            time.sleep(1.2)
            print("Mega Shot Successful!")
        elif getRandInt == 2:
            time.sleep(1.2)
            print("Mega Shot Failed!")
        else:
            print("An error has occurred. Random integer was not properly defined. Line 46")
    
    #represent the class for string purposes
    def __repr__(self):
        return "Ship"
    
#all other classes follow similar structure unless otherwise noted
class Plane:
    def __init__(self):
        self.health = 50
        self.skip = False
        self.attackInfo = "(1) Refuel: Adds 20 Health \n(2) Air Strike: 35 Damage."
     
    #unlike other functions, this adds health instead of deducting it. It follows a similar syntax    
    def function1(self):
        if self == computerChoice:
            computerChoice.health += 20
        elif self == playerChoice:
            playerChoice.health += 20
        else: 
            print("An error has occurred. Could not identify which entity to add health to. Line 66")
        time.sleep(1.2)
        print(colored("Refuel Successful", "green"))
    
    #this removes 35 health
    def function2(self):
        if self == computerChoice:
            playerChoice.health -= 35
        elif self == playerChoice:
            computerChoice.health -= 35
        else: 
            print("An error has occurred. Could not identify which entity to deduct health from. Line 77")
        time.sleep(1.2)
        print(colored("Air Strike Successful", "green"))
    
    #for string purposes
    def __repr__(self):
        return "Plane"
    
class Tank:
    def __init__(self):
        self.health = 100
        self.skip = False
        self.attackInfo = "(1) Standard Shot: 20 Damage \n(2) Mega Shot: 35 Damage, But Skips Your Next Turn"
    
    #deducts 20 health, the tank functions also check for the skip attribute as a mega shot requires that the next turn be skipped    
    def function1(self):
        if self.skip == False:
            if self == computerChoice:
                playerChoice.health -= 20
            elif self == playerChoice:
                computerChoice.health -= 20
            else: 
                print("An error has occurred. Could not identify which entity to deduct health from. Line 99")
            time.sleep(1.2)
            print(colored("Standard Shot Fired!", "green"))
        elif self.skip == True:
            time.sleep(1)
            print(colored("Your Turn Was Skipped Because Of Your Mega Shot", "red"))
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
                print("An error has occurred. Could not identify which entity to deduct health from. Line 117")
            time.sleep(1.2)
            print(colored("Mega Shot Successful! Your Next Turn Will Be Skipped", "green"))
        elif self.skip == True:
            self.skip = False
            time.sleep(1.2)
            print("Your Turn Was Skipped Because Of Your Mega Shot")
        else:
            print("An error has occurred. Skip attribute was not properly configured. Line 125")
    
    #for strings
    def __repr__(self):
        return "Tank"

#global variable declarations for inputs and class instances appropriately
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
            print("An error has occurred. Random number was not properly configured. Line 148")
    elif choice == "1":
        if randNum == 1:
            theChoice = "Tank"
        elif randNum == 2:
            theChoice = "Plane"
        else:
            print("An error has occurred. Random number was not properly configured. Line 155")
    elif choice == "2":
        if randNum == 1:
            theChoice = "Ship"
        elif randNum == 2:
            theChoice = "Tank"
        else:
            print("An error has occurred. Random number was not properly configured. Line 162")
    else:
        print("An error has occurred. Random number was not properly configured. Line 164")
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
        print("An error has occurred. Passed input did not equal valid choice. Line 177")
    return theChoice

#Game Initialization: Welcome, ask their name, say hello
print(colored("Welcome To PyWar!", "red"))
print("To Begin, What Is Your Name?")
name = input().strip()
print("Hello, " + name)
time.sleep(1.2)

#Choose Weapon: offer information about each weapon 
print(colored("Now It Is Time To Choose Your Weapon! Here Are Your Choices:", "yellow"))
time.sleep(1.2)
print("(1) Battleship: 75 Health, 25 Attack Damage, 45 Damage Target Strikes (50% chance you miss!)")
time.sleep(0.6)
print("(2) Fighter Plane: 50 Health, Refueling Ability (Adds 20 Health), 35 Attack Damage")
time.sleep(0.6)
print("(3) Tank: 100 Health, 20 Attack Damage, 35 Damage Mega Shot (Skips Your Next Turn)")

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
        print("Please Enter A Number Between 1 And 3.")
        selection = input().strip()
        
#checks init function from above and associates the returned value with a class instance
if initSelection(selection) == "Tank":
    playerChoice = Tank()
elif initSelection(selection) == "Plane":
    playerChoice = Plane()
elif initSelection(selection) == "Ship":
    playerChoice = Ship()
else:
    print("An error has occurred. Input selection did not match any valid options. Line 219")

#confirm choice and announce the computer is selecting
print(colored("You Have Selected {choice}! Great Choice!".format(choice=playerChoice), "green"))
time.sleep(1.2)
print("Now The Computer Will Choose Its Weapon")

#iterate through computer selection choices from above function then announces their weapon and battle start
if computerSelection(selection) == "Tank":
    computerChoice = Tank()
elif computerSelection(selection) == "Plane":
    computerChoice = Plane()
elif computerSelection(selection) == "Ship":
    computerChoice = Ship()
else:
    print("An error has occurred. Computer selection does not match a valid option. Line 234")
time.sleep(1.2)
print(colored("The Computer Has Chosen {choice}".format(choice=computerChoice), "red"))
time.sleep(2)
print("Let The Battle Begin!")

#Actual game loop
while playerChoice.health > 0 and computerChoice.health > 0:
    #prints points
    print(colored("Your Points: " + str(playerChoice.health), "yellow"))
    print("Computer Points: " + str(computerChoice.health))
    time.sleep(1.2)
    
    #checks if the turn should be skipped because of a Tank class option
    if playerChoice.skip == True:
        print(colored("Your Turn Was Skipped Because Of Your Mega Shot", "red"))
        playerChoice.skip = False
        time.sleep(2.1)
    else:
        #prints options for selected weapon then gives input option
        print(colored("Please Choose Your Move:", "blue"))
        print(playerChoice.attackInfo)
        nextMove = input().strip()

        #checks to make sure the input is a valid selection
        while True:   
            if nextMove == "1":
                break
            elif nextMove == "2":
                break
            else:
                print("Please Enter 1 or 2")
                nextMove = input().strip()
        
        #associates the input with the appropriate class function    
        if nextMove == "1":
            playerChoice.function1()
        elif nextMove == "2":
            playerChoice.function2()
        else:
            print("An error has occurred. Passed input does not match a valid option. Line 274")
        
        #checks to see if the computer has no health, at which point the game ends    
        if computerChoice.health <= 0:
            break
        
    #announces computer's turn
    time.sleep(1.2)
    print("Now It Is The Computer's Turn!")
    time.sleep(1.2)
    
    #uses random number to choose the computer's action
    compRandChoice = random.randint(1,2)
    
    #checks to see if the turn should be skipped accoridng to Tank class function
    if computerChoice.skip == True:
        print(colored("The Computer's Turn Was Skipped Because Of Its Mega Shot", "red"))
        computerChoice.skip = False
    else:
    #executes function based on random number
        if compRandChoice == 1:
            computerChoice.function1()
        elif compRandChoice == 2:
            computerChoice.function2()
        else:
            print("An error has occurred. Passed input does not match a valid option. Line 299")

#checks to see if either instance is out of health, at which point the game ends, if one has won, it announces it and ends the program        
if computerChoice.health <= 0:
    time.sleep(1.2)
    print(colored("You Win!", "green"))
elif playerChoice.health <= 0:
    time.sleep(1.2)
    print(colored("You Lose! Computer Wins!", "red"))
else:
    print("An error has occurred. The game unexpectedly ended. Line 309")