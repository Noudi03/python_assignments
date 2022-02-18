'''Έστω μία σκακιέρα 8*8 στην οποία τοποθετούμε πάνω της, σε τυχαίες θέσεις, έναν λευκό πύργο και ένα μαύρο αξιωματικό.
Σε κάθε γύρο, ο κάθε παίκτης παίρνει ένα βαθμό αν το κομμάτι του τρώει κομμάτι του αντιπάλου.
Μετά από 100 παιχνίδια, εμφανίστε τους βαθμούς των δύο παικτών.
Επαναλάβετε το πείραμα 100 φορές για σκακιέρες 7*7 και 7*8 και εμφανίστε τους αντίστοιχους βαθμούς των παικτών.'''
import random

def chess_game(size_x=8,size_y=8):
    #initialized the points of both players
    points_black = points_white = 0
    
    for i in range(100):
        

        position_bishop = position_rook = []
        
        #assigning random values for the coordinates of the bishop and rook
        #also,checking if they have the same position on the chessboard, if they do we assign the coords again.
        #this code block will be executed at least once
        while position_bishop == position_rook:
            x1 = random.randint(1,size_x)
            y1 = random.randint(1,size_y)
            x2 = random.randint(1,size_x)
            y2 = random.randint(1,size_y)
            position_bishop=[x1,y1]
            position_rook=[x2,y2]   

        #if the 2 pieces are in the same x or y axis, the rook can take down the pawn
        if position_bishop[1] == position_rook[1] or position_bishop[0] == position_rook[0]:
            points_white+=1
        #if the rook and the bishop are in the same diagonals, which meansa that if the slope of their coords is 1 or -1, the bishop can take down the pawn
        elif abs((position_bishop[1] - position_rook[1]) / (position_bishop[0] - position_rook[0])) == 1:
            points_black +=1 

    print(f"{size_x} * {size_y} chessboard")
    return(points_white,points_black)

#!8x8 chess board
wp, bp = chess_game()
print(f"white points: {wp} \nblack points: {bp}")
#!8x7 chess board
wp, pb = chess_game(8,7)
print(f"white points: {wp} \nblack points: {bp}")
#!7x7 chess board
wp, bp = chess_game(7,7)
print(f"white points: {wp} \nblack points: {bp}")