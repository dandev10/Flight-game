print("hello welcome to flight   (version 0.0.3a)")
print("Loading game...")
import time, random
time.sleep(5)
name = input("what your name?\n")
print("hello ", name)
run = True
position = "LONDON"
locations = ["NYC", "TRONDHEIM", "OSLO", "LONDON"] 
#def shuffran():
   # random.

while run:
    print(f"You are now at {position}")
    print(("also you have 3 airplanes"))
    print("Write commands below (Write as they are wroten below): ")
    print("                                                       Fly")
    print("                                                       About (It will say about the game) ")
    print("                                                       write Money to(see your flight money)")
    print("                                                       write Market to buy something")
    commands = input(" ")
    if "Fly" in commands:
        print("Choose a flight: ")
        print(f"                 SAS-804; {position}-{random.choice(locations)}. Write Sas")
        print(f"                 NORWIGIAN-735; {position}-TRONDHEIM. Write Nor")
        print(f"                 WIZZAIR-356; {position}-NYC. Write Wizz")
        flight = input("What flight? ")
        if "Sas" in flight:
            print("                write Start to start fly")
            commandsas = input(" ") 
            if "Start" in commandsas:
                print("flying...") 
                time.sleep(25)
                position = "OSLO"
                print(f"Welcome to {position}")
                print("you got 50 flight coins ")
        if "Nor" in flight:
            print("                write Start to start fly")
            commandnor = input(" ")
            if "Start" in commandnor:
                print("Flying...")
                time.sleep(24)
                print("welcome to Trondheim") 
        if "Wizz" in flight:
            print("              write Start to start fly")
            commandwiz = input(" ")
            if "Start" in commandwiz:
                print("flying...")
                time.sleep(25)
                print("welcome to New york")

    elif "Money" in commands:
        print("you have now 0 flight coins")

    if "Market" in commands:
        print("welcome to Market! here you can buy  new airport places and airplanes for flight coins")
        print("                  write Airplane to buy Airplanes")
        print("                  write Airport to buy Airport landing place")
        commandmark = input(" ")

        if "Airplane" in commandmark:
            print("what Airplane do you want to buy wait a minute i thing i can chose for you")
            time.sleep(3)
            print("aha what about emirates 3sec faster then Sas")



    if "About" in commands:
        print("game made by THESpager and nikeedev. this is orginal version of flight game. this game is about")
        print("flight andveturs an full of sky flying and make money and of this money you can unlock new ")
        print("places, airplanes, some of them are faster and make more money. we can`t wait to you try it.")
