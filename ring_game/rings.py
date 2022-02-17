'''Έστω ένα τετράγωνο 3*3 στο οποίο τοποθετείτε δακτυλίους.
Έχετε στην κατοχή σας 27 δακτυλίους, 9 για κάθε μέγεθος (μικρό, μεσαίο, μεγάλο).
Μια τριάδα που τερματίζει το παιχνίδι γίνεται οριζόντια, κάθετα ή διαγώνια. 
Η τριάδα αποτελείται από δακτυλίους είτε του ίδιου μεγέθους είτε από το μικρό προς το μεγαλύτερο.
Επειδή έχετε δακτυλίους, ένας δακτύλιος μπορεί να μπει σε οποιοδήποτε τετράγωνο,
αρκεί να μην έχει ήδη δακτύλιο του ίδιου μεγέθους. 
Γράψτε ένα πρόγραμμα το οποίο παίζει τυχαία το παιχνίδι 100 φορές και επιστρέφει το μέσο όρο των βημάτων για να λήξει το παιχνίδι.'''

import random
import check

#initializing a list with 9 cells that will represent the board

game_board = ["0"] * 9

#initializing the moves_counter will increment every time a move is finished
moves_counter = 0

#initializing the sum of all total moves of the whole game that will be used to calculate the avg moves per game
sum = 0

#game has to be played 100 times
game_count = 100
for i in range(game_count):
    
    move = True
    while move:
        #generating a random index for the list to insert into the list
        index = random.randint(0,8)

        sizes = ["s","m","l"]
        #picking a random size to insert to the list
        value = random.choice(sizes)

        #here we will check if the ring we are trying to place on the board has been placed in a previous move
        
        duplicate = check.duplicate(value, game_board[index])
        
        #if the move we are doing is valid, we will place the ring on the board
        
        if not duplicate:
            if game_board[index] == "0":
                game_board[index] = value
            else:
                game_board[index] += value
            moves_counter+=1
        
        #checking if there is a winning pair (after the first 3 moves, no pair of 3 can be formed before them)
        if moves_counter >=3:
            
            #calling the functions from the check file to determine if the game can end
            if check.row(game_board) or check.column(game_board) or check.diagonal(game_board):
                move = False
                sum += moves_counter
                #resetting the board and move_counter for the next game
                moves_counter = 0
                game_board = ["0"] * 9

print("the average moves to end the game are: ",sum/game_count)