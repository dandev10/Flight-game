print("hello welcome to flight   (version 1.0)")
import time, random
print("Loading game...")
time.sleep(5)
name = input("what your name?\n")
print("hello ", name)
print("please first read about the game or you dont get point of game!!")
print("loading kart, airplanes and airport...")
time.sleep(10)
run = True
the_number = random.randint(5, 15)



while run:
    print(("you have 3 airplanes"))
    print("Write commands below (Write as they are wroten below): ")
    print("                                                       Fly")
    print("                                                       About (It will say about the game) ")
 
    commands = input(" ")
    if "Fly" in commands:
        print("Choose a flight: ")
        print("                 SAS-804; LONDON-NYC. Write Sas")
        print("                 NORWIGIAN-735; LONDON-TRONDHEIM. Write Nor")
        print("                 WIZZAIR-356; LONDON-OSLO. Write Wizz")
        flight = input("What flight? ")
        if "Sas" in flight:
            print("                write Start to start fly")
            commandsas = input(" ") 
            if "Start" in commandsas:
                guess = int(input("write how long miles need to get to New york: "))
                while guess!= the_number:
                    if guess > the_number:
                        print(guess, "to long. ")
                    if guess < the_number:
                        print(guess, "for short man")
                    guess = int(input("the last chance"))
                print(guess, "thats right")
                print("Flying...") 
                time.sleep(25)
                print("Welcome to new york")
                print("you got 50 flight coins ")
        if "Nor" in flight:
            print("                write Start to start fly")
            commandnor = input(" ")
            if "Start" in commandnor:
                 guess = int(input("write how long miles need to get to Trondheim: "))
                 while guess!= the_number:
                    if guess > the_number:
                        print(guess, "to long. ")
                    if guess < the_number:
                        print(guess, "for short man")
                    guess = int(input("the last chance"))
                 print(guess, "thats right")
                 print("Flying...")
                 time.sleep(24)
                 print("Welcome to trondheim") 
        if "Wizz" in flight:
            print("              write Start to start fly")
            commandwiz = input(" ")
            if "Start" in commandwiz:
                 guess = int(input("write how long miles need to get to OSLO: "))
                 while guess!= the_number:
                    if guess > the_number:
                        print(guess, "to long. ")
                    if guess < the_number:
                        print(guess, "for short man")
                    guess = int(input("the last chance"))
                 print(guess, "thats right")
                 print("Flying...")
                 time.sleep(25)
                 print("Welcome to OSLO")

    if "About" in commands:
        print("game made by THESpager and nikeedev. this is orginal version of flight game. this game is about")
        print("flight andveturs an full of sky flying ")
        print(" we can`t wait to you try it. ", name)

    else:
        continue
