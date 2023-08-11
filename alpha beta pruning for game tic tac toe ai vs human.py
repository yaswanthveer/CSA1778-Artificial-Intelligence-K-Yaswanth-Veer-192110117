def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def alphabeta(board, depth, alpha, beta, is_maximizing):
    scores = {
        "X": 1,
        "O": -1,
        "draw": 0
    }

    if check_winner(board, "X"):
        return scores["X"]
    if check_winner(board, "O"):
        return scores["O"]
    if is_full(board):
        return scores["draw"]

    if is_maximizing:
        max_eval = -float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = alphabeta(board, depth + 1, alpha, beta, False)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = alphabeta(board, depth + 1, alpha, beta, True)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def find_best_move(board):
    best_eval = -float("inf")
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                eval = alphabeta(board, 0, -float("inf"), float("inf"), False)
                board[i][j] = " "
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)

    return best_move

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]

    while True:
        print_board(board)

        if is_full(board) or check_winner(board, "X") or check_winner(board, "O"):
            break

        player_row = int(input("Enter row (0-2): "))
        player_col = int(input("Enter column (0-2): "))

        if board[player_row][player_col] != " ":
            print("That cell is already occupied. Try again.")
            continue

        board[player_row][player_col] = "O"

        if is_full(board) or check_winner(board, "X") or check_winner(board, "O"):
            break

        print("AI's Turn:")
        ai_row, ai_col = find_best_move(board)
        board[ai_row][ai_col] = "X"

    print_board(board)

    if check_winner(board, "X"):
        print("AI wins!")
    elif check_winner(board, "O"):
        print("Player wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    tic_tac_toe()
