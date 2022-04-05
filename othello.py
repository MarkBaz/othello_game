#Tilemachos-Markos Mpazakas, A.M. 3281


#for deepcopy purposes
import copy

def create_board():
    board=[[0 for i in range(8)]for j in range(8)]
    board[3][3]=1
    board[4][4]=1
    board[3][4]=2
    board[4][3]=2

    return board


def print_board(board):
    print('    0   1   2   3   4   5   6   7')
    for y in range(8):
        print((y),end=' ')
        for x in range(8):
            print(('| %s'%board[x][y]), end=' ')
        print('|')


def allowed_move(x,y,board,player):
    if board[x][y]!=0:
        return False
    returned = False
    if player == 1:
        this_player = 1
        opponent = 2
    else:
        this_player = 2
        opponent = 1
    if y>0:
        if board[x][y-1] == opponent:
            returned = check_up(x,y,board,this_player)
            if returned:
                return returned
    if y<7:
        if board[x][y+1] == opponent:
            returned = check_down(x,y,board,this_player)
            if returned:
                return returned
    if x<7:
        if board[x+1][y] == opponent:
            returned = check_right(x,y,board,this_player)
            if returned:
                return returned
    if x>0:
        if board[x-1][y] == opponent:
            returned = check_left(x,y,board,this_player)
            if returned:
                return returned
        #up left
    if y>0 and x>0:
        if board[x-1][y-1] == opponent:
            returned = check_up_left(x,y,board,this_player)
            if returned:
                return returned
        #down left
    if x>0 and y<7:
        if board[x-1][y+1] == opponent:
            returned = check_down_left(x,y,board,this_player)
            if returned:
                return returned
        #down right
    if x<7 and y<7:
        if board[x+1][y+1] == opponent:
            returned = check_down_right(x,y,board,this_player)
            if returned:
                return returned
        #up right
    if y>0 and x<7:
        if board[x+1][y-1] == opponent:
            returned = check_up_right(x,y,board,this_player)
    return returned




    
#check for allowed move up                
def check_up(x,y,board,this_player):
        y=y-1
        while (y>=0):
            if board[x][y]==this_player:
                return True
            if board[x][y]==0:
                return False
            y=y-1
        return False

def check_down(x,y,board,this_player):
        y=y+1
        while (y<=7):
            if board[x][y]==this_player:
                return True
            if board[x][y]==0:
                return False
            y=y+1
        return False

def check_left(x,y,board,this_player):
        x=x-1
        while (x>=0):
            if board[x][y]==this_player:
                return True
            if board[x][y]==0:
                return False
            x=x-1
        return False

def check_right(x,y,board,this_player):
        x=x+1
        while (x<=7):
            if board[x][y]==this_player:
                return True
            if board[x][y]==0:
                return False
            x=x+1
        return False

def check_up_left(x,y,board,this_player):
    x=x-1
    y=y-1
    if (x>y):
        while (y>=0) and (x>=0):
            if board[x][y]==this_player:
                return True
            if board[x][y]==0:
                return False
            x=x-1
            y=y-1
        return False
    else:
        while (x>=0) and (y>=0):
            if board[x][y]==this_player:
                return True
            if board[x][y]==0:
                return False
            x=x-1
            y=y-1
        return False

def check_down_left(x,y,board,this_player):
    x=x-1
    y=y+1
    if (x>y):
        while (x>=0) and (y<=7):
            if board[x][y]==this_player:
                return True
            if board[x][y]==0:
                return False
            x=x-1
            y=y+1
        return False
    else:
        while (y<=7) and (x>=0):
            if board[x][y]==this_player:
                return True
            if board[x][y]==0:
                return False
            x=x-1
            y=y+1
        return False
    
def check_down_right(x,y,board,this_player):
    x=x+1
    y=y+1
    if (x>y):
        while (x<=7) and (y<=7):
            if board[x][y]==this_player:
                return True
            if board[x][y]==0:
                return False
            x=x+1
            y=y+1
        return False
    else:
        while (y<=7) and (x<=7):
            if board[x][y]==this_player:
                return True
            if board[x][y]==0:
                return False
            x=x+1
            y=y+1
        return False
    
