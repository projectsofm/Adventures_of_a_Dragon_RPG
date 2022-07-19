import sys
import os
import time
import random
import pickle
import socket

weapons = {"Great Sword": 40}

class Player:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.base_attack = 5
        self.gold = 1
        self.potions = 1
        self.weapons = ["Rusty Sword"]
        self.currweapon = ["Rusty Sword"]
    
    @property
    def attack(self):
        attack = self.base_attack
        if self.currweapon == "Rusty Sword":
            attack == 5
            
        if self.currweapon == "Great Sword":
            attack == 15
            
        return attack
        
class Goblin:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 50
        self.health = self.maxhealth
        self.attack = 5
        self.goldgain = 10
Goblin1=Goblin("Goblin")

class Zombie:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 70
        self.health = self.maxhealth
        self.attack = 7
        self.goldgain = 15
Zombie1=Zombie("Zombie")

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
        if os.path.exists("Save File") == True:
            os.system('cls')
            with open("Save File", "rb") as f:
                global Player1
                Player1 = pickle.load(f)
            print("Loaded!")
            option = input(' ')
            start1()
        else:
            print("There is no save file")
            option = input(' ')
            main()
    elif option == "3":
        sys.exit()
    else:
        print("Hey! That's not an option!")
        time.sleep(2)
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
    print("Name: %s" % Player1.name)
    print("Attack: %i" % Player1.attack)
    print("Health: %i/%i" % (Player1.health, Player1.maxhealth))
    print("Weapon: %s" % Player1.currweapon)
    print("Gold: %i" % Player1.gold)
    print("Potions: %i" % Player1.potions)
    print("1) Fight")
    print("2) Store")
    print("3) Save")
    print("4) Exit")
    print("5) Inventory")
    print("6) Local Multiplayer")
    option = input("> ")
    
    if option == "1":
        prefight()
    elif option == "2":
        store()
    elif option == "3":
        os.system('cls')
        with open("Save File", "wb") as f:
            pickle.dump(Player1, f)
            print("\n...Game saved!\n")
        option = input(' ')
        start()
    elif option == "4":
        sys.exit()
    elif option == "5":
        inventory()
    elif option == "6":
        MP_Main()
    else:
        start1()
        
def inventory():
    os.system('cls')
    print("What want?")
    print("1) Equip weapon")
    print("2) Back")
    option = input("> ")
    if option == 1:
        equip()
    elif option == 2:
        start1()
        
def equip():
    os.system('cls')
    print("What equip?")
    for weapon in Player1.weapons:
        print(weapon)
    print("b to go back")
    option = input("> ")
    if option == Player1.currweapon:
        print("already euiped!")
        option = input(' ')
        equip()
    elif option == "b":
        inventory()
    elif option in Player1.weapons:
        Player1.currweapon = option
        print("Success you equip %s" % option)
        equip()
    else:
        print("You dont have a %s!" % option)
        
def prefight():
    os.system('cls')
    global enemy
    enemynum = random.randint(1,2)
    if enemynum == 1:
        enemy = Goblin1
    else:
        enemy = Zombie1
    fight()

def fight():
    os.system('cls')
    print("%s   vs   %s" % (Player1.name, enemy.name))
    print("%s's Health: %d/%d   %s's Health: %i/%i" % (Player1.name, Player1.health, Player1.maxhealth, enemy.name, enemy.health, enemy.maxhealth))
    print("Potions: %i\n" % Player1.potions)
    print("1) Attack")
    print("2) Drink Potion")
    print("3) Run")
    option = input("> ")
    if option == "1":
        attack()
    elif option == "2":
        drinkpotion()
    elif option == "3":
        run()
    else:
        fight()
        
