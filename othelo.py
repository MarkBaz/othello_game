# for deepcopy purposes
import copy


def create_board():
    board = [[0 for i in range(8)] for j in range(8)]
    board[3][3] = 2
    board[4][4] = 1
    board[3][4] = 2
    board[4][3] = 2
    board[3][5] = 2
    board[3][2] = 2
    board[3][1] = 0
    board[3][6] = 2
    board[5][3] = 2
    board[2][3] = 1
    board[5][4] = 2
    board[6][5] = 1
    board[4][2] = 2
    board[5][1] = 2
    board[6][0] = 1
    board[4][6] = 1
    board[5][0] = 1
    board[2][2] = 2
    board[5][5] = 2
    board[0][7] = 1
    board[1][6] = 2
    board[2][5] = 2
    board[5][6] = 2
    board[5][7] = 1
    board[6][2] = 2
    board[7][2] = 1
    board[1][2] = 2
    board[0][2] = 1
    board[6][3] = 2
    board[7][4] = 1
    board[6][1] = 2
    board[7][0] = 1

    return board


def print_board(board):
    print('    0   1   2   3   4   5   6   7')
    for y in range(8):
        print((y), end=' ')
        for x in range(8):
            print(('| %s' % board[x][y]), end=' ')
        print('|')


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
        if board[x - 1][y]:
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
    x = x - 1
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
        while (y >= 0):
            if board[x][y] == this_player:
                return True
            if board[x][y] == 0:
                return False
            x = x - 1
            y = y - 1
        return False
    else:
        while (x >= 0):
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
    if (x < y):
        while (x >= 0):
            if board[x][y] == this_player:
                return True
            if board[x][y] == 0:
                return False
            x = x - 1
            y = y + 1
        return False
    else:
        while (y <= 7):
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
        while (x <= 7):
            if board[x][y] == this_player:
                return True
            if board[x][y] == 0:
                return False
            x = x + 1
            y = y + 1
        return False
    else:
        while (y <= 7):
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
        while (y <= 7):
            if board[x][y] == this_player:
                return True
            if board[x][y] == 0:
                return False
            x = x + 1
            y = y - 1
        return False
    else:
        while (x >= 0):
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
        if board[x - 1][y]:
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
        while (y >= 0):
            counter = counter + 1
            if board[x][y] == this_player:
                return counter - 1
            if board[x][y] == 0:
                return 0
            x = x - 1
            y = y - 1
        return 0
    else:
        while (x >= 0):
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
    if (x < y):
        while (x >= 0):
            counter = counter + 1
            if board[x][y] == this_player:
                return counter - 1
            if board[x][y] == 0:
                return 0
            x = x - 1
            y = y + 1
        return 0
    else:
        while (y <= 7):
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
        while (x <= 7):
            counter = counter + 1
            if board[x][y] == this_player:
                return counter - 1
            if board[x][y] == 0:
                return 0
            x = x + 1
            y = y + 1
        return 0
    else:
        while (y <= 7):
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
        while (y <= 7):
            counter = counter + 1
            if board[x][y] == this_player:
                return counter - 1
            if board[x][y] == 0:
                return 0
            x = x + 1
            y = y - 1
        return 0
    else:
        while (x >= 0):
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
        if board[x - 1][y]:
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
        computed_board[x][y] = 1
        y = y - 1
    return board_old


def check_down_computed(x, y, board, this_player, computed_board):
    board_old = copy.deepcopy(computed_board)
    y = y + 1
    while (y <= 7):
        if board[x][y] == this_player:
            return computed_board
        if board[x][y] == 0:
            print('ok')
            return board_old
        computed_board[x][y] = 1
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
        computed_board[x][y] = 1
        x = x - 1
    return 0


def check_right_computed(x, y, board, this_player, computed_board):
    board_old = copy.deepcopy(computed_board)
    x = x + 1
    while (x <= 7):
        if board[x][y] == this_player:
            return computed_board
        if board[x][y] == 0:
            return board_old
        computed_board[x][y] = 1
        x = x + 1
    return board_old


def check_up_left_computed(x, y, board, this_player, computed_board):
    board_old = copy.deepcopy(computed_board)
    x = x - 1
    y = y - 1
    if (x > y):
        while (y >= 0):
            if board[x][y] == this_player:
                return computed_board
            if board[x][y] == 0:
                return board_old
            computed_board[x][y] = 1
            x = x - 1
            y = y - 1
        return board_old
    else:
        while (x >= 0):
            if board[x][y] == this_player:
                return computed_board
            if board[x][y] == 0:
                return board_old
            computed_board[x][y] = 1
            x = x - 1
            y = y - 1
        return board_old


def check_down_left_computed(x, y, board, this_player, computed_board):
    board_old = copy.deepcopy(computed_board)
    x = x - 1
    y = y + 1
    if (x < y):
        while (x >= 0):
            if board[x][y] == this_player:
                return computed_board
            if board[x][y] == 0:
                return board_old
            computed_board[x][y] = 1
            x = x - 1
            y = y + 1
        return board_old
    else:
        while (y <= 7):
            if board[x][y] == this_player:
                return computed_board
            if board[x][y] == 0:
                return board_old
            computed_board[x][y] = 1
            x = x - 1
            y = y + 1
        return board_old


def check_down_right_computed(x, y, board, this_player, computed_board):
    board_old = copy.deepcopy(computed_board)
    x = x + 1
    y = y + 1
    if (x > y):
        while (x <= 7):
            if board[x][y] == this_player:
                return computed_board
            if board[x][y] == 0:
                return board_old
            computed_board[x][y] = 1
            x = x + 1
            y = y + 1
        return board_old
    else:
        while (y <= 7):
            if board[x][y] == this_player:
                return computed_board
            if board[x][y] == 0:
                return board_old
            computed_board[x][y] = 1
            x = x + 1
            y = y + 1
        return board_old


def check_up_right_computed(x, y, board, this_player, computed_board):
    board_old = copy.deepcopy(computed_board)
    x = x + 1
    y = y - 1
    if (x > y):
        while (y <= 7):
            if board[x][y] == this_player:
                return computed_board
            if board[x][y] == 0:
                return board_old
            computed_board[x][y] = 1
            x = x + 1
            y = y - 1
        return board_old
    else:
        while (x >= 0):
            if board[x][y] == this_player:
                return computed_board
            if board[x][y] == 0:
                return board_old
            computed_board[x][y] = 1
            x = x + 1
            y = y - 1
        return board_old


def add_checker(x, y, board, player):
    board_computed = compute_counts(x, y, board, player)
    print_board(board_computed)
    for y in range(8):
        for x in range(8):
            if board_computed[x][y] == 1:
                board[x][y] = player
    return board


def human_play(board, player):
    print('\nBoard after move')
    checkForAllowed = False
    print_board(board)
    for y in range(8):
        for x in range(8):
            if allowed_move(x, y, board, player):
                print('allowed move x=', x, ' y=', y)
                checkForAllowed = True
                # end if
                # end for x
    # end for y






    if (not checkForAllowed):
        return False
    # human play started

    return true


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# main program
board = create_board()
print_board(board)

board = add_checker(5, 2, board, 1)
if human_play(board, 1):
    print('ola good')







