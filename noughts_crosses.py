import time
import random

def start():
    
    while True:
        print ("Would you like to,")
        print ("[1] Play Game\n[2] See Rules\n[3] Leave Game")
        startChoice = input ("[1/2/3]:")

        if startChoice == "1":
            print ("Lets Play!")
            setup()
            continue

        if startChoice == "2":
            print ("\nRULES:")
            print ("The player and computer will take turns to place noughts 'O' and crosses 'X' on a 3x3 grid.\nTo win, you must place 3 crosses in a row anywhere on the grid,")
            print ("However, if the computer places 3 noughts in a row first, you will lose!\n")
            continue

        if startChoice == "3":
            break

        else:
            print ("Please enter a listed option from the menu.")
            continue  

def setup():
    
    pos = {1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}

    print ("\nLets flip a coin to see who goes first,\nIf it lands heads, the player goes first.\nIf it lands tails, the computer goes first.")
    flip = input ("\nPress enter to flip a coin")
    print ("...")

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

    print ("[CPU TURN]")

    while True:
        selection = random.randint(1,9)

        if pos[int(selection)] in {"X","O"}:
            continue
        
        if selection in pos:
            print (str(selection)+" selected.")
            break

    pos[selection] = "O"

    print_board(pos)

    check_win(pos)

    check_draw(pos)

    player_turn(pos)

def player_turn(pos):

    print_board(pos)

    print ("[YOUR TURN]")

    print ("To place your 'X', Please select a number inside the grid")
    while True:
        selection = input ("[1-9]:")

        try:
            selection = int(selection)
        except:
            print("Please enter a number!")
            continue

        if selection not in pos:
            print ("Please enter a number from the grid!")
            continue

        if pos[int(selection)] in {"X","O"}:
            print ("That spot is already taken!")
            continue
        
        if selection in pos:
            print (str(selection)+" selected.")
            break

    pos[selection] = "X"

    print_board(pos)

    check_win(pos)

    check_draw(pos)

    computer_turn(pos)

def print_board(pos):
    
    print("\n")
    print (f" {pos[1]} | {pos[2]} | {pos[3]} ")
    print ("---+---+---")
    print (f" {pos[4]} | {pos[5]} | {pos[6]} ")
    print ("---+---+---")
    print (f" {pos[7]} | {pos[8]} | {pos[9]} ")
    print("\n")

def check_win(pos):
        
    if (pos[1] == 'X' and pos[2] == 'X' and pos[3] == 'X') \
    or (pos[4] == 'X' and pos[5] == 'X' and pos[6] == 'X') \
    or (pos[7] == 'X' and pos[8] == 'X' and pos[9] == 'X') \
    or (pos[1] == 'X' and pos[4] == 'X' and pos[7] == 'X') \
    or (pos[2] == 'X' and pos[5] == 'X' and pos[8] == 'X') \
    or (pos[3] == 'X' and pos[6] == 'X' and pos[9] == 'X') \
    or (pos[1] == 'X' and pos[5] == 'X' and pos[9] == 'X') \
    or (pos[7] == 'X' and pos[5] == 'X' and pos[3] == 'X'):
        result = ("player")
        game_end(result)

    if (pos[1] == 'O' and pos[2] == 'O' and pos[3] == 'O') \
    or (pos[4] == 'O' and pos[5] == 'O' and pos[6] == 'O') \
    or (pos[7] == 'O' and pos[8] == 'O' and pos[9] == 'O') \
    or (pos[1] == 'O' and pos[4] == 'O' and pos[7] == 'O') \
    or (pos[2] == 'O' and pos[5] == 'O' and pos[8] == 'O') \
    or (pos[3] == 'O' and pos[6] == 'O' and pos[9] == 'O') \
    or (pos[1] == 'O' and pos[5] == 'O' and pos[9] == 'O') \
    or (pos[7] == 'O' and pos[5] == 'O' and pos[3] == 'O'):
        result = ("cpu")
        game_end(result)

def check_draw(pos):
    pass
    
def game_end(result):

    if result == ("player"):
        print ("*** YOU WIN! ***")
        playerScore = playerScore +1

    if result == ("cpu"):
        print ("*** YOU LOSE - THE COMPUTER WINS ***")
        cpuScore = cpuScore +1

    if result == ("draw"):
        print ("*** DRAW - NOBODY WINS ***")
        drawScore = drawScore +1

    print ("SCORES:\nPLAYER - "+str(playerScore)+" wins.\nCOMPUTER - "+str(cpuScore)+" wins.\nTIES - "+str(drawScore)+" games.")

    start()