def check_up_right(x,y,board,this_player):
    x=x+1
    y=y-1
    if (x>y):
        while (y>=0) and (x<=7):
            if board[x][y]==this_player:
                return True
            if board[x][y]==0:
                return False
            x=x+1
            y=y-1
        return False
    else:
        while (x<=7) and (y>=0):
            if board[x][y]==this_player:
                return True
            if board[x][y]==0:
                return False
            x=x+1
            y=y-1
        return False

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def reverse_counts (x,y,board,player):
    counter = 0
    if player == 1:
        this_player = 1
        opponent = 2
    else:
        this_player = 2
        opponent = 1
    if y>0:
        if board[x][y-1] == opponent:
            counter = counter + check_up_count(x,y,board,this_player)
    if y<7:
        if board[x][y+1] == opponent:
            counter = counter + check_down_count(x,y,board,this_player)
    if x<7:
        if board[x+1][y] == opponent:
            counter = counter + check_right_count(x,y,board,this_player)
    if x>0:
        if board[x-1][y] == opponent:
            counter = counter + check_left_count(x,y,board,this_player)
    #up left
    if x>0 and y>0:
        if board[x-1][y-1] == opponent:
            counter = counter + check_up_left_count(x,y,board,this_player)
    #down left
    if x>0 and y<7:
        if board[x-1][y+1] == opponent:
            counter = counter + check_down_left_count(x,y,board,this_player)
    #down right
    if x<7 and y<7:
        if board[x+1][y+1] == opponent:
            counter = counter + check_down_right_count(x,y,board,this_player)
    #up right
    if x<7 and y>0:
        if board[x+1][y-1] == opponent:
            counter = counter + check_up_right_count(x,y,board,this_player)
    return counter




    
#check for allowed move up                
def check_up_count(x,y,board,this_player):
        y=y-1
        counter = 0
        while (y>=0):
            counter = counter + 1
            if board[x][y]==this_player:
                return counter-1
            if board[x][y]==0:
                return 0
            y=y-1
        return 0

def check_down_count(x,y,board,this_player):
        y=y+1
        counter = 0
        while (y<=7):
            counter = counter + 1
            if board[x][y]==this_player:
                return counter-1
            if board[x][y]==0:
                return 0
            y=y+1
        return 0

def check_left_count(x,y,board,this_player):
        x=x-1
        counter = 0
        while (x>=0):
            counter = counter + 1
            if board[x][y]==this_player:
                return counter-1
            if board[x][y]==0:
                return 0
            x=x-1
        return 0

def check_right_count(x,y,board,this_player):
        x=x+1
        counter = 0
        while (x<=7):
            counter = counter + 1
            if board[x][y]==this_player:
                return counter-1
            if board[x][y]==0:
                return 0
            x=x+1
        return 0

def check_up_left_count(x,y,board,this_player):
    x=x-1
    y=y-1
    counter = 0
    if (x>y):
        while (y>=0) and (x>=0):
            counter = counter + 1
            if board[x][y]==this_player:
                return counter-1
            if board[x][y]==0:
                return 0
            x=x-1
            y=y-1
        return 0
    else:
        while (y>=0) and (x>=0):
            counter = counter + 1
            if board[x][y]==this_player:
                return counter-1
            if board[x][y]==0:
                return 0
            x=x-1
            y=y-1
        return 0

def check_down_left_count(x,y,board,this_player):
    x=x-1
    y=y+1
    counter = 0
    if (x>y):
        while (x>=0) and (y<=7):
            counter = counter + 1
            if board[x][y]==this_player:
                return counter-1
            if board[x][y]==0:
                return 0
            x=x-1
            y=y+1
        return 0
    else:
        while (x>=0) and (y<=7):
            counter = counter + 1
            if board[x][y]==this_player:
                return counter-1
            if board[x][y]==0:
                return 0
            x=x-1
            y=y+1
        return 0
    
def check_down_right_count(x,y,board,this_player):
    x=x+1
    y=y+1
    counter = 0
    if (x>y):
        while (x<=7) and (y<=7):
            counter = counter + 1
            if board[x][y]==this_player:
                return counter-1
            if board[x][y]==0:
                return 0
            x=x+1
            y=y+1
        return 0
    else:
        while (x<=7) and (y<=7):
            counter = counter + 1
            if board[x][y]==this_player:
                return counter-1
            if board[x][y]==0:
                return 0
            x=x+1
            y=y+1
        return 0
    
