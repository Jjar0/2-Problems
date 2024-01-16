def start():
    
    while True:
        print ("Would you like to,")
        print ("[1] Play Game\n[2] See Rules\n[3] Session Score")
        startChoice = input ("[1/2/3]:")

        if startChoice == "1":
            print ("Lets Play!")
            set_turn()

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



        test_board()

        

def set_turn():
    pass

def test_board():

    pos = {1:" ",2:" ",3:" ",4:" ",5:" ",6:" ",7:" ",8:" ",9:" "}
    
    print (f" {pos[1]} | {pos[2]} | {pos[3]} ")
    print ("---+---+---")
    print (f" {pos[4]} | {pos[5]} | {pos[6]} ")
    print ("---+---+---")
    print (f" {pos[7]} | {pos[8]} | {pos[9]} ")
    

start()