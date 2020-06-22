#board
#disply the boRD
#play the game 
#handel a turn
#check win
    #check rows
    #check columns
    #check diagonals
#check tie
#flip btw player

#-----global Variables-----
board = [1,2,3,
         4,5,6,
         7,8,9]

gameStillGoing = True

#who won?tie
winner = None

#whos turn is it
currentPlayer = "X"
i = 0


#display Board
def displayBoard():
    print( " | " + str(board[0]) + " | " + str(board[1]) + " | " + str(board[2]) + " | ")
    print( " | " + str(board[3]) + " | " + str(board[4]) + " | " + str(board[5]) + " | ")
    print( " | " + str(board[6]) + " | " + str(board[7]) + " | " + str(board[8]) + " | ")


#handel a single turn of an arbitery player
def handelTurn(player):
    position = input(currentPlayer + "'s turn. Please choose a poition form 1 to 9:")

    valid = False
    while not valid: 

        while position not in ['1','2','3','4','5','6','7','8','9']:
            position = input("Invalid input Please choose a poition form 1 to 9:")
        
        position = int (position) - 1 

        if board[position] == "X" or board[position] == "Y":
            print("you cant go there")
        else:
            valid = True
            

    board[position] = player
    displayBoard()

def checkIfGameOver():
    checkIfWin()
    checkIfTie()

def checkIfWin():
    global  winner
    #check Rows
    rowWinner = checkRows()
    #check Cloumns
    columnWinner = checkColumns()
    #check diagonals
    diagonalsWinner = checkDiagonals()

    if rowWinner:
        #there was a win
        winner = rowWinner
    elif columnWinner:
        #there was a win
        winner = columnWinner
    elif diagonalsWinner:
        #there was a win
        winner = diagonalsWinner
    else:
        #there was no win 
        winner = None
    return

def checkRows():
    #set up gloabl variables
    global gameStillGoing

    #check if all the rows has the same value

    row_1 = board[0] == board[1] == board[2]
    row_2 = board[3] == board[4] == board[5]
    row_3 = board[6] == board[7] == board[8]
    # if any rows has a match ,flag there is a win
    if row_1 or row_2 or row_3:
        gameStillGoing = False

    #return the winner x or o
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def checkColumns():

    #set up gloabl variables
    global gameStillGoing

    #check if all the columns has the same value

    col_1 = board[0] == board[3] == board[6]
    col_2 = board[1] == board[4] == board[7]
    col_3 = board[2] == board[5] == board[8]
    # if any rows has a match ,flag there is a win
    if col_1 or col_2 or col_3:
        gameStillGoing = False

    #return the winner x or o
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    return
    

def checkDiagonals():
    #set up gloabl variables
    global gameStillGoing

    #check if all the columns has the same value

    diagonal_1 = board[0] == board[4] == board[8]
    diagonal_2 = board[2] == board[4] == board[6]
    # if any rows has a match ,flag there is a win
    if diagonal_1 or diagonal_2:
        gameStillGoing = False

    #return the winner x or o
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
     
    return 

def checkIfTie():
    global gameStillGoing
    global i 
    i +=1
    
    if i == 9:
        gameStillGoing = False
    return

        
def flipPlayer():
    global currentPlayer
    #  changing the current player basicly toglling the player
    if currentPlayer =="X":
         currentPlayer = "O"
    elif currentPlayer =="O":
         currentPlayer = "X"
    return


def playGame():
    #display the initial board
    displayBoard()

    #while the game is still going   
    while gameStillGoing:
        
        # Hnadel the turns btw players
        handelTurn(currentPlayer)

        #check if gae has ended
        checkIfGameOver()

        #change player
        flipPlayer()
        
    # the game has ended
    if winner == "X" or winner == "O":
        print(winner + " Won")
    elif winner == None:
        print ("Tie")


playGame()    