import sys
import os

class Player:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.attack = 5
        
def main():
    os.system('cls')
    print("Adventures of a Dragon\n")
    print("1) Start")
    print("2) Load")
    print("3) Exit")
    option = input("> ")
    if option == "1": 
        start()
    elif option == "2": 
        pass
    elif option == "3":
        sys.exit()
    else:
        print("..Hey! That's not an option!\n")
        main()
        
def start():
    os.system('cls')
    print("So the game begins...You are a dragon, and your name is..")
    option = input("> ")
    global Player1
    Player1 = Player(option)
    start1()

def start1():
    os.system('cls')
    print("Welcome, %s." % Player1.name)
    
main()
