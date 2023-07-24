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

players = {'black': 
              {'pieces': 
                  {'pawns': 
                      {'bpawn-1': {'position': 'h7', 'taken': False},
                      'bpawn-2':  {'position': 'g7', 'taken': False},
                      'bpawn-3':  {'position': 'cf', 'taken': False},
                      'bpawn-4':  {'position': 'e7', 'taken': False},
                      'bpawn-5':  {'position': 'd7', 'taken': False},
                      'bpawn-6':  {'position': 'c7', 'taken': False},
                      'bpawn-7':  {'position': 'b7', 'taken': False},
                      'bpawn-8':  {'position': 'a7', 'taken': False}},
                  'rooks': 
                      {'brook-1': {'position': 'h8', 'taken': False}, 
                      'brook-2':  {'position': 'a8', 'taken': False}},
                  'knights': 
                      {'bknight-1':{'position': 'g8', 'taken': False},
                      'bknight-2': {'position': 'b8', 'taken': False}},
                  'bishops': 
                      {'bbishop-1':{'position': 'f8', 'taken': False}, 
                      'bbishop-2': {'position': 'c8', 'taken': False}},
                  'queen-king': 
                      {'bqueen': {'position': 'd8', 'taken': False},
                      'bking':   {'position': 'e8', 'taken': False}}
                  },
                  'piecesLeft': 16,
                  'checkMate': False
              },
          'white': 
              {'pieces': 
                  {'pawns': 
                      {'wpawn-1': {'position': 'a2', 'taken': False}, 
                      'wpawn-2':  {'position': 'b2', 'taken': False},
                      'wpawn-3':  {'position': 'c2', 'taken': False},
                      'wpawn-4':  {'position': 'd2', 'taken': False}, 
                      'wpawn-5':  {'position': 'e2', 'taken': False},
                      'wpawn-6':  {'position': 'f2', 'taken': False},
                      'wpawn-7':  {'position': 'g2', 'taken': False},
                      'wpawn-8':  {'position': 'h2', 'taken': False}},
                  'rooks': 
                      {'wrook-1': {'position': 'a1', 'taken': False}, 
                      'wrook-2':  {'position': 'h1', 'taken': False}},
                  'knights': 
                      {'wknight-1': {'position': 'b1', 'taken': False}, 
                      'wknight-2':  {'position': 'g1', 'taken': False}},
                  'bishops': 
                      {'wbishop-1': {'position': 'c1', 'taken': False}, 
                      'wbishop-2':  {'position': 'f1', 'taken': False}},
                  'queen-king': 
                      {'wqueen': {'position': 'd1', 'taken': False},
                      'wking':   {'position': 'e1', 'taken': False}}
                  },
                  'piecesLeft': 16,
                  'checkMate': False
              }
          }

theBoard = {
    
}


def isValidChessBoard(board):
    print(board)