def attack():
    os.system('cls')
    PAttack = random.randint(Player1.attack/2, Player1.attack)
    EAttack = random.randint(enemy.attack/2, enemy.attack)
    if PAttack == Player1.attack/2:
        print("You miss!")
    else:
        enemy.health -= PAttack
        print("You deal %i damage" % PAttack)
    option = input(' ')
    if enemy.health <= 0:
        win()
    os.system('cls')
    if EAttack == enemy.attack/2:
        print("Enemy missed!")
    else:
        Player1.health -= enemy.attack
        print("Enemy deals %i damage!" % EAttack)
    option = input(' ')
    if Player1.health <= 0:
        lose()
    else:
        fight()

def drinkpotion():
    os.system('cls')
    if Player1.potions == 0:
        print("You don't have any potions!")
    else:
        Player1.health += 50
        if Player1.health > Player1.maxhealth:
            Player1.health = Player1.maxhealth
        print("You drank a potion!")
    option = input(' ')
    fight()
    
def run():    
    runnum = random.ranint(1, 3)
    if runnum == 1:
        print("You have ran away")
        option = input(' ')
        start1()
    else:
        print("You failed to run away!")
        option = input(' ')
        os.system('cls')
        EAttack = random.randint(enemy.attack/2, enemy.attack)
        if EAttack == enemy.attack/2:
            print("Enemy missed!")
        else:
            Player1.health -= enemy.attack
            print("Enemy deals %i damage!" % EAttack)
        option = input(' ')
        if Player1.health <= 0:
            lose()
        else:
            fight()

        

def win():
    os.system('cls')
    enemy.health = enemy.maxhealth
    Player1.gold += enemy.goldgain
    print("You have defeated %s" % enemy.name)
    print("You found %s" % enemy.goldgain)
    option = input(' ')
    start1()

def lose():
    os.system('cls')
    print("You have died!")
    option = input(' ')
    
def store():
    os.system('cls')
    print("Welcome to store")
    print("\nWhat buy?\n")
    print("1) Great Sword")
    print("Back")
    print(" ")
    option = input(' ')
    
    if option in weapons:
        if Player1.gold >= weapons[option]:
            os.system('cls')
            Player1.gold -= weapons[option]
            Player1.weapons.append(option)
            print("Congrats on new purchase %s" % option)
            option = input(' ')
            store()
        else:
            os.system('cls')
            print("Too poor..")
            option = input(' ')
            store()
    elif option == "Back":
        start1()
    else:
        os.system('cls')
        print("That item doesn't exist")
        option = input(' ')
        store()
            
def MP_Format(name, health):
    print("%s   vs   %s" % (Player1.name, name))
    print("%s Health: %i" % (Player1.name, Player1.health))
    print("%s Health: %i" % (name, health))
    print("1) Attack")
    mpinput = input("> ")
    if mpinput != "1":
        MP_Format(name, health)
    else: 
        return mpinput


def MP_Main():
    host = input("Please enter IP address: ")
    port = input("Please enter room number: ")
    s = socket.socket()
    s.connect((host, port))
    print("Waiting for other player...")
    PlayerObj = pickle.dumps(Player1)
    s.send(PlayerObj)
    Enemy = s.recv(1024)
    Enemy = pickle.loads(Enemy)
    
    while True: 
        mpinput = MP_Format(Enemy.name, Enemy.health)
        s.send(mpinput.encode())
        print("Waiting for other player to respond..")
        Damage = s.recv(1024)
        Damage = pickle.loads(Damage)
        Damage_Dealt(Player1.health - Damage[0], Enemy.health - Damage[1], Enemy.name)
        Player1.health = Damage[0]
        Enemy.health = Damage[1]
        if Damage[2] != 0:
            if Damage[2] == 1:
                mpwin(Enemy.name, s)
            elif Damage[2] == 2:
                mplose(Enemy.name, s)
    
def Damage_Dealt(x, y, name):
    print("You take %i damage!" % x)
    print("You deal %i damage to %s!" % (y, name))
    option = input("> ")
    
def mpwin(name, s):
    print("You have defeated %s" % name)
    option = input(' ')
    s.close
    start1()
    
def mplose(name, s):
    print("You have lost to %s" % name)
    option = input(' ')
    s.close
    start1()
    
if __name__ == "__main__":
    main()