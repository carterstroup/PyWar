#import necessary modules
import random
import time
from termcolor import colored
import os, sys

#configure the termcolor module for the appropriate device
if sys.platform == "win32":
    os.system('color')
        
class Computer:
    def __init__(self, weapon):
        self.weapon = weapon
        self.health = weapon.get_health()
        
    def __repr__(self):
        return self.weapon

class Player:
    def __init__(self, weapon):
        self.weapon = weapon
        self.health = weapon.get_health()
        
    def __repr__(self):
        return self.weapon
        
class Ship:
    def __init__(self):
        #define starting health, skip function (primarily for tank class), and weapon information
        self.health = 75
        self.skip = False
        self.attackInfo = "(1) Standard Shot: 25 Damage \n(2) Target Strike: 45 Damage (50% Chance You Miss!)"
    
    def get_health(self):
        return self.health
    
    #This is for the 25 damage shot. It reads which user is utilizing the class and deducts the appropriate amount  .  
    def function1(self, player, computer):
        if self == computer.weapon:
            player.health -= 25
        elif self == player.weapon:
            computer.health -= 25
        time.sleep(1.2)
        print(colored("Shots Fired! 25 Damage!", "green"))
    
    #This is for the 45 Damage shot with a 50% chance of missing. Similarly, it reads which entity should be deducted and
    #uses random to determine the hit or miss
    def function2(self, player, computer):
        getRandInt = random.randint(1,2)
        if getRandInt == 1:
            if self == computer.weapon:
                player.health -= 45
            elif self == player.weapon:
                computer.health -= 45
            time.sleep(1.2)
            print(colored("Target Strike Successful!", "green"))
        elif getRandInt == 2:
            time.sleep(1.2)
            print(colored("Target Strike Failed!", "red"))
    
    #represent the class for string purposes
    def __repr__(self):
        return "Ship"
    
#all other classes follow similar structure unless otherwise noted
class Plane:
    def __init__(self):
        self.health = 50
        self.skip = False
        self.attackInfo = "(1) Refuel: Adds 20 Health \n(2) Air Strike: 35 Damage."
        
    def get_health(self):
        return self.health
    
    #unlike other functions, this adds health instead of deducting it. It follows a similar syntax    
    def function1(self, player, computer):
        if self == computer.weapon:
            computer.health += 20
        elif self == player.weapon:
            player.health += 20
        time.sleep(1.2)
        print(colored("Refuel Successful", "green"))
    
    #this removes 35 health
    def function2(self, player, computer):
        if self == computer.weapon:
            player.health -= 35
        elif self == player.weapon:
            computer.health -= 35
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
    
    def get_health(self):
        return self.health
    
    #deducts 20 health, the tank functions also check for the skip attribute as a mega shot requires that the next turn be skipped    
    def function1(self, player, computer):
        if self.skip == False:
            if self == computer.weapon:
                player.health -= 20
            elif self == player.weapon:
                computer.health -= 20
            time.sleep(1.2)
            print(colored("Standard Shot Fired!", "green"))
        elif self.skip == True:
            time.sleep(1)
            print(colored("Your Turn Was Skipped Because Of Your Mega Shot", "red"))
            self.skip = False
    
    #when used, this function require the next turn to be skipped, the function is adjusted accordingly with if statement checks
    def function2(self, player, computer):
        if self.skip == False:
            if self == computer.weapon:
                player.health -= 35
                self.skip = True
            elif self == player.weapon:
                computer.health -= 35
                self.skip = True
            time.sleep(1.2)
            print(colored("Mega Shot Successful! Your Next Turn Will Be Skipped", "green"))
        elif self.skip == True:
            self.skip = False
            time.sleep(1.2)
            print("Your Turn Was Skipped Because Of Your Mega Shot")
    
    #for strings
    def __repr__(self):
        return "Tank"