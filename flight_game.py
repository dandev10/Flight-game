print("hello welcome to flight   (version 0.0.2-2a)")
name = input("what your name?\n")
print("hello", name)
run = True
while run:
    print("Write commands below (Write as they are wroten below): ")
    print("                                                       Fly")
    print("                                                       About (It will say about the game) ")
    commands = input(" ")
    if "Fly" in commands:
        print("Choose a flight: ")
        print("                 SAS-804; LONDON-OSLO. Write Sas")
        print("                 NORWIGIAN-735; HAU-OSLO. Write Nor")
        print("                 WIZZAIR-356; NYC-LONDON. Write Wizz")
        flight = input("What flight? ")
    elif "About" in commands:
        print("")
