#Tilemachos-Markos Mpazakas, A.M. 3281


from tkinter import *
import copy
import time
root = Tk()
root.wm_title("OTHELLO")
pouli = Canvas(root,width=400, height=400)
pouli.pack(side=LEFT)


human=Button(root,text="HUMAN PLAY",width=15, height=3,bg="yellow", fg="black",cursor="target")
human.config(font=("Courier", 16))
human.pack(side=RIGHT)
comp=Button(root,text="COMPUTER PLAY",width=15, height=3,bg="yellow", fg="black",cursor="target")
comp.config(font=("Courier", 16))
comp.pack(side=RIGHT)
mes = Label(root, width=15, height=3)
mes.config(font=("Courier", 16))
mes.pack()
scoreword = Label(root,width=15,height=1)
scoreword.config(font=("Courier", 16))
scoreword.pack()
players = Label(root,width=15,height=1)
players.config(font=("Courier", 16))
players.pack()
score = Label(root,width=15, height=1)
score.config(font=("Courier", 16))
score.pack()




global AllowedMoves
global turn


def graphic_board():
    for x in range(8):
        for y in range(8):
            pouli.create_rectangle( x * 50, y * 50, 50 + x * 50, 50 + y * 50, fill="green")
            if (x == 3 and y == 4) or (x == 4 and y == 3):
                pouli.create_oval(5 + x * 50, 5 + y * 50, 45 + x * 50, 45 + y * 50, fill="black")
            if (x == 3 and y == 3) or (x == 4 and y == 4):
                pouli.create_oval(5 + x * 50, 5 + y * 50, 45 + x * 50, 45 + y * 50, fill="white")


def new_board(board):
    for x in range(8):
        for y in range(8):
            pouli.create_rectangle(x * 50, y * 50, 50 + x * 50, 50 + y * 50, fill="green")
            if board[x][y] == 2:
                pouli.create_oval(5+x * 50, 5 + y * 50, 45 + x * 50, 45 + y * 50, fill="black")
            if board[x][y] == 1:
                pouli.create_oval(5 + x * 50, 5 + y * 50, 45 + x * 50, 45 + y * 50, fill="white")


def create_board():
    board = [[0 for i in range(8)] for j in range(8)]
    board[3][3] = 1
    board[4][4] = 1
    board[3][4] = 2
    board[4][3] = 2
    return board


def allowed_move(x, y, board, player):
    if board[x][y] != 0:
        return False
    returned = False
    if player == 1:
        this_player = 1
        opponent = 2
    else:
        this_player = 2
        opponent = 1
    if y > 0:
        if board[x][y - 1] == opponent:
            returned = check_up(x, y, board, this_player)
            if returned:
                return returned
    if y < 7:
        if board[x][y + 1] == opponent:
            returned = check_down(x, y, board, this_player)
            if returned:
                return returned
    if x < 7:
        if board[x + 1][y] == opponent:
            returned = check_right(x, y, board, this_player)
            if returned:
                return returned
    if x > 0:
        if board[x - 1][y] == opponent:
            returned = check_left(x, y, board, this_player)
            if returned:
                return returned
                # up left
    if y > 0 and x > 0:
        if board[x - 1][y - 1] == opponent:
            returned = check_up_left(x, y, board, this_player)
            if returned:
                return returned
                # down left
    if x > 0 and y < 7:
        if board[x - 1][y + 1] == opponent:
            returned = check_down_left(x, y, board, this_player)
            if returned:
                return returned
                # down right
    if x < 7 and y < 7:
        if board[x + 1][y + 1] == opponent:
            returned = check_down_right(x, y, board, this_player)
            if returned:
                return returned
                # up right
    if y > 0 and x < 7:
        if board[x + 1][y - 1] == opponent:
            returned = check_up_right(x, y, board, this_player)
    return returned


# check for allowed move up
def check_up(x, y, board, this_player):
    y = y - 1
    while (y >= 0):
        if board[x][y] == this_player:
            return True
        if board[x][y] == 0:
            return False
        y = y - 1
    return False


def check_down(x, y, board, this_player):
    y = y + 1
    while (y <= 7):
        if board[x][y] == this_player:
            return True
        if board[x][y] == 0:
            return False
        y = y + 1
    return False


def check_left(x, y, board, this_player):
    x = x - 1
    while (x >= 0):
        if board[x][y] == this_player:
            return True
        if board[x][y] == 0:
            return False
        x = x - 1
    return False


