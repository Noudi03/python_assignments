'''Έστω μία σκακιέρα στην οποία τοποθετούμε πάνω της, σε τυχαίες θέσεις, έναν λευκό πύργο και αξιωματικό και μια μαύρη βασίλισσα.
Ο κάθε παίκτης παίρνει ως δυο βαθμούς σε κάθε γύρο ανάλογα με το αν τρώει κομμάτι του αντιπάλου.
Έτσι, ο λευκός μπορεί να πάρει 2 βαθμούς αν ο πύργος τρώει τη βασίλισσα και το ίδιο κάνει και ο αξιωματικός του.
Αν μόνο ένα από τα κομμάτια του τρώει τη βασίλισσα τότε παίρνει ένα βαθμό.
Αντίστοιχα, ο μαύρος παίρνει δύο βαθμούς αν η βασίλισσά του μπορεί να φάει και τα δύο κομμάτια του λευκού ή ένα αν μπορεί να φάει μόνο ένα.
Μετά από 100 παιχνίδια, εμφανίστε τους βαθμούς των δύο παικτών.'''
import random

def chess_game(size_x=8,size_y=8):
    
    #initialized the points of both players
    points_black = points_white = 0
    
    for i in range(100):
        

        position_bishop = position_rook = position_queen = []
        
        #assigning random values for the coordinates of the bishop, rook and queen
        #also,checking if they have the same position on the chessboard, if they do we assign the coords again.
        #this code block will be executed at least once
        while position_bishop == position_rook or position_queen == position_bishop or position_queen == position_rook:
            x1 = random.randint(1,size_x)
            y1 = random.randint(1,size_y)
            x2 = random.randint(1,size_x)
            y2 = random.randint(1,size_y)
            x3 = random.randint(1,size_x)
            y3 = random.randint(1,size_y)
            
            position_bishop=[x1,y1]
            position_rook=[x2,y2]
            position_queen=[x3,y3]
        
        #will be used later in order to not make more checks than needed  
        Triple_y = Triple_x = Triple_diag =False
        
        # if all the pieces are on the same line
        if position_queen[0] == position_rook[0] == position_bishop[0]:
            
            Triple_x = True
            
            #if the queen is on a lower or higher y axis than BOTH the rook and bishop and the bishop blocking the rook
            if position_queen[1] < position_bishop[1] < position_rook[1] or position_rook[1] < position_bishop[1] < position_queen[1]:
                points_black+=1

                
            #if the queen is on a lower or higher y axis than BOTH the rook and bishop and the rook blocking the bishop    
            elif position_queen[1] < position_rook[1] < position_bishop[1] or position_bishop[1] < position_rook[1] < position_queen[1]:
                points_black+=1
                points_white+=1

                
            #if the queen is the between 2 pieces
            else:
                points_black+=2
                points_white+=1

                
        # if all the pieces are on the same row
        elif position_queen[1] == position_rook[1] == position_bishop[1]:
            
            Triple_y = True
            
            #if the queen is on a lower or higher x axis than BOTH the rook and bishop and the bishop blocking the rook

            if position_queen[0] < position_bishop[0] < position_rook[0] or position_rook[0] < position_bishop[0] < position_queen[0]:
                points_black+=1

            #if the queen is on a lower or higher x axis than BOTH the rook and bishop and the rook blocking the bishop    
            elif position_queen[0] < position_rook[0] < position_bishop[0] or position_bishop[0] < position_rook[0] < position_queen[0]:
                points_black+=1
                points_white+=1

            #if the queen is the between 2 pieces
            else:
                points_black+=2
                points_white+=1


        #if the 2 pieces (queen and rook) are on the same y axis then BOTH get one point
        if (position_rook[1] == position_queen[1]) and not Triple_y:
            points_white+=1
            points_black+=1
    

        #if the 2 pieces (queen and rook) are on the same x axis then BOTH get one point
        if (position_rook[0] == position_queen[0]) and not Triple_x:
            points_white+=1
            points_black+=1

            
        #if the 2 pieces (bishop and queen) are in the same y axis,queen can take down the bishop
        if (position_bishop[1] == position_queen[1]) and not Triple_y :
            points_black+=1

            
        #if the 2 pieces (bishop and queen) are in the same y axis,queen can take down the bishop
        if (position_bishop[0] == position_queen[0]) and not Triple_x:
            points_black+=1

        
        
        


        #if the queen and the bishop are in the same diagonals, which means that the slope of their coords is 1 or -1, the pieces can take down each other
        #abs((position_bishop[1] - position_queen[1]) / (position_bishop[0] - position_queen[0])) == 1
        #is equal to the expresion abs(position_bishop[1] - position_queen[1] == abs(position_bishop[0] - position_queen[0]):
        
        if abs(position_bishop[1] - position_queen[1]) == abs(position_bishop[0] - position_queen[0]):
            
            #if the rook is in the same diagonal with the queen and the bishop
            if abs(position_rook[1] - position_queen[1]) == abs(position_rook[0] - position_queen[0]):

                Triple_diag = True
                
                #if the rook is in between the 2 pawns (in the "secondary" diagonals) 
                if ((position_bishop[0] < position_rook[0] < position_queen[0]) and (position_bishop[1] < position_rook[1] < position_queen[1])) or (
                    (position_queen[0] < position_rook[0] < position_bishop[0]) and (position_queen[1] < position_rook[1] < position_bishop[1])):
                    points_black+=1

                    
                #if the queen is on the same secondary diagonal with the other pieces and she is between them
                elif ((position_bishop[0] < position_queen[0] < position_rook[0]) and (position_bishop[1] < position_queen[1] < position_rook[1])) or (
                      (position_rook[0] < position_queen[0] < position_bishop[0]) and (position_rook[1] < position_queen[1] < position_bishop[1])):
                    points_black+=2
                    points_white+=1

                    
                #if the rook is in the same diagonal and between the 2 pawns (in the main diagonals)
                elif ((position_bishop[0] < position_rook[0] < position_queen[0]) and (position_bishop[1] > position_rook[1] > position_queen[1])) or (
                    (position_queen[0] < position_rook[0] < position_bishop[0]) and (position_queen[1] > position_rook[1] > position_bishop[1])):
                    points_black+=1
                    
                #if the queen is on the same main diagonal with the other pieces and she is between them
                elif ((position_bishop[0] < position_queen[0] < position_rook[0] and position_bishop[1] > position_queen[1] > position_rook[1])) or (
                   (position_rook[0] < position_queen[0] < position_bishop[0]) and (position_rook[1] > position_queen[1] > position_bishop[1])):
                    points_black+=2
                    points_white+=1

                    
            #if there are only 2 pieces on the diagonal, or the rook is not blocking the bishop
            else:
                points_black +=1
                points_white +=1
                
        #if the queen and the rook are in the same diagonals, the queen can take down the rook
        if abs(position_rook[1] - position_queen[1]) == abs(position_rook[0] - position_queen[0]) and not Triple_diag:
            points_black +=1

            
    return(points_white,points_black)

#!8x8 chess board
wp,bp =(chess_game())
print(f"white points: {wp} \nblack points: {bp}")