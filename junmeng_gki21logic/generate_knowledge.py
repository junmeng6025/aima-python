import numpy as np
from field_var import *

def generate_knowledge(chessboard_array):
    """
    Initialize the knowledge base, by adding statements describing
    the initial state of the chessboard, as well as the rules concerning the
    danger fields.
    
    You can use the functions Queen(x,y), Pawn(x,y), and Danger(x,y) to
    produce the statements Qxy, Pxy, and Dxy, if x and y are integers.
    
    Input: np.ndarray 2-D array, where each field
            contains either 'Q', 'P', 'D' or '0'
            
    Output: A list kb of logical sentences that will be added to
             the knowledge base
    """
    
    chessboard_size = len(chessboard_array)
    kb = []
                
    all_fields = [(x,y) for x in range(chessboard_size) for y in range(chessboard_size)]
    
    for field in all_fields:
        x = field[0]
        y = field[1]
        if chessboard_array[x, y] == 'Q':
            kb.append(Queen(x, y))
        if chessboard_array[x, y] == 'P':
            kb.append(Pawn(x, y))

    # check along x+        
    for field in all_fields:
        x = field[0]
        y = field[1]
        i = 1
        while Pawn(x + i, y) not in kb and x + i < chessboard_size:
            sentence = Queen(x, y) + '==>' + Danger(x + i, y)
            kb.append(sentence)
            i += 1
    # check along x-        
    for field in all_fields:
        x = field[0]
        y = field[1]
        i = 1
        while Pawn(x - i, y) not in kb and x - i >= 0:
            sentence = Queen(x, y) + '==>' + Danger(x - i, y)
            kb.append(sentence)
            i += 1
    # check along y+        
    for field in all_fields:
        x = field[0]
        y = field[1]
        i = 1
        while Pawn(x, y + i) not in kb and y + i < chessboard_size:
            sentence = Queen(x, y) + '==>' + Danger(x, y + i)
            kb.append(sentence)
            i += 1
    # check along y-        
    for field in all_fields:
        x = field[0]
        y = field[1]
        i = 1
        while Pawn(x, y - i) not in kb and y - i >= 0:
            sentence = Queen(x, y) + '==>' + Danger(x, y - i)
            kb.append(sentence)
            i += 1
    # check along diag++        
    for field in all_fields:
        x = field[0]
        y = field[1]
        i = 1
        while Pawn(x + i, y + i) not in kb and x + i < chessboard_size and y + i < chessboard_size:
            sentence = Queen(x, y) + '==>' + Danger(x + i, y + i)
            kb.append(sentence)
            i += 1
    # check along diag--        
    for field in all_fields:
        x = field[0]
        y = field[1]
        i = 1
        while Pawn(x - i, y - i) not in kb and x - i >= 0 and y - i >= 0:
            sentence = Queen(x, y) + '==>' + Danger(x - i, y - i)
            kb.append(sentence)
            i += 1
    # check along codiag+-        
    for field in all_fields:
        x = field[0]
        y = field[1]
        u = 1
        d = 1
        while Pawn(x + u, y - d) not in kb and x + u < chessboard_size and y - d >= 0:
            sentence = Queen(x, y) + '==>' + Danger(x + u, y - d)
            kb.append(sentence)
            u += 1
            d += 1
    # check along codiag-+        
    for field in all_fields:
        x = field[0]
        y = field[1]
        u = 1
        d = 1
        while Pawn(x - d, y + u) not in kb and y + u < chessboard_size and x - d >= 0:
            sentence = Queen(x, y) + '==>' + Danger(x - d, y + u)
            kb.append(sentence)
            u += 1
            d += 1
   
    return kb

    