def check_right(x, y, board, this_player):
    x = x + 1
    while (x <= 7):
        if board[x][y] == this_player:
            return True
        if board[x][y] == 0:
            return False
        x = x + 1
    return False


def check_up_left(x, y, board, this_player):
    x = x - 1
    y = y - 1
    if (x > y):
        while (y >= 0) and (x >= 0):
            if board[x][y] == this_player:
                return True
            if board[x][y] == 0:
                return False
            x = x - 1
            y = y - 1
        return False
    else:
        while (x >= 0) and (y >= 0):
            if board[x][y] == this_player:
                return True
            if board[x][y] == 0:
                return False
            x = x - 1
            y = y - 1
        return False


def check_down_left(x, y, board, this_player):
    x = x - 1
    y = y + 1
    if (x > y):
        while (x >= 0) and (y <= 7):
            if board[x][y] == this_player:
                return True
            if board[x][y] == 0:
                return False
            x = x - 1
            y = y + 1
        return False
    else:
        while (y <= 7) and (x >= 0):
            if board[x][y] == this_player:
                return True
            if board[x][y] == 0:
                return False
            x = x - 1
            y = y + 1
        return False


def check_down_right(x, y, board, this_player):
    x = x + 1
    y = y + 1
    if (x > y):
        while (x <= 7) and (y <= 7):
            if board[x][y] == this_player:
                return True
            if board[x][y] == 0:
                return False
            x = x + 1
            y = y + 1
        return False
    else:
        while (y <= 7) and (x <= 7):
            if board[x][y] == this_player:
                return True
            if board[x][y] == 0:
                return False
            x = x + 1
            y = y + 1
        return False


def check_up_right(x, y, board, this_player):
    x = x + 1
    y = y - 1
    if (x > y):
        while (y >= 0) and (x <= 7):
            if board[x][y] == this_player:
                return True
            if board[x][y] == 0:
                return False
            x = x + 1
            y = y - 1
        return False
    else:
        while (x <= 7) and (y >= 0):
            if board[x][y] == this_player:
                return True
            if board[x][y] == 0:
                return False
            x = x + 1
            y = y - 1
        return False


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def reverse_counts(x, y, board, player):
    counter = 0
    if player == 1:
        this_player = 1
        opponent = 2
    else:
        this_player = 2
        opponent = 1
    if y > 0:
        if board[x][y - 1] == opponent:
            counter = counter + check_up_count(x, y, board, this_player)
    if y < 7:
        if board[x][y + 1] == opponent:
            counter = counter + check_down_count(x, y, board, this_player)
    if x < 7:
        if board[x + 1][y] == opponent:
            counter = counter + check_right_count(x, y, board, this_player)
    if x > 0:
        if board[x - 1][y] == opponent:
            counter = counter + check_left_count(x, y, board, this_player)
    # up left
    if x > 0 and y > 0:
        if board[x - 1][y - 1] == opponent:
            counter = counter + check_up_left_count(x, y, board, this_player)
    # down left
    if x > 0 and y < 7:
        if board[x - 1][y + 1] == opponent:
            counter = counter + check_down_left_count(x, y, board, this_player)
    # down right
    if x < 7 and y < 7:
        if board[x + 1][y + 1] == opponent:
            counter = counter + check_down_right_count(x, y, board, this_player)
    # up right
    if x < 7 and y > 0:
        if board[x + 1][y - 1] == opponent:
            counter = counter + check_up_right_count(x, y, board, this_player)
    return counter


# check for allowed move up
def check_up_count(x, y, board, this_player):
    y = y - 1
    counter = 0
    while (y >= 0):
        counter = counter + 1
        if board[x][y] == this_player:
            return counter - 1
        if board[x][y] == 0:
            return 0
        y = y - 1
    return 0


def check_down_count(x, y, board, this_player):
    y = y + 1
    counter = 0
    while (y <= 7):
        counter = counter + 1
        if board[x][y] == this_player:
            return counter - 1
        if board[x][y] == 0:
            return 0
        y = y + 1
    return 0


def check_left_count(x, y, board, this_player):
    x = x - 1
    counter = 0
    while (x >= 0):
        counter = counter + 1
        if board[x][y] == this_player:
            return counter - 1
        if board[x][y] == 0:
            return 0
        x = x - 1
    return 0


