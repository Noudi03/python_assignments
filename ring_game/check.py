def check_win_condition(board):
    patterns = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
                (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
                (0, 4, 8), (2, 4, 6)]  # diagonals

    for a, b, c in patterns:
        if board[a] == board[b] == board[c] and board[a] != "0":
            return True

        # Check for increasing size sequence
        if all(size in board[cell] for size, cell in zip("sml", sorted([a, b, c]))):
            return True

    return False
