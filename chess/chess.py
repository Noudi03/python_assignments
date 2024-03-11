'''Έστω μία σκακιέρα 8*8 στην οποία τοποθετούμε πάνω της, σε τυχαίες θέσεις, έναν λευκό πύργο και ένα μαύρο αξιωματικό.
Σε κάθε γύρο, ο κάθε παίκτης παίρνει ένα βαθμό αν το κομμάτι του τρώει κομμάτι του αντιπάλου.
Μετά από 100 παιχνίδια, εμφανίστε τους βαθμούς των δύο παικτών.
Επαναλάβετε το πείραμα 100 φορές για σκακιέρες 7*7 και 7*8 και εμφανίστε τους αντίστοιχους βαθμούς των παικτών.'''
import random


def is_on_same_line_or_column(pos1, pos2):
    """checking if two pieces are on the same line or column."""
    return pos1[0] == pos2[0] or pos1[1] == pos2[1]


def is_on_same_diagonal(pos1, pos2):
    """checking if two pieces are on the same diagonal."""
    return abs(pos1[0] - pos2[0]) == abs(pos1[1] - pos2[1])


def chess_game(size_x=8, size_y=8, rounds=100):
    points_white = 0  # points for the player with the rook
    points_black = 0  # points for the player with the bishop

    for _ in range(rounds):
        # generating unique positions for the rook and bishop
        positions = random.sample(
            [(x, y) for x in range(size_x) for y in range(size_y)], 2)
        position_rook, position_bishop = positions

        # rook captures bishop if they are on the same line or column
        if is_on_same_line_or_column(position_rook, position_bishop):
            points_white += 1

        # bishop captures rook if they are on the same diagonal
        if is_on_same_diagonal(position_rook, position_bishop):
            points_black += 1

    print(f"{size_x}x{size_y} chessboard: ")
    return points_white, points_black


#!8x8 chess board
wp, bp = chess_game()
print(f"white points: {wp} \nblack points: {bp}")
#!8x7 chess board
wp, pb = chess_game(8, 7)
print(f"white points: {wp} \nblack points: {bp}")
#!7x7 chess board
wp, bp = chess_game(7, 7)
print(f"white points: {wp} \nblack points: {bp}")