def check_right_count(x, y, board, this_player):
    x = x + 1
    counter = 0
    while (x <= 7):
        counter = counter + 1
        if board[x][y] == this_player:
            return counter - 1
        if board[x][y] == 0:
            return 0
        x = x + 1
    return 0


def check_up_left_count(x, y, board, this_player):
    x = x - 1
    y = y - 1
    counter = 0
    if (x > y):
        while (y >= 0) and (x >= 0):
            counter = counter + 1
            if board[x][y] == this_player:
                return counter - 1
            if board[x][y] == 0:
                return 0
            x = x - 1
            y = y - 1
        return 0
    else:
        while (y >= 0) and (x >= 0):
            counter = counter + 1
            if board[x][y] == this_player:
                return counter - 1
            if board[x][y] == 0:
                return 0
            x = x - 1
            y = y - 1
        return 0


def check_down_left_count(x, y, board, this_player):
    x = x - 1
    y = y + 1
    counter = 0
    if (x > y):
        while (x >= 0) and (y <= 7):
            counter = counter + 1
            if board[x][y] == this_player:
                return counter - 1
            if board[x][y] == 0:
                return 0
            x = x - 1
            y = y + 1
        return 0
    else:
        while (x >= 0) and (y <= 7):
            counter = counter + 1
            if board[x][y] == this_player:
                return counter - 1
            if board[x][y] == 0:
                return 0
            x = x - 1
            y = y + 1
        return 0


def check_down_right_count(x, y, board, this_player):
    x = x + 1
    y = y + 1
    counter = 0
    if (x > y):
        while (x <= 7) and (y <= 7):
            counter = counter + 1
            if board[x][y] == this_player:
                return counter - 1
            if board[x][y] == 0:
                return 0
            x = x + 1
            y = y + 1
        return 0
    else:
        while (x <= 7) and (y <= 7):
            counter = counter + 1
            if board[x][y] == this_player:
                return counter - 1
            if board[x][y] == 0:
                return 0
            x = x + 1
            y = y + 1
        return 0


def check_up_right_count(x, y, board, this_player):
    x = x + 1
    y = y - 1
    counter = 0
    if (x > y):
        while (y >= 0) and (x <= 7):
            counter = counter + 1
            if board[x][y] == this_player:
                return counter - 1
            if board[x][y] == 0:
                return 0
            x = x + 1
            y = y - 1
        return 0
    else:
        while (x >= 0) and (x <= 7):
            counter = counter + 1
            if board[x][y] == this_player:
                return counter - 1
            if board[x][y] == 0:
                return 0
            x = x + 1
            y = y - 1
        return 0


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def compute_counts(x, y, board, player):
    computed_board = [[0 for i in range(8)] for j in range(8)]
    if player == 1:
        this_player = 1
        opponent = 2
    else:
        this_player = 2
        opponent = 1
    if y > 0:
        if board[x][y - 1] == opponent:
            computed_board = check_up_computed(x, y, board, this_player, computed_board)
    if y < 7:
        if board[x][y + 1] == opponent:
            computed_board = check_down_computed(x, y, board, this_player, computed_board)
    if x < 7:
        if board[x + 1][y] == opponent:
            computed_board = check_right_computed(x, y, board, this_player, computed_board)
    if x > 0:
        if board[x - 1][y] == opponent:
            computed_board = check_left_computed(x, y, board, this_player, computed_board)
    # up left
    if x > 0 and y > 0:
        if board[x - 1][y - 1] == opponent:
            computed_board = check_up_left_computed(x, y, board, this_player, computed_board)
    # down left
    if x > 0 and y < 7:
        if board[x - 1][y + 1] == opponent:
            computed_board = check_down_left_computed(x, y, board, this_player, computed_board)
    # down right
    if x < 7 and y < 7:
        if board[x + 1][y + 1] == opponent:
            computed_board = check_down_right_computed(x, y, board, this_player, computed_board)
    # up right
    if x < 7 and y > 0:
        if board[x + 1][y - 1] == opponent:
            computed_board = check_up_right_computed(x, y, board, this_player, computed_board)
    return computed_board


# check for allowed move up
def check_up_computed(x, y, board, this_player, computed_board):
    board_old = copy.deepcopy(computed_board)
    y = y - 1
    while (y >= 0):
        if board[x][y] == this_player:
            return computed_board
        if board[x][y] == 0:
            return board_old
        computed_board[x][y] = this_player
        y = y - 1
    return board_old


