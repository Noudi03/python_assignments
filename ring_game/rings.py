'''Έστω ένα τετράγωνο 3*3 στο οποίο τοποθετείτε δακτυλίους.
Έχετε στην κατοχή σας 27 δακτυλίους, 9 για κάθε μέγεθος (μικρό, μεσαίο, μεγάλο).
Μια τριάδα που τερματίζει το παιχνίδι γίνεται οριζόντια, κάθετα ή διαγώνια. 
Η τριάδα αποτελείται από δακτυλίους είτε του ίδιου μεγέθους είτε από το μικρό προς το μεγαλύτερο.
Επειδή έχετε δακτυλίους, ένας δακτύλιος μπορεί να μπει σε οποιοδήποτε τετράγωνο,
αρκεί να μην έχει ήδη δακτύλιο του ίδιου μεγέθους. 
Γράψτε ένα πρόγραμμα το οποίο παίζει τυχαία το παιχνίδι 100 φορές και επιστρέφει το μέσο όρο των βημάτων για να λήξει το παιχνίδι.'''

import random
import check


def simulate_game():
    # using empty strings to indicate no rings
    game_board = [""] * 9
    moves_counter = 0
    while True:
        index = random.randint(0, 8)
        value = random.choice(["s", "m", "l"])
        # check if the ring size already exists in the cell to prevent duplicates
        if value not in game_board[index]:
            game_board[index] += value
            moves_counter += 1
            # earliest win possible is after 5 moves
            if moves_counter >= 5:
                if check.check_win_condition(game_board):
                    break
    return moves_counter


def simulate_games(n=100):
    total_moves = sum(simulate_game() for _ in range(n))
    return total_moves / n


average_moves = simulate_games(100)
print(f"the average moves to end the game are: {average_moves}")
