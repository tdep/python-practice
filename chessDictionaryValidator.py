"""
Write a function named isValidChessBoard() that takes a dictionary argument 
and returns True or False depending on if the board is valid.

A valid board will have exactly one black king and exactly one white kings. 
Each player can only have at most 16 pieces, at most 8 pawns, and all pieces 
must be on a valid space from '1a' to '8h'; that is, a piece can't be on space
'9z'. The piece names begin with either a 'w' or 'b' to represent white or black,
followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'. This function
should detect when a bug has resulted in an improper chess board.
"""



def isValidChessBoard(board):
    print(board)