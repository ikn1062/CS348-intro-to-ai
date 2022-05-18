import common


def minmax_tictactoe(board, turn):
    """
    TIC-TAC-TOE solver capable of predicting the result of a specific game when a board is provided
    Min Max Method
    :param board: an array of 9 (from 0 to 8) integers representing the squares of the tic tac toe board
    :param turn: number indicating which player moves next (1 for X, 2 for O)
    :return: returns an integer representing the winner of the game under optimal play, 1 for X, 2 for O and 0 for tie

    # put your code here:
    # it must return common.constants.X(1), common.constants.O(2) or common.constants.NONE(0) for tie.
    # use the function common.game_status(board), to evaluate a board
    # it returns common.constants.X(1) if X wins, common.constants.O(2) if O wins or common.constants.NONE(0) if tie
    # or game is not finished
    # the program will keep track of the number of boards evaluated
    # result = common.game_status(board);
    """
    game = minmax(board, turn)
    if game == -1:
        game = 2
    return game


def abprun_tictactoe(board, turn):
    """
    TIC-TAC-TOE solver capable of predicting the result of a specific game when a board is provided
    alpha beta pruning method
    :param board: an array of 9 (from 0 to 8) integers representing the squares of the tic tac toe board
    :param turn: number indicating which player moves next (1 for X, 2 for O)
    :param a: max - alpha
    :param b: min - beta
    :return: returns an integer representing the winner of the game under optimal play, 1 for X, 2 for O and 0 for tie

    # put your code here:
    # it must return common.constants.X(1), common.constants.O(2) or common.constants.NONE(0) for tie.
    # use the function common.game_status(board), to evaluate a board
    # it returns common.constants.X(1) if X wins, common.constants.O(2) if O wins or common.constants.NONE(0) if tie or
    # game is not finished
    # the program will keep track of the number of boards evaluated
    # result = common.game_status(board);
    """
    # Check if the game is over
    game = prune(board, turn, -10000, 10000)
    if game == -1:
        game = 2
    return game


def prune(board, turn, a, b):
    board_status = common.game_status(board)
    if board_status != 0 or (0 not in board):
        if board_status == 2:
            return -1
        else:
            return board_status

    empty_pos = []
    for i in range(len(board)):
        if board[i] == 0:
            empty_pos.append(i)

    if turn == 1:
        val = -10000
        for i in empty_pos:
            board[i] = turn
            temp_val = prune(board, 2, a, b)
            if temp_val > val:
                val = temp_val
            board[i] = 0
            if val >= b:
                return val
            if val > a:
                a = val
        return val

    if turn == 2:
        val = 10000
        for i in empty_pos:
            board[i] = turn
            temp_val = prune(board, 1, a, b)
            if temp_val < val:
                val = temp_val
            board[i] = 0
            if val <= a:
                return val
            if val < b:
                b = val
        return val


def minmax(board, turn):
    board_status = common.game_status(board)
    if board_status != 0 or (0 not in board):
        if board_status == 2:
            return -1
        else:
            return board_status

    empty_pos = []
    for i in range(len(board)):
        if board[i] == 0:
            empty_pos.append(i)

    if turn == 1:
        val = -10000
        for i in empty_pos:
            board[i] = turn
            temp_val = minmax(board, 2)
            if temp_val > val:
                val = temp_val
            board[i] = 0
        return val

    if turn == 2:
        val = 10000
        for i in empty_pos:
            board[i] = turn
            temp_val = minmax(board, 1)
            if temp_val < val:
                val = temp_val
            board[i] = 0
        return val