def check_down_computed(x, y, board, this_player, computed_board):
    board_old = copy.deepcopy(computed_board)
    y = y + 1
    while (y <= 7):
        if board[x][y] == this_player:
            return computed_board
        if board[x][y] == 0:
            return board_old
        computed_board[x][y] = this_player
        y = y + 1
    return board_old


def check_left_computed(x, y, board, this_player, computed_board):
    board_old = copy.deepcopy(computed_board)
    x = x - 1
    while (x >= 0):
        if board[x][y] == this_player:
            return computed_board
        if board[x][y] == 0:
            return board_old
        computed_board[x][y] = this_player
        x = x - 1
    return board_old


def check_right_computed(x, y, board, this_player, computed_board):
    board_old = copy.deepcopy(computed_board)
    x = x + 1
    while (x <= 7):
        if board[x][y] == this_player:
            return computed_board
        if board[x][y] == 0:
            return board_old
        computed_board[x][y] = this_player
        x = x + 1
    return board_old


def check_up_left_computed(x, y, board, this_player, computed_board):
    board_old = copy.deepcopy(computed_board)
    x = x - 1
    y = y - 1
    if (x > y):
        while (y >= 0) and (x >= 0):
            if board[x][y] == this_player:
                return computed_board
            if board[x][y] == 0:
                return board_old
            computed_board[x][y] = this_player
            x = x - 1
            y = y - 1
        return board_old
    else:
        while (x >= 0) and (y >= 0):
            if this_player == 1:
                this_player = 1
                opponent = 2
            else:
                this_player = 2
                opponent = 1
            if board[x][y] == this_player:
                return computed_board
            if board[x][y] == 0:
                return board_old
            computed_board[x][y] = this_player
            x = x - 1
            y = y - 1

        return board_old


def check_down_left_computed(x, y, board, this_player, computed_board):
    board_old = copy.deepcopy(computed_board)
    x = x - 1
    y = y + 1
    if (x > y):
        while (x >= 0) and (y <= 7):
            if board[x][y] == this_player:
                return computed_board
            if board[x][y] == 0:
                return board_old
            computed_board[x][y] = this_player
            x = x - 1
            y = y + 1
        return board_old
    else:
        while (x >= 0) and (y <= 7):
            if board[x][y] == this_player:
                return computed_board
            if board[x][y] == 0:
                return board_old
            computed_board[x][y] = this_player
            x = x - 1
            y = y + 1
        return board_old


def check_down_right_computed(x, y, board, this_player, computed_board):
    board_old = copy.deepcopy(computed_board)
    x = x + 1
    y = y + 1
    if (x > y):
        while (x <= 7) and (y <= 7):
            if board[x][y] == this_player:
                return computed_board
            if board[x][y] == 0:
                return board_old
            computed_board[x][y] = this_player
            x = x + 1
            y = y + 1
        return board_old
    else:
        while (x <= 7) and (y <= 7):
            if board[x][y] == this_player:
                return computed_board
            if board[x][y] == 0:
                return board_old
            computed_board[x][y] = this_player
            x = x + 1
            y = y + 1
        return board_old


def check_up_right_computed(x, y, board, this_player, computed_board):
    board_old = copy.deepcopy(computed_board)
    x = x + 1
    y = y - 1
    if (x > y):
        while (y >= 0) and (x <= 7):
            if board[x][y] == this_player:
                return computed_board
            if board[x][y] == 0:
                return board_old
            computed_board[x][y] = this_player
            x = x + 1
            y = y - 1
        return board_old
    else:
        while (x <= 7) and (y >= 0):
            if board[x][y] == this_player:
                return computed_board
            if board[x][y] == 0:
                return board_old
            computed_board[x][y] = this_player
            x = x + 1
            y = y - 1
        return board_old


def add_checker(x, y, board, player):
    board_computed = compute_counts(x, y, board, player)
    board[x][y] = player
    for y in range(8):
        for x in range(8):
            if board_computed[x][y] == player:
                board[x][y] = player
    return board


def score_human(x, y, board):
    oneScore = 0
    twoScore = 0
    for x in range(8):
        for y in range(8):
            if board[x][y] == 1:
                oneScore += 1
            if board[x][y] == 2:
                twoScore += 1

    return oneScore, "-", twoScore


def score_computer(x, y, board):
    ComputerScore = 0
    PlayerScore = 0
    for x in range(8):
        for y in range(8):
            if board[x][y] == 1:
                ComputerScore += 1
            if board[x][y] == 2:
                PlayerScore += 1
    return PlayerScore, "-", ComputerScore


def humanclick(event):
    
    global AllowedMoves
    global turn
    x = int((event.x ) / 50)
    y = int((event.y) / 50)
    if [x, y] not in AllowedMoves:
        return
    if turn == 1:
        player = 1
    if turn == 2:
        player = 2

    if [x, y] in AllowedMoves:
        pouli.delete("all")
        boardAfterMove = add_checker(x, y, board, player)
        scoreAfterMove = score_human(x, y, board)
        score.config(text=scoreAfterMove)
        new_board(boardAfterMove)
    if turn == 1:
        player = 2
    if turn == 2:
        player = 1
    AllowedMoves = []
    for i in range(8):
        for j in range(8):
            if allowed_move(i, j, board, player):
                checkForAllowed = True
                AllowedMoves.append([i, j])
                pouli.create_oval(15 + i * 50, 15 + j * 50, 35 + i * 50, 35 + j * 50, fill="gray")
    
    if AllowedMoves != []:
        if player == 2:
            turn = 2
            mes.config(text="BLACKPLAYS")
        if player == 1:
            turn = 1
            mes.config(text="WHITEPLAYS")
        return
    else:
        #print(player)
        if player == 1:
            player = 2

        else:
            if player == 2:
                player = 1
                #print(player)
        for i in range(8):
            for j in range(8):
                if allowed_move(i, j, board, player):
                    checkForAllowed = True
                    AllowedMoves.append([i, j])
                    pouli.create_oval(15 + i * 50, 15 + j * 50, 35 + i * 50, 35 + j * 50, fill="gray")
        if AllowedMoves != []:
            if player == 2:
                mes.config(text="BLACKPLAYS  AGAIN")
                turn = 2
            if player == 1:
                mes.config(text="WHITEPLAYS AGAIN")
                turn = 1
            return
        else:
            mes.config(text="GAMEOVER!!!")
        return
def human_play(event):
    global turn
    global AllowedMoves
    mes.config(text="WHITEPLAYS",bg="yellow", fg="black")
    scoreword.config(text="SCORE",bg="orchid",fg="black")   
    players.config(text="WHITE BLACK",bg="orchid",fg="black")
    score.config(text="2 - 2",bg="orchid",fg="black")
    
    
    board = create_board()
    turn = 1
    AllowedMoves = []
    checkForAllowed = False
    for i in range(8):
        for j in range(8):
            if allowed_move(i, j, board, 1):
                checkForAllowed = True
                AllowedMoves.append([i, j])
                pouli.create_oval(15 + i * 50, 15 + j * 50, 35 + i * 50, 35 + j * 50, fill="gray")
    #print(AllowedMoves)
    pouli.bind("<Button-1>", humanclick)
    human.pack_forget()
    comp.pack_forget()
    return
def computer_play(event):
    
    global AllowedMoves
    mes.config(text="HUMAN PLAYS",bg="yellow", fg="black")
    scoreword.config(text="SCORE",bg="orchid",fg="black")   
    players.config(text="COMPUTER HUMAN",bg="orchid",fg="black")
    score.config(text="2 - 2",bg="orchid",fg="black")
    
    
    board = create_board()
    
    AllowedMoves = []
    checkForAllowed = False
    for i in range(8):
        for j in range(8):
            if allowed_move(i, j, board, 1):
                checkForAllowed = True
                AllowedMoves.append([i, j])
                pouli.create_oval(15 + i * 50, 15 + j * 50, 35 + i * 50, 35 + j * 50, fill="gray")
    pouli.bind("<Button-1>", computerclick)
    human.pack_forget()
    comp.pack_forget()
    return
def computerclick(event):        
    global AllowedMoves
    #Human move
    x = int((event.x ) / 50)
    y = int((event.y) / 50)
    if [x, y] not in AllowedMoves:
        return
    player = 1
    AllowedMoves = []
    checkForAllowed = False
    for i in range(8):
        for j in range(8):
            if allowed_move(i, j, board, 1):
                checkForAllowed = True
                AllowedMoves.append([i, j])
                pouli.create_oval(15 + i * 50, 15 + j * 50, 35 + i * 50, 35 + j * 50, fill="gray")
    if AllowedMoves != []:
        if [x, y] in AllowedMoves:
            pouli.delete("all")
            boardAfterMove = add_checker(x, y, board, player)
            scoreAfterMove = score_human(x, y, board)
            score.config(text=scoreAfterMove)
            new_board(boardAfterMove)
            mes.config(text="COMPUTER PLAYS")
            
    if AllowedMoves == []:
        player = 2       
        for i in range(8):
            for j in range(8):
                if allowed_move(i, j, board, player):
                    checkForAllowed = True
                    AllowedMoves.append([i, j])
                    pouli.create_oval(15 + i * 50, 15 + j * 50, 35 + i * 50, 35 + j * 50, fill="gray")
        if AllowedMoves != []:
            mes.config(text="COMPUTER PLAYS  AGAIN")
                           
            return
        else:
            mes.config(text="GAMEOVER!!!")
        return
   
    #Computer move    
    player = 2    
    AllowedMoves = []
    for i in range(8):
        for j in range(8):
            if allowed_move(i, j, board, player):
                checkForAllowed = True
                AllowedMoves.append([i, j])
                pouli.create_oval(15 + i * 50, 15 + j * 50, 35 + i * 50, 35 + j * 50, fill="gray")
               
    if AllowedMoves != []: 
        while True:     
            CompMove = AllowedMoves
            maxReversed = 0
            #here we have the number of the allowed moves the computer has
            NumberOfCompsAllowed = len(CompMove)
            for i in range(NumberOfCompsAllowed):
                x = CompMove[i][0]
                y = CompMove[i][1]
                reversedTiles = reverse_counts(x,y,board,player)
                if reversedTiles > maxReversed:
                    maxReversed = reversedTiles
                    xMax = x                    #best moves x
                    yMax = y                    #best moves y
            break    
            
        
        boardAfterMove = add_checker(xMax,yMax,board,player)
        scoreAfterMove = score_computer(xMax,yMax,board)
        score.config(text=scoreAfterMove)
        new_board(boardAfterMove)       
        mes.config(text="HUMAN PLAYS") 
       
   
    player = 1
    AllowedMoves = [] 
    for i in range(8):
        for j in range(8):
            if allowed_move(i, j, board, player):
               checkForAllowed = True
               AllowedMoves.append([i, j])
               pouli.create_oval(15 + i * 50, 15 + j * 50, 35 + i * 50, 35 + j * 50, fill="gray")
                   
      
    if AllowedMoves == []:
        player = 2       
        for i in range(8):
            for j in range(8):
                if allowed_move(i, j, board, player):
                    checkForAllowed = True
                    AllowedMoves.append([i, j])
                    pouli.create_oval(15 + i * 50, 15 + j * 50, 35 + i * 50, 35 + j * 50, fill="gray")
        if AllowedMoves != []:
            mes.config(text="COMPUTER PLAYS AGAIN")
           
            while True:     
                CompMove = AllowedMoves
                maxReversed = 0
                #here we have the number of the allowed moves the computer has
                NumberOfCompsAllowed = len(CompMove)
                for i in range(NumberOfCompsAllowed):
                    x = CompMove[i][0]
                    y = CompMove[i][1]
                    reversedTiles = reverse_counts(x,y,board,player)
                    if reversedTiles > maxReversed:
                        maxReversed = reversedTiles
                        xMax = x                    #best moves x
                        yMax = y                    #best moves y
                break    
            
        
            boardAfterMove = add_checker(xMax,yMax,board,player)
            scoreAfterMove = score_computer(xMax,yMax,board)
            score.config(text=scoreAfterMove)
            new_board(boardAfterMove)       
            mes.config(text="HUMAN PLAYS")
        player = 1
        AllowedMoves = [] 
        for i in range(8):
            for j in range(8):
                if allowed_move(i, j, board, player):
                   checkForAllowed = True
                   AllowedMoves.append([i, j])
                   pouli.create_oval(15 + i * 50, 15 + j * 50, 35 + i * 50, 35 + j * 50, fill="gray")     
                   return
        else:
            mes.config(text="GAMEOVER!!!")
        return        
        

    
    
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# main program
board = create_board()
graphic_board()
human.bind("<Button-1>", human_play)
comp.bind("<Button-1>", computer_play)

root.mainloop()
