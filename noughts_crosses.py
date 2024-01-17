def start():
    
    while True:
        print ("Would you like to,")
        print ("[1] Play Game\n[2] See Rules\n[3] Session Score")
        startChoice = input ("[1/2/3]:")

        if startChoice == "1":
            print ("Lets Play!")
            setup()
            continue

        if startChoice == "2":
            print ("\nRULES:")
            print ("The player and computer will take turns to place noughts 'O' and crosses 'X' on a 3x3 grid.\nTo win, you must place 3 noughts in a row anywhere on the grid,")
            print ("However, if the computer places 3 crosses in a row first, you will lose!\n")
            continue

        if startChoice == "3":
            continue

        else:
            print ("Please enter a listed option from the menu.")
            continue
        

def setup():
    
    pos = {1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9"}

    print ("\nLets flip a coin to see who goes first,\nIf it lands heads, the player goes first.\nIf it lands tails, the computer goes first.")
    flip = input ("\nPress enter to flip a coin")
    print ("...")

    import random
    coin = random.randint(1,9)
    landing = (coin%2)

    if landing == 0:
        print ("Heads!\nPlayer goes first.")
        player_turn(pos)
    
    if landing == 1:
        print ("Tails!\nComputer goes first.")
        computer_turn(pos)

    pass

def computer_turn(pos):
    pass

def player_turn(pos):

    print_board(pos)



    pass

def print_board(pos):
    
    print("\n")
    print (f" {pos[1]} | {pos[2]} | {pos[3]} ")
    print ("---+---+---")
    print (f" {pos[4]} | {pos[5]} | {pos[6]} ")
    print ("---+---+---")
    print (f" {pos[7]} | {pos[8]} | {pos[9]} ")
    print("\n")
    

start()