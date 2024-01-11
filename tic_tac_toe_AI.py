import random

def print_board(board):
    print("---------")
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(board[i][j], end="|")
        print("\n---------")

def is_winner(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def is_board_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True

def get_empty_cells(board):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                empty_cells.append((i, j))
    return empty_cells

def make_move(board, player, row, col):
    board[row][col] = player

def minimax(board, depth, maximizing_player):
    if is_winner(board, "X"):
        return -1
    elif is_winner(board, "O"):
        return 1
    elif is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = float("-inf")
        for cell in get_empty_cells(board):
            row, col = cell
            board[row][col] = "O"
            eval = minimax(board, depth + 1, False)
            board[row][col] = " "
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for cell in get_empty_cells(board):
            row, col = cell
            board[row][col] = "X"
            eval = minimax(board, depth + 1, True)
            board[row][col] = " "
            min_eval = min(min_eval, eval)
        return min_eval

def get_best_move(board):
    best_eval = float("-inf")
    best_move = None
    for cell in get_empty_cells(board):
        row, col = cell
        board[row][col] = "O"
        eval = minimax(board, 0, False)
        board[row][col] = " "
        if eval > best_eval:
            best_eval = eval
            best_move = cell
    return best_move

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    while True:
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))
        if board[row][col] != " ":
            print("Invalid move. Try again.")
            continue
        make_move(board, "X", row, col)
        if is_winner(board, "X"):
            print("You win!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break
        print("AI is thinking...")
        ai_row, ai_col = get_best_move(board)
        make_move(board, "O", ai_row, ai_col)
        print_board(board)
        if is_winner(board, "O"):
            print("AI wins!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break

play_game()
