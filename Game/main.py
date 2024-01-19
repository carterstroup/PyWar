#import necessary modules
import random
import time
from termcolor import colored
import os, sys
from classes import Computer, Player, Ship, Tank, Plane

#configure the termcolor module for the appropriate device
if sys.platform == "win32":
    os.system('color')

#Game Initialization: Welcome, ask their name, say hello
def welcome():
    print(colored("Welcome To PyWar!", "red"))
    print("To Begin, What Is Your Name?")
    name = input().strip()
    print("Hello, " + name)
    time.sleep(1.2)

#Prints information about the weapons choices.
def print_weapon_info():
    print(colored("Now It Is Time To Choose Your Weapon! Here Are Your Choices:", "yellow"))
    time.sleep(1.2)
    print("(1) Battleship: 75 Health, 25 Attack Damage, 45 Damage Target Strikes (50% chance you miss!)")
    time.sleep(0.6)
    print("(2) Fighter Plane: 50 Health, Refueling Ability (Adds 20 Health), 35 Attack Damage")
    time.sleep(0.6)
    print("(3) Tank: 100 Health, 20 Attack Damage, 35 Damage Mega Shot (Skips Your Next Turn)")

#Insures input is a valid option. Will continue to ask for input until a valid option is provided.
def validate_input_and_convert(passed_selection):
    selection = passed_selection
    while True:   
        if selection == "1":
            return "Ship"
        elif selection == "2":
            return "Plane"
        elif selection == "3":
            return "Tank"
        else:
            print("Please Enter A Number Between 1 And 3.")
            selection = input().strip()
            
#Checks init function from above and associates the returned value with a class instance         
def string_to_object(passed_selection):
    if passed_selection == "Tank":
        return Tank()
    elif passed_selection == "Plane":
        return Plane()
    elif passed_selection == "Ship":
        return Ship()

#Gets the user input for the weapon choice then initiates the player class with the weapon class.
def select_weapon():
    print_weapon_info()
    
    #get input for selection
    weapon_selection = input().strip()
    
    #validates the input
    validated_selection = validate_input_and_convert(weapon_selection)
    
    #converts the input to weapon object
    weapon = string_to_object(validated_selection)
    
    #confirms the player's choice
    print(colored("You Have Selected {choice}! Great Choice!".format(choice=weapon), "green"))
    time.sleep(1.2)
    
    #Establish Player Class
    player = Player(weapon)

    return player

#This function outputs a string of the computer's random selection.
def computerSelection(player):
    computer = ""
    list_of_options = ["Ship", "Plane", "Tank"]
    
    #Remove what the player chose to avoid duplicate weapons.
    index_to_remove = list_of_options.index(str(player.weapon))
    list_of_options.pop(index_to_remove)
    
    #Use radom number to decide weapon.
    rand_num = random.randint(1, 2)
    if rand_num == 1:
        computer = list_of_options[0]
    elif rand_num == 2:
        computer = list_of_options[1]
    return computer

#Uses random numbers to select the weapon for the computer.
def computer_weapon_selection(player):
    print("Now The Computer Will Choose Its Weapon")
    
    #Gets the computer string selection
    computer_choice = computerSelection(player)
    
    #Converts the string to an object
    computer_object = string_to_object(computer_choice)
    time.sleep(1.2)
    print(colored("The Computer Has Chosen {choice}".format(choice=computer_object), "red"))
    time.sleep(2)
    
    #Create the computer class.
    computer = Computer(computer_object)
    return computer

#Prints points for both players
def get_points(player, computer):
    print(colored("Your Points: " + str(player.health), "yellow"))
    print("Computer Points: " + str(computer.health))
    time.sleep(1.2)

#Should the turn be skipped.
def player_skip(player):
    if player.weapon.skip == True:
        print(colored("Your Turn Was Skipped Because Of Your Mega Shot", "red"))
        player.weapon.skip = False
        time.sleep(2.1)
        return True
    else:
        return False

#Calls the function appropriate to the input. Will keep asking until a valid input is received.
def validate_attack_options(player_input, player, computer):
    choice = player_input
    while True:   
        if choice == "1":
            player.weapon.function1(player, computer)
            break
        elif choice == "2":
            player.weapon.function2(player, computer)
            break
        else:
            print("Please Enter 1 or 2")
            choice = input().strip()  

#Gets the user to choose their attack move.
def choose_attack(player, computer):
    #prints options for selected weapon then gives input option
    print(colored("Please Choose Your Move:", "blue"))
    print(player.weapon.attackInfo)
    nextMove = input().strip()
    
    #Validates the choice and calls the appropriate function.
    validate_attack_options(nextMove, player, computer)
    
#Determines if the computer's turn needs to be skipped.    
def computer_skip(computer):
    if computer.weapon.skip == True:
        print(colored("The Computer's Turn Was Skipped Because Of Its Mega Shot", "red"))
        computer.weapon.skip = False
        time.sleep(2.1)
        return True
    else:
        return False

#Gets the computer's attack option.
def computer_attack(player, computer):
    time.sleep(1.2)
    print("Now It Is The Computer's Turn!")
    time.sleep(1.2)
    
    if computer_skip(computer) == False:
        compRandChoice = random.randint(1,2)
        if compRandChoice == 1:
            computer.weapon.function1(player, computer)
        elif compRandChoice == 2:
            computer.weapon.function2(player, computer)

#Sees if either party has won, if so it prints the result and ends the program.            
def check_for_win(player, computer):
    if computer.health <= 0:
        time.sleep(1.2)
        print(colored("You Win!", "green"))
    elif player.health <= 0:
        time.sleep(1.2)
        print(colored("You Lose! Computer Wins!", "red"))

#Manages the function calls for the main game.
def gameplay(player, computer):
    print("Let The Battle Begin!")
    
    #Loops as long as both players have health.
    while player.health > 0 and computer.health > 0:
        
        #prints points of both players
        get_points(player, computer)
        
        #Prompts the user to choose their attack.
        if player_skip(player) == False:
            choose_attack(player, computer)
        
        #Checks if the player has won.    
        if computer.health <= 0:
            break
        
        #Runs the computer attack.
        computer_attack(player, computer)    

    #Checks for the winner
    check_for_win(player, computer)  

#Manages function calls for the whole program.        
def game_init():
    #Welcome the player
    welcome()
    
    #Holds the player object
    player = select_weapon()
    
    #Holds the computer object
    computer = computer_weapon_selection(player)
    
    #Starts the main gameplay.
    gameplay(player, computer)

#Starts the program
game_init()