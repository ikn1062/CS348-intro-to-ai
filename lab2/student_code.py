QUEENS = 10


def gradient_search(board):
    current_queens = make_queens(board)
    while True:
        best_board = find_best_board(current_queens)
        best_queens = make_queens(best_board)
        if count_attack(current_queens) == count_attack(best_queens):
            break
        current_queens = make_queens(best_board)
        copy_board(board, current_queens)
    if count_attack(current_queens) == 0:
        return True
    return False


def make_queens(board):
    queens = []
    for j in range(QUEENS):
        for i in range(QUEENS):
            if board[j][i] == 1:
                queens.append([j, i])
    return queens


def make_board(queens):
    board = [[0 for i in range(QUEENS)] for j in range(QUEENS)]
    for queen in queens:
        j, i = queen[0], queen[1]
        board[j][i] = 1
    return board


def find_best_board(queens):
    min_attack = 100
    best_queens = copy_list(queens)
    queens_c = copy_list(queens)

    for i in range(len(queens_c)):
        queen = queens_c[i]
        for row in range(QUEENS):
            queen[0] = row
            curr_attack = count_attack(queens_c)
            if curr_attack < min_attack:
                best_queens = copy_list(queens_c)
                min_attack = curr_attack
                q_best_y, q_best_x = queen[0], queen[1]
            if curr_attack == min_attack:
                if queen[1] < q_best_x:
                    best_queens = copy_list(queens_c)
                    min_attack = curr_attack
                    q_best_y, q_best_x = queen[0], queen[1]
                elif queen[1] == q_best_x:
                    if queen[0] < q_best_y:
                        best_queens = copy_list(queens_c)
                        min_attack = curr_attack
                        q_best_y, q_best_x = queen[0], queen[1]
        queens_c = copy_list(queens)
    best_board = make_board(best_queens)
    return best_board


def copy_list(lists):
    list_return = []
    for l in lists:
        list_return.append([l[0], l[1]])
    return list_return


def count_attack(queens):
    attacks = 0
    queens_list = copy_list(queens)

    for i in range(len(queens_list)):
        queen = queens_list.pop()
        y, x = queen[0], queen[1]
        attack_board = [[0 for i in range(QUEENS)] for j in range(QUEENS)]

        for ix in range(QUEENS):
            attack_board[y][ix] = 1

        i1, j1 = queen[1], queen[0]
        while (j1 < QUEENS) and (i1 < QUEENS):
            attack_board[j1][i1] = 1
            i1 = i1 + 1
            j1 = j1 + 1
        i2, j2 = queen[1], queen[0]
        while (j2 >= 0) and (i2 >= 0):
            attack_board[j2][i2] = 1
            i2 = i2 - 1
            j2 = j2 - 1
        i3, j3 = queen[1], queen[0]
        while (j3 < QUEENS) and (i3 >= 0):
            attack_board[j3][i3] = 1
            i3 = i3 - 1
            j3 = j3 + 1
        i4, j4 = queen[1], queen[0]
        while (j4 >= 0) and (i4 < QUEENS):
            attack_board[j4][i4] = 1
            i4 = i4 + 1
            j4 = j4 - 1

        for q_attack in queens_list:
            qy, qx = q_attack[0], q_attack[1]
            if attack_board[qy][qx] == 1:
                attacks = attacks + 1
    return attacks


def copy_board(board, queens):
    for j in range(QUEENS):
        for i in range(QUEENS):
            board[j][i] = 0
    for queen in queens:
        j, i = queen[0], queen[1]
        board[j][i] = 1
    return 0
