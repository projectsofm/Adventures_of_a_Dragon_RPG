import socket
import random
import pickle
from game import Player

def Battle(x, y):
    global win1
    global win2
    
    if x == "1":
        global dmg1
        dmg1 = random.randint(int(Player1.attack/3), Player1.attack)
        Player2.health -= dmg1
    if y == "1":
        global dmg2
        dmg2 = random.randint(int(Player2.attack/3), Player2.attack)
        Player1.health -= dmg2
        if Player1.health <= 0:
            win2 = 1 
            win1 = 2 
        elif Player2.health <= 0:
            win2 = 2
            win1 = 1

def main():
    host = input("Please re-enter IP address: ")
    port = input("Please re-enter room number: ")
    global win1
    win1 = 0
    global win2
    win2 = 0
    
    s = socket.socket()
    s.bind((host, port))
    
    s.listen(1)
    connection1, address1 = s.accept()
    print("Connection from: " + str(address1))
    s.listen(2)
    connection2, address2 = s.accept()
    print("Connection from: " + str(address2))
    
    data1 = connection1.recv(1024)
    global Player1
    Player1 = pickle.loads(data1)
    data2 = connection2.recv(1024)
    global Player2
    Player2 = pickle.loads(data2)
    connection1.send(data2)
    connection2.send(data1)
    
    while True:
        data1 = connection1.recv(1024)
        data1 = data1.decode()
        data2 = connection2.recv(1024)
        data2 = data2.decode()
        Battle(data1, data2)
        Health1 = Player1.health
        Health2 = Player2.health
        THealth1 = pickle.dumps([Health1, Health2, win1])
        THealth2 = pickle.dumps([Health2, Health1, win2])
        connection1.send(THealth1)
        connection2.send(THealth2)
        
    connection1.close()
    connection2.close()
    s.close()

if __name__ == "__main__":
    main()