def check_up_right_count(x,y,board,this_player):
    x=x+1
    y=y-1
    counter = 0
    if (x>y):
        while (y>=0) and (x<=7):
            counter = counter + 1
            if board[x][y]==this_player:
                return counter-1
            if board[x][y]==0:
                return 0
            x=x+1
            y=y-1
        return 0
    else:
        while (x>=0) and (x<=7):
            counter = counter + 1
            if board[x][y]==this_player:
                return counter-1
            if board[x][y]==0:
                return 0
            x=x+1
            y=y-1
        return 0




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def compute_counts (x,y,board,player):
    computed_board = [[0 for i in range(8)]for j in range(8)]
    if player == 1:
        this_player = 1
        opponent = 2
    else:
        this_player = 2
        opponent = 1
    if y>0:
        if board[x][y-1] == opponent:
            computed_board = check_up_computed(x,y,board,this_player,computed_board)
    if y<7:
        if board[x][y+1] == opponent:
            computed_board = check_down_computed(x,y,board,this_player,computed_board)
    if x<7:
        if board[x+1][y] == opponent:
            computed_board = check_right_computed(x,y,board,this_player,computed_board)
    if x>0:
        if board[x-1][y] == opponent:
            computed_board = check_left_computed(x,y,board,this_player,computed_board)
    #up left
    if x>0 and y>0:
        if board[x-1][y-1] == opponent:
            computed_board = check_up_left_computed(x,y,board,this_player,computed_board)
    #down left
    if x>0 and y<7:
        if board[x-1][y+1] == opponent:
            computed_board = check_down_left_computed(x,y,board,this_player,computed_board)
    #down right
    if x<7 and y<7:
        if board[x+1][y+1] == opponent:
            computed_board = check_down_right_computed(x,y,board,this_player,computed_board)
    #up right
    if x<7 and y>0:
        if board[x+1][y-1] == opponent:
            computed_board = check_up_right_computed(x,y,board,this_player,computed_board)
    return computed_board




    
#check for allowed move up                
def check_up_computed(x,y,board,this_player,computed_board):
        board_old = copy.deepcopy(computed_board)
        y=y-1
        while (y>=0):
            if board[x][y]==this_player:
                return computed_board
            if board[x][y]==0:
                return board_old
            computed_board[x][y]=this_player
            y=y-1
        return board_old

def check_down_computed(x,y,board,this_player,computed_board):
        board_old = copy.deepcopy(computed_board)
        y=y+1
        while (y<=7):
            if board[x][y]==this_player:
                return computed_board
            if board[x][y]==0:
                return board_old
            computed_board[x][y]=this_player
            y=y+1
        return board_old

def check_left_computed(x,y,board,this_player,computed_board):
        board_old = copy.deepcopy(computed_board)
        x=x-1
        while (x>=0):
            if board[x][y]==this_player:
                return computed_board
            if board[x][y]==0:
                return board_old
            computed_board[x][y]=this_player
            x=x-1
        return board_old

def check_right_computed(x,y,board,this_player,computed_board):
        board_old = copy.deepcopy(computed_board)
        x=x+1
        while (x<=7):
            if board[x][y]==this_player:
                return computed_board
            if board[x][y]==0:
                return board_old
            computed_board[x][y]=this_player
            x=x+1
        return board_old

def check_up_left_computed(x,y,board,this_player,computed_board):
    board_old = copy.deepcopy(computed_board)
    x=x-1
    y=y-1
    if (x>y):
        while (y>=0) and (x>=0):
            if board[x][y]==this_player:
                return computed_board
            if board[x][y]==0:
                return board_old
            computed_board[x][y]=this_player
            x=x-1
            y=y-1
        return board_old
    else:
        while (x>=0) and (y>=0):
            if this_player == 1:
                this_player = 1
                opponent = 2
            else:
                this_player = 2
                opponent = 1
            if board[x][y]==this_player:
                return computed_board
            if board[x][y]==0:
                return board_old
            computed_board[x][y]=this_player
            x=x-1
            y=y-1
  
        return board_old

def check_down_left_computed(x,y,board,this_player,computed_board):
    board_old = copy.deepcopy(computed_board)
    x=x-1
    y=y+1
    if (x>y):
        while (x>=0) and (y<=7):
            if board[x][y]==this_player:
                return computed_board
            if board[x][y]==0:
                return board_old
            computed_board[x][y]=this_player
            x=x-1
            y=y+1
        return board_old
    else:
        while (x>=0) and (y<=7):
            if board[x][y]==this_player:
                return computed_board
            if board[x][y]==0:
                return board_old
            computed_board[x][y]=this_player
            x=x-1
            y=y+1
        return board_old
    
def check_down_right_computed(x,y,board,this_player,computed_board):
    board_old = copy.deepcopy(computed_board)
    x=x+1
    y=y+1
    if (x>y):
        while (x<=7) and (y<=7):
            if board[x][y]==this_player:
                return computed_board
            if board[x][y]==0:
                return board_old
            computed_board[x][y]=this_player
            x=x+1
            y=y+1
        return board_old
    else:
        while (x<=7) and (y<=7):
            if board[x][y]==this_player:
                return computed_board
            if board[x][y]==0:
                return board_old
            computed_board[x][y]=this_player
            x=x+1
            y=y+1
        return board_old
    
def check_up_right_computed(x,y,board,this_player,computed_board):
    board_old = copy.deepcopy(computed_board)
    x=x+1
    y=y-1
    if (x>y):
        while (y>=0) and (x<=7):
            if board[x][y]==this_player:
                return computed_board
            if board[x][y]==0:
                return board_old
            computed_board[x][y]=this_player
            x=x+1
            y=y-1
        return board_old
    else:
        while (x<=7) and (y>=0):
            if board[x][y]==this_player:
                return computed_board
            if board[x][y]==0:
                return board_old
            computed_board[x][y]=this_player
            x=x+1
            y=y-1
        return board_old





def add_checker(x,y,board,player):
    board_computed = compute_counts(x,y,board,player)
    print('\nTiles changed')
    print_board(board_computed)
    board[x][y]=player
    for y in range(8):
        for x in range(8):
            if board_computed[x][y]==player:
                board[x][y] = player
    print('\nBoard after move')
    return board

def score_human(x,y,board):
    oneScore = 0
    twoScore = 0
    for x in range(8):
        for y in range(8):
            if board[x][y] == 1:
                oneScore += 1
            if board[x][y] == 2:
                twoScore += 1
    return {'Scoreboard: Player 1':oneScore, 'Player 2':twoScore}

def score_computer(x,y,board):
    ComputerScore = 0
    PlayerScore = 0
    for x in range(8):
        for y in range(8):
            if board[x][y] == 1:
                ComputerScore += 1
            if board[x][y] == 2:
                PlayerScore += 1
    return {'Scoreboard: Computer':ComputerScore, 'Player':PlayerScore}
    




def human_play(board,player):

    
    print('\nPLAYER: ',player,' HAS THE NEXT MOVE')
    #list of allowed moves
    AllowedMoves = []
    checkForAllowed = False
    for i in range(8):
        for j in range(8):
            if allowed_move(i,j,board,player):
                checkForAllowed = True
                AllowedMoves.append([i,j])
    
    if AllowedMoves == []:
        print('\nThe player has no moves available')
        return
    
    else:
        print('Your allowed moves are:',AllowedMoves)
    
    if (not checkForAllowed):
        return False
    digits = '0 1 2 3 4 5 6 7'.split()
    while True:
        print('Enter your move, "nn"')
        move = input()
        if len(move) == 2 and move[0] in digits and move[1] in digits:
            x = int(move[0]) 
            y = int(move[1])
            if allowed_move(x,y,board,player) == False:
                print('Invalid move, try one of the allowed moves')
                continue
            else:
                break
        else:
            print('Out of boarders, try one of the allowed moves')
    
    boardAfterMove = add_checker(x,y,board,player)
    scoreAfterMove = score_human(x,y,board)
    print_board(boardAfterMove)
    print(scoreAfterMove)
    return
    
    
    
    


def computer_play(board,player):

    #list of allowed moves
    AllowedMoves = []
    checkForAllowed = False
    for i in range(8):
        for j in range(8):
            if allowed_move(i,j,board,player):
                checkForAllowed = True
                
                
                AllowedMoves.append([i,j])

    

    #if there is a zero in the board
    ZeroFound = False
    for i in range(8):
        for j in range(8):
            if board[i][j] == 0:
                ZeroFound = True
                break
    if ZeroFound == True and AllowedMoves == []:
        print('\nThe player has no moves available')
        return

    elif AllowedMoves == []:
        print('\nEnd of the game, thanks for playing')
        
    if (not checkForAllowed):
        return False



    #computers move
    while True:
        print('\nComputer choosing next move wisely...')
        CompMove = AllowedMoves
        maxReversed = 0
        #here we have the number of the allowed moves the computer has
        NumberOfCompsAllowed = len(CompMove)
        for i in range(NumberOfCompsAllowed):
            #print(CompMove[i])
            x = CompMove[i][0]
            y = CompMove[i][1]
            reversedTiles = reverse_counts(x,y,board,player)
            if reversedTiles > maxReversed:
                maxReversed = reversedTiles
                xMax = x                    #best moves x
                yMax = y                    #best moves y
            #print(reversedTiles)
        break
        print(x,y)
        reversedTiles = reverse_counts(xMax,yMax,board,player)
        boardAfterMove = add_checker(xMax,yMax,board,player)
        scoreAfterMove = score_computer(xMax,yMax,board)
        print_board(boardAfterMove)       
        print(reversedTiles)
        
    print('Computer is playing...')
    boardAfterMove = add_checker(xMax,yMax,board,player)
    print_board(boardAfterMove)
    scoreAfterMove = score_computer(xMax,yMax,board)
    print(scoreAfterMove)















#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#main program
player = 1 or 2
opponent = 1 or 2
board = create_board()
print_board(board)
ComputerOrPlayer = ''
while not (ComputerOrPlayer == 'player' or ComputerOrPlayer == 'computer'):
    print('\nChoose between a player or the computer, please type "player" or "computer":')
    ComputerOrPlayer = input().lower()
if ComputerOrPlayer == 'player':
    while True:
        ZeroFound = False           #check if there are empty tiles
        for i in range(8):
            for j in range(8):
                if board[i][j] == 0:
                    ZeroFound = True
        if ZeroFound:
            human_play(board,2)
        else:
            break                   #if no empty tiles terminate game
        ZeroFound = False
        for i in range(8):
            for j in range(8):
                if board[i][j] == 0:
                    ZeroFound = True
        if ZeroFound:
            human_play(board,1)
        else:
            break
    countForPlayer1 = 0
    countForPlayer2 = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == 1:
                countForPlayer1 = countForPlayer1 + 1
            elif board[i][j] == 2:
                countForPlayer2 = countForPlayer2 + 1
    if countForPlayer1>countForPlayer2:
        print('Player 1 WINS!')
    elif countForPlayer1<countForPlayer2:
        print('Player 2 WINS!')
    else:
        print('DRAW!')
    print('Game is over, Thanks for playing')
    
if ComputerOrPlayer == 'computer':
    while True:
        ZeroFound = False           #check if there are empty tiles
        for i in range(8):
            for j in range(8):
                if board[i][j] == 0:
                    ZeroFound = True
        if ZeroFound:
            human_play(board,2)
        else:
            break                   #if no empty tiles terminate game
        ZeroFound = False
        for i in range(8):
            for j in range(8):
                if board[i][j] == 0:
                    ZeroFound = True
        if ZeroFound:
            computer_play(board,1)
        else:
            break
    countForComputer = 0
    countForPlayer = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == 1:
                countForComputer = countForComputer + 1
            elif board[i][j] == 2:
                countForPlayer = countForPlayer + 1
    if countForComputer>countForPlayer:
        print('Computer WINS!')
    elif countForComputer<countForPlayer:
        print('Player WINS!')
    else:
        print('DRAW!')
    print('Game is over, Thanks for playing!')




        







