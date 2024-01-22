import random

def wipe_scores(): #wipes scores when a student is done playing

    playerScore = 0
    cpuScore = 0
    drawScore = 0
    start(playerScore,cpuScore,drawScore)

def start(playerScore,cpuScore,drawScore): #main menu for game

    while True: #input validation loop for menu
        print ("Would you like to,")
        print ("[1] Play Game\n[2] See Rules\n[3] See Scores\n[4] Wipe Scores\n[5] Leave Game")
        startChoice = input ("[1/2/3]:")

        if startChoice == "1":
            print ("Lets Play!")
            setup(playerScore,cpuScore,drawScore)
            continue

        if startChoice == "2":
            print ("\nRULES:")
            print ("The player and computer will take turns to place noughts 'O' and crosses 'X' on a 3x3 grid.\nTo win, you must place 3 crosses in a row anywhere on the grid,")
            print ("However, if the computer places 3 noughts in a row first, you will lose!\n")
            continue

        if startChoice == "3":
            print ("\nCURRENT SCORES:\nPLAYER - "+str(playerScore)+" wins.\nCOMPUTER - "+str(cpuScore)+" wins.\nTIES - "+str(drawScore)+" games.\n") #display scores
            continue

        if startChoice == "4":
            print ("Scores have been wiped.")
            wipe_scores()

        if startChoice == "5":
            break #game ends here

        else:
            print ("Please enter a listed option from the menu.")
            continue  

def setup(playerScore,cpuScore,drawScore): #chooses turns, defines game variables
    
    pos = {1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'} #dictionary for numpad ascii display

    turn = 0

    print ("\nLets flip a coin to see who goes first,\nIf it lands heads, the player goes first.\nIf it lands tails, the computer goes first.")
    flip = input ("\nPress enter to flip a coin")
    print ("...")

    coin = random.randint(1,9) #50/50 chance coin toss for first turn
    landing = (coin%2)

    if landing == 0:
        print ("Heads!\nPlayer goes first.")
        player_turn(pos,turn,playerScore,cpuScore,drawScore)
    
    if landing == 1:
        print ("Tails!\nComputer goes first.")
        computer_turn(pos,turn,playerScore,cpuScore,drawScore)

def computer_turn(pos,turn,playerScore,cpuScore,drawScore):

    print ("[CPU TURN]")

    while True:
        selection = random.randint(1,9) #cpu selects random position on board

        if pos[int(selection)] in {"X","O"}: #checking if spot is taken
            continue
        
        if selection in pos:
            print (str(selection)+" selected.") #display to player which spot cpu chose
            break

    pos[selection] = "O" #replace number with 'O'

    turn = turn+1 #increment turn count

    print_board(pos)

    check_win(pos,playerScore,cpuScore,drawScore) #check for draw, win and change to players turn

    check_draw(turn,playerScore,cpuScore,drawScore)

    player_turn(pos,turn,playerScore,cpuScore,drawScore)

def player_turn(pos,turn,playerScore,cpuScore,drawScore):#players turn

    print_board(pos)

    print ("[YOUR TURN]")

    print ("To place your 'X', Please select a number inside the grid")
    while True:
        selection = input ("[1-9]:")#player chooses values 1-9

        try:
            selection = int(selection) #input validation for integers
        except:
            print("Please enter a number!")
            continue

        if selection not in pos: #validation for range of inputs
            print ("Please enter a number from the grid!")
            continue

        if pos[int(selection)] in {"X","O"}: #check if spot is taken
            print ("That spot is already taken!") #[REVISION - TEST 7] changed validation to function properly.
            continue
        
        if selection in pos:
            print (str(selection)+" selected.")#confirm selection to player
            break

    pos[selection] = "X" #replace number selected with 'X'

    turn = turn+1 #increment turn count

    print_board(pos)

    check_win(pos,playerScore,cpuScore,drawScore) #check for win, draw, go to computer turn.

    check_draw(turn,playerScore,cpuScore,drawScore)

    computer_turn(pos,turn,playerScore,cpuScore,drawScore)

def print_board(pos): #Displays board and current dictionary values to the player every turn
    
    print("\n")
    print (f" {pos[1]} | {pos[2]} | {pos[3]} ")
    print ("---+---+---")
    print (f" {pos[4]} | {pos[5]} | {pos[6]} ")
    print ("---+---+---")
    print (f" {pos[7]} | {pos[8]} | {pos[9]} ")
    print("\n")

def check_win(pos,playerScore,cpuScore,drawScore): #checks for game win.
        
    if (pos[1] == 'X' and pos[2] == 'X' and pos[3] == 'X') \
    or (pos[4] == 'X' and pos[5] == 'X' and pos[6] == 'X') \
    or (pos[7] == 'X' and pos[8] == 'X' and pos[9] == 'X') \
    or (pos[1] == 'X' and pos[4] == 'X' and pos[7] == 'X') \
    or (pos[2] == 'X' and pos[5] == 'X' and pos[8] == 'X') \
    or (pos[3] == 'X' and pos[6] == 'X' and pos[9] == 'X') \
    or (pos[1] == 'X' and pos[5] == 'X' and pos[9] == 'X') \
    or (pos[3] == 'X' and pos[5] == 'X' and pos[7] == 'X'): #[REVISION - TEST 12] Added win checking for diagonal lines.
        result = "player"
        game_end(result,playerScore,cpuScore,drawScore)

    if (pos[1] == 'O' and pos[2] == 'O' and pos[3] == 'O') \
    or (pos[4] == 'O' and pos[5] == 'O' and pos[6] == 'O') \
    or (pos[7] == 'O' and pos[8] == 'O' and pos[9] == 'O') \
    or (pos[1] == 'O' and pos[4] == 'O' and pos[7] == 'O') \
    or (pos[2] == 'O' and pos[5] == 'O' and pos[8] == 'O') \
    or (pos[3] == 'O' and pos[6] == 'O' and pos[9] == 'O') \
    or (pos[1] == 'O' and pos[5] == 'O' and pos[9] == 'O') \
    or (pos[3] == 'O' and pos[5] == 'O' and pos[7] == 'O'):
        result = "cpu"
        game_end(result,playerScore,cpuScore,drawScore)

def check_draw(turn,playerScore,cpuScore,drawScore): #checks turn count to see if board is full
    if turn == 9:
        result = "draw"
        game_end(result,playerScore,cpuScore,drawScore)
    
    
def game_end(result,playerScore,cpuScore,drawScore): #displays scores to the player at game end

    if result == ("player"):
        print ("*** YOU WIN! ***") #iterate scores depending on game results
        playerScore = playerScore+1

    if result == ("cpu"):
        print ("*** YOU LOSE - THE COMPUTER WINS ***")
        cpuScore = cpuScore+1

    if result == ("draw"):
        print ("*** DRAW - NOBODY WINS ***")
        drawScore = drawScore+1

    print ("\nSCORES:\nPLAYER - "+str(playerScore)+" wins.\nCOMPUTER - "+str(cpuScore)+" wins.\nTIES - "+str(drawScore)+" games.\n") #display scores

    print ("\nDo you want to [1] play another round? or [2] exit to menu?") #ask player if they wish to play aggain immediatley or go to menu

    while True:
        epilogue = input ("[1/2]:")

        if epilogue == '1':
            setup(playerScore,cpuScore,drawScore)

        if epilogue == '2':
            start(playerScore,cpuScore,drawScore)

        else:
            print ("Please enter a listed number,")
            continue

