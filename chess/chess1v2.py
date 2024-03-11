'''Έστω μία σκακιέρα στην οποία τοποθετούμε πάνω της, σε τυχαίες θέσεις, έναν λευκό πύργο και αξιωματικό και μια μαύρη βασίλισσα.
Ο κάθε παίκτης παίρνει ως δυο βαθμούς σε κάθε γύρο ανάλογα με το αν τρώει κομμάτι του αντιπάλου.
Έτσι, ο λευκός μπορεί να πάρει 2 βαθμούς αν ο πύργος τρώει τη βασίλισσα και το ίδιο κάνει και ο αξιωματικός του.
Αν μόνο ένα από τα κομμάτια του τρώει τη βασίλισσα τότε παίρνει ένα βαθμό.
Αντίστοιχα, ο μαύρος παίρνει δύο βαθμούς αν η βασίλισσά του μπορεί να φάει και τα δύο κομμάτια του λευκού ή ένα αν μπορεί να φάει μόνο ένα.
Μετά από 100 παιχνίδια, εμφανίστε τους βαθμούς των δύο παικτών.'''
import random


def is_same_line_or_row(pos1, pos2):
    """checking if two pieces are on the same line or row."""
    return pos1[0] == pos2[0] or pos1[1] == pos2[1]


def is_diagonal(pos1, pos2):
    """checking if two pieces are diagonal to each other."""
    return abs(pos1[0] - pos2[0]) == abs(pos1[1] - pos2[1])


def chess_game(num_games=100, board_size=(8, 8)):
    points_white, points_black = 0, 0

    for _ in range(num_games):
        # generating 3 random positions
        positions = random.sample([(x, y) for x in range(
            1, board_size[0]+1) for y in range(1, board_size[1]+1)], 3)
        # assigning the positions to the pieces
        pos_bishop, pos_rook, pos_queen = positions

        # checking for attacks
        if is_same_line_or_row(pos_rook, pos_queen) or is_diagonal(pos_rook, pos_queen):
            points_white += 1
            points_black += 1

        if is_same_line_or_row(pos_bishop, pos_queen) or is_diagonal(pos_bishop, pos_queen):
            points_white += 1
            points_black += 1

        # adjusting for queen attacking both pieces
        if (is_same_line_or_row(pos_queen, pos_rook) and is_same_line_or_row(pos_queen, pos_bishop)) or \
           (is_diagonal(pos_queen, pos_rook) and is_diagonal(pos_queen, pos_bishop)):
            points_black += 1  # additional point for queen attacking both

    return points_white, points_black


#!8x8 chess board
wp, bp = (chess_game())
print(f"white points: {wp} \nblack points: {bp}")
