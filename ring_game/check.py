def duplicate(value, block):
    '''takes the position and size of the ring and checks
    if the move can be played. If there is no ring of the current size
    in the block, the ring will be placed'''
    if block == "0":
        return False
    elif value in block:
        return True
    return False

def row(board):
    '''checking if there is a winning pair in any of the rows'''
    for i in range(0,9,3):
        
        #if a row has a pair of 3 rings (of any size)
        if board[i:i+4].count("s") == 3 or board[i:i+4].count("m") == 3 or board[i:i+4].count("l") == 3:
            return True
        
        #if a row has an increasing or decreasing sequence of rings
        if ("s" in board[i] or "l" in board[i]) and "m" in board[i+1] and ("s" in board[i+2] or "l" in board[i+2]):
            return True
        
    #if there are no pairs in any rows
    return False
        
        
def column(board):
    '''checking if there is a winning pair in any of the columns'''
    for i in range(3):
        
        #if a column has an increasing or decreasing sequence of rings
        
        if ("s" in board[i] or "l" in board[i]) and "m" in board[i+3] and ("s" in board[i+6] or "l" in board[i+6]):
            return True
        
        #if a column has a pair of 3 rings (of any size)
        ctr_small = ctr_med = ctr_large = 0
        
        for j in range(i,i+7,3):
            if "s" in board[j]:
                ctr_small +=1
            if "m" in board[j]:
                ctr_med +=1
            if "l" in board[j]:
                ctr_large +=1
                
        if ctr_small == 3 or ctr_med == 3 or ctr_large == 3:
            return True
        
    #if there are no pairs in any columns
    return False
    

def diagonal(board):
    '''checking if there are pairs of 3, or sequences in the "diagonals"'''
    
    #if there is a sequence in the main diagonal
    pos = 0
    if ("s" in board[pos] or "l" in board[pos]) and "m" in board[pos+4] and ("s" in board[pos+8] or "l" in board[pos+8]):
        return True
    
    #if there is a pair of 3 in the main diagonal
    ctr_small = ctr_med = ctr_large = 0
    for i in range(0,9,4):
        if "s" in board[i]:
            ctr_small +=1
        if "m" in board[i]:
            ctr_med +=1
        if "l" in board[i]:
            ctr_large +=1
            
    if ctr_small == 3 or ctr_med == 3 or ctr_large == 3:
        return True
    
    #if there is a sequence in the secondary diagonal
    pos = 2
    if ("s" in board[pos] or "l" in board[pos]) and "m" in board[pos+2] and ("s" in board[pos+4] or "l" in board[pos+4]):
        return True
    
    #if there is a pair of 3 in the secondary diagonal
    ctr_small = ctr_med = ctr_large = 0
    for i in range(2,7,2):
        if "s" in board[i]:
            ctr_small +=1
        if "m" in board[i]:
            ctr_med +=1
        if "l" in board[i]:
            ctr_large +=1
            
    if ctr_small == 3 or ctr_med == 3 or ctr_large == 3:
        return True
    #if there are no pairs in diagonals
    return False