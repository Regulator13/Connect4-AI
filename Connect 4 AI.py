#Connect 4 AI
#Programmed by: Isaiah Frey
#This AI will allow you to play a game of connect 4 against a computer of several different difficulties using the mini-max funtion.


###
global move_count
move_count = 0

#Functions

def sign(number):
    if (number >= 0):
        return 1
    if (number < 0):
        return -1

def Place(board, piece, col):
    for row in range (0,6):
        if (board[5-row][col] == '_'):
            board[5-row][col] = piece
            return board

def Min_row(board, col):
    for row in range (0,6):
        if (board[5-row][col] == '_'):
            row = 5 - row
            return row
    #If the column is full return 6 to avoid that column
    row = 6
    return row

def Print_board():
    for row in range (0,6):
        print ("\n")
        for col in range (0,7):
            print (board[row][col], " ", end='')
    print ("\n")
    
def Print_score_board(score_board):
    max_length = 0
    num_length = [['_','_','_','_'],
                  ['_','_','_','_'],
                  ['_','_','_','_'],
                  ['_','_','_','_']]
    for row in range (0,4):
        for col in range (0,4):
            length = len(str(score_board[row][col]))
            if (length > max_length):
                max_length = length
    for row in range (0,4):
        for col in range (0,4):
            num_length[row][col] = len(str(score_board[row][col]))
    print (score_board[0][0], ' '*(max_length - num_length[0][0]), score_board[0][1], ' '*(max_length - num_length[0][1]), score_board[0][2], ' '*(max_length - num_length[0][2]), score_board[0][3], ' '*(max_length - num_length[0][3]),)
    print (score_board[1][0], ' '*(max_length - num_length[1][0]), score_board[1][1], ' '*(max_length - num_length[1][1]), score_board[1][2], ' '*(max_length - num_length[1][2]), score_board[1][3], ' '*(max_length - num_length[1][3]),)
    print (score_board[2][0], ' '*(max_length - num_length[2][0]), score_board[2][1], ' '*(max_length - num_length[2][1]), score_board[2][2], ' '*(max_length - num_length[2][2]), score_board[2][3], ' '*(max_length - num_length[2][3]),)
    print (score_board[3][0], ' '*(max_length - num_length[3][0]), score_board[3][1], ' '*(max_length - num_length[3][1]), score_board[3][2], ' '*(max_length - num_length[3][2]), score_board[3][3], ' '*(max_length - num_length[3][3]),)

def Reset_score_board():
    for row in range(0,4):
        for col in range(0,4):
            score_board[row][col] = '_'

def Choose_depth(board, smart_fast, smart_medium, smart_slow):
    if (smart_fast):
        pieces_placed = Pieces_placed(board)
        if (pieces_placed == 0):
            DEPTH = 1
        if (pieces_placed > 0 and pieces_placed < 22):
            DEPTH = 4
        if (pieces_placed >= 22 and pieces_placed < 28):
            DEPTH = 5
        if (pieces_placed >= 28 and pieces_placed < 34):
            DEPTH = 6
        if (pieces_placed >= 34):
            DEPTH = 7
    if (smart_medium):
        pieces_placed = Pieces_placed(board)
        if (pieces_placed == 0):
            DEPTH = 1
        if (pieces_placed > 0 and pieces_placed < 22):
            DEPTH = 5
        if (pieces_placed >= 22 and pieces_placed < 26):
            DEPTH = 6
        if (pieces_placed >= 26 and pieces_placed < 30):
            DEPTH = 7
        if (pieces_placed >= 30):
            DEPTH = 8
    if (smart_slow):
        pieces_placed = Pieces_placed(board)
        if (pieces_placed == 0):
            DEPTH = 1
        if (pieces_placed > 0 and pieces_placed < 22):
            DEPTH = 6
        if (pieces_placed >= 22 and pieces_placed < 26):
            DEPTH = 7
        if (pieces_placed >= 26 and pieces_placed < 30):
            DEPTH = 8
        if (pieces_placed >= 30):
            DEPTH = 9
    return DEPTH

def Find_in_row(board, row, col, piece):
    score = 0
    #Check to see if this piece has already been counted
    #Check downward direction
    if (board[row][col] == piece):
        if ((not board[row - 1][col] == piece) or (row == 0)):
            if (row < 5):
                if (board[row + 1][col] == piece):
                    if (row < 4):
                        if(board[row + 2][col] == piece):
                            if (row < 3):
                                if(board[row + 3][col] == piece):
                                    score+= 1000
                            score += 15
                    score += 3
    #Check diagnol right direction
        if ((not board[row - 1][col - 1] == piece) or (row == 0) or (col == 0)):
            if (row < 5 and col < 6):
                if (board[row + 1][col + 1] == piece):
                    if (row < 4 and col < 5):
                        if(board[row + 2][col + 2] == piece):                           
                            if (row < 3 and col < 4):
                                if(row < 2 and col < 4):
                                    if(board[row + 3][col + 3] == '_' and board[row + 4][col + 3] == '_' and (row + 3)%2 == first):
                                        score+= 40
                                if(board[row + 3][col + 3] == piece):
                                    return 1000
                            if(row > 0 and col > 0):
                                if(board[row - 1][col - 1] == '_' and board[row][col - 1] == '_' and (row - 1)%2 == first):
                                    score+= 40 
                            score += 15
                    score += 3
    #Check diagnol left direction
        try:
            if ((not board[row - 1][col + 1] == piece) or (row == 0) or (col == 6)):
                if (row < 5 and col > 0):
                    if (board[row + 1][col - 1] == piece):
                        if (row < 4 and col > 1):
                            if(board[row + 2][col - 2] == piece):
                                if (row < 3 and col > 2):
                                    if(row < 2 and col > 2):
                                        if(board[row + 3][col - 3] == '_' and board[row + 4][col + 3] == '_' and (row + 3)%2 == first):
                                            score += 40
                                    if(board[row + 3][col - 3] == piece):
                                        return 1000
                                if(row > 0 and col < 6):
                                    if(board[row - 1][col + 1] == '_' and board[row][col + 1] == '_' and (row - 1)%2 == first):
                                        score += 40
                                score += 15
                        score += 3
        except IndexError:
            score += 0
    #Check horizontal direction
        if ((not board[row][col - 1] == piece) or (col == 0)):
            if (board[row][col] == piece):
                if (col < 6):
                    if (board[row][col + 1] == piece):
                        if (col < 5):
                            if(board[row][col + 2] == piece):
                                if (col < 4):
                                    if(row < 5 and col < 4):
                                        if(board[row][col + 3] == '_' and board[row + 1][col + 3] == '_' and (row)%2 == first):
                                            score += 40
                                    if(board[row][col + 3] == piece):
                                        return 1000
                                if(row < 5 and col > 0):
                                    if(board[row][col - 1] == '_' and board[row + 1][col - 1] == '_' and (row - 1)%2 == first):
                                        score += 40
                                score += 15
                        score += 3
    else:
        return 0
    return score


def Pieces_placed(board):
    pieces_placed = 0
    for row in range (0,6):
        for col in range (0,7):
            if (not board[row][col] == '_'):
                pieces_placed += 1
    return pieces_placed

def Check_win(board):
    global move_count
    move_count += 1
    scoreX = 0   #Set a tally for the number of points X got
    scoreO = 0   #Set a tally for the number of points O got
    game_over = False #See if the game is over or not    
    #For each space, see how many are in a row for X
    piece = 'X'
    for row in range (0,6):
        for col in range (0,7):
            scoreX += Find_in_row(board,row,col,piece)
    #For each space, see how many are in a row for O
    piece = 'O'
    for row in range (0,6):
        for col in range (0,7):
            scoreO += Find_in_row(board,row,col,piece)   
    #Check for end of game
    pieces_placed = Pieces_placed(board)
    #Check to see if the game was a tie
    if (pieces_placed > 41):
        game_over = True
    #Check to see if someone connected 4
    if (scoreX >= 1000 or scoreO >= 1000):
        game_over = True
    #return values
    return scoreX,scoreO,game_over
    
def Eval_board(board, turn):
    scoreX,scoreO,game_over = Check_win(board)
    score = scoreX - scoreO
    return score, game_over

def Mini_max(board, depth, turn_computer, alpha, beta):
    score, game_over = Eval_board(board, turn)
    if (game_over):      #When the game is over return the score
        return score
    #Find best move for computer's turn
    if (depth >= 0 and depth <= (DEPTH - 1)):
        if alpha < beta:
            if(turn_computer):
                best = -1000
                for col in range (0,7):
                    row = Min_row(board,col)
                    if (row < 6):
                        board[row][col] = 'X'
                        best = max(best, Mini_max(board, depth - 1, False, alpha, beta))
                        alpha = max(alpha, best)
                        board[row][col] = '_'
                return best
            if(not turn_computer):
                best = 1000
                for col in range (0,7):
                    row = Min_row(board,col)
                    if (row < 6):
                        board[row][col] = 'O'
                        best = min(best, Mini_max(board, depth - 1, True, alpha, beta))
                        beta = min(beta, best)
                        board[row][col] = '_'
                return best
    return score

def Find_best_move(board, turn, DEPTH, smart_fast, smart_medium, smart_slow):
    best_col = -1
    col = 0
    best_temp = -5000
    alpha = -5000
    beta = 5000
    #Allow the computer to adapt it's depth based on the number of moves left
    if (DEPTH > 8):
        DEPTH = Choose_depth(board, smart_fast, smart_medium, smart_slow)
    for col in range(0,7):
        row = Min_row(board,col)
        if(row < 6):
            board[row][col] = 'X'
            best = Mini_max(board, DEPTH - 1, False, alpha, beta)
            if (col == 1 or col == 5):   #Have the computer favor the center squares
                best += 1
            if (col == 2 or col == 4):
                best += 2
            if (col == 3):
                best += 3
            ###
            #score_board[row][col] = best
            ###
            if(best > best_temp):
                best_col = col
                best_row = row
                ###
                print ("Best col is ", best_col)
                print ("Best row is ", best_row)
                print ("With a score of ", best)
                ###
                best_temp = best
            board[row][col] = '_'
    #Print_score_board(score_board)
    #Reset_score_board()
    return best_col

#Single time setup
print ("Connect-4 AI by Isaiah Frey")
while(True):    
    rules = input("Would you like to read the rules or learn about the computers? If so type 'y' then hit enter. Otherwise just hit enter: ")
    if (rules == 'y'):
        read = '''\n    Connect-4 is a two player strategy game where each player takes turn placing tokens on a vertical board. The goal of the game
is to get 4 of your pieces in a row, horizontally, vertically, or diagonally. Choose a column and you piece will drop to the bottom of it. In this game you will
face a computer player of a difficulty level of your choosing. You can choose a difficulty 0-7, which basically determines how many moves in advance the computer
will look forward. You can also choose 9, 10, or 11 for an adaptable computer player, which increase the number of moves it looks ahead as the game goes on.
        
    Computing which move to make takes time. A level 7 will take over a minute to make most its moves, as it is trying nearly a million combinations. Level 6 takes
around 10 seconds, and level 5 and below move almost instantly. Level 9, 10, and 11 move about as fast as a level 4, 5, and 6 respectively. Try out the
different difficulties and enjoy!\n'''
        print (read)
        go_on = input("Press a key to continue.")
        break
    else:
        break
#Gameplay
while(True):
    board = [['_','_','_','_','_','_','_'], #setup the board
             ['_','_','_','_','_','_','_'],
             ['_','_','_','_','_','_','_'],
             ['_','_','_','_','_','_','_'],
             ['_','_','_','_','_','_','_'],
             ['_','_','_','_','_','_','_']]
    
    score_board = [['_','_','_','_','_','_','_'], #setup a grid to show how good certain spaces are
                   ['_','_','_','_','_','_','_'],
                   ['_','_','_','_','_','_','_'],
                   ['_','_','_','_','_','_','_'],
                   ['_','_','_','_','_','_','_'],
                   ['_','_','_','_','_','_','_']]
    turn = 1
    game_over = False
    smart_fast = False
    smart_medium = False
    smart_slow = False
    #Setup difficulty
    while(True):
        try:
            #Set the number of moves the AI should look ahead (max is 15 for 4X4 Tic-tac-toe)
            DEPTH = int(input("Choose a difficulty from 0 to 9, 0 being the easiest and 6 being the hardest normal difficulty.\nYou can also choose 9 for the adaptive fast computer, 10 for the adaptive medium computer, or 11 for the adaptive slow computer: "))
        except ValueError:
            print("Please choose a number!")
            continue
        if (DEPTH == 9):
            smart_fast = True
        if (DEPTH == 10):
            smart_medium = True
        if (DEPTH == 11):
            smart_slow = True
        if(DEPTH < 0 or DEPTH > 9):
            print("Please choose a number from 0 to 9.")
            continue
        else:
            break
    
    #Decide who goes first
    while(True):
        try:
            first = int(input("Choose who goes first, 1 for the computer or 0 for you: "))
        except ValueError:
            print("Please enter a number!")
            continue
        if(first > 1 or first < 0):
            print("Please choose either 1 or 0.")
        else:
            break
    
    #Begin the game
    Print_board()
    while(not game_over):
        if (not game_over):
            if (turn%2 == first):                
                move_count = 0
                print ("Computer's turn")
                col = Find_best_move(board, turn, DEPTH, smart_fast, smart_medium, smart_slow)
                Place(board, 'X', col)
                turn += 1
                Print_board()
                scoreX,scoreO,game_over = Check_win(board)
                print ("The computer tried ", move_count, " moves.")              
        if (not game_over):
            if (turn%2 == (not first)):   
                while(True):
                    move_count = 0
                    try:
                        col = (int(input("Input a value 1-7 for the column you want to place an O in. 1 is left and 7 is right: "))) - 1
                    except ValueError:
                        print("Please enter a number!")
                        continue
                    if(col > 6 or col < 0):
                        print("Please choose a number between 1 and 7")
                    else:
                        break
                if (board[0][col] == '_'):
                    Place(board, 'O' ,col)
                    turn += 1
                    Print_board()
                    scoreX,scoreO,game_over = Check_win(board)
                else:
                    print ("This column is full, try another one.")
    
    #Once the game has ended see who won
    scoreX,scoreO,game_over = Check_win(board)
    if (scoreX > scoreO):
        print ("The computer won %d to %d." %(scoreX, scoreO))
    if (scoreX < scoreO):
        print ("You won %d to %d!" %(scoreO,scoreX))
    if (scoreX == scoreO):
        print ("It's a Tie %d to %d!" %(scoreO,scoreX))
    answer = input("Play again? Press y to continue or another key to exit: ")
    if(answer == 'y'):
        continue
    else:
        print("Thanks for playing!")
        break
    