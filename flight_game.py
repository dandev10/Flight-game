print("hello welcome to flight   (version 0.0.3a)")
print("Loading game...")
import time, random
time.sleep(5)
name = input("what your name?\n")
print("hello ", name)
run = True
position = "LONDON"
locations = ["NYC", "TRONDHEIM", "OSLO", "LONDON"] 
def shuffran():
    if (random.choice(locations) == position):
        return shuffran
    else:
        return random.choice(locations)


while run:
    print(f"You are now at {position}")
    print("Write commands below (Write as they are wroten below): ")
    print("                                                       Fly")
    print("                                                       About (It will say about the game) ")
    print("                                                       write Money to(see your flight money)")
    commands = input(" ")
    if "Fly" in commands:
        flight1 = shuffran()
        flight2 = shuffran()
        flight3 = shuffran()
        print("Choose a flight: ")
        print(f"                 SAS-804; {position}-{flight1}. Write Sas")
        print(f"                 NORWIGIAN-735; {position}-{flight2}. Write Nor")
        print(f"                 WIZZAIR-356; {position}-{flight3}. Write Wizz")
        flight = input("What flight? ")
        if "Sas" in flight:
            print("                write Start to start fly")
            commandsas = input(" ") 
            if "Start" in commandsas:
                print("Flying...") 
                time.sleep(25)
                position = flight1
                print(f"Welcome to {position}")
        if "Nor" in flight:
            print("                write Start to start fly")
            commandnor = input(" ")
            if "Start" in commandnor:
                print("Flying...")
                time.sleep(24)
                position = flight2
                print(f"Welcome to {position}") 
        if "Wizz" in flight:
            print("              write Start to start fly")
            commandwiz = input(" ")
            if "Start" in commandwiz:
                print("Flying...")
                time.sleep(25)
                position = flight3
                print(f"Welcome to {position}")

    elif "Money" in commands:
        print("you have now 0 flight coins") 



    if "About" in commands:
        print("game made by THESpager and nikeedev. this is orginal version of flight game. this game is about")
        print("flight andveturs an full of sky flying and make money and of this money you can unlock new ")
        print("places, airplanes, some of them are faster and make more money. we can`t wait to you try it.")

    else:
        continue
