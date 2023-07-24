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

cheesers = [[' //==  ||  ||  ||===  ||===   //==  ||===  ||==     //=='],
            ['||     ||  ||  ||     ||     ||     ||     ||  ||  ||   '],
            ['||     ||==||  ||==   ||==   ||==|| ||==   ||====  ||==||'],
            ['||     ||  ||  ||     ||         || ||     ||   ||     ||'],
            ['||===  ||  ||  ||===  ||===  ====|| ||===  ||   || ====||']]


player1 = {'side': ' ', 'pieces': ' ', 'remainingPieces': 16, 'checkmate': False, 'captures': []}
player2 = {'side': ' ', 'pieces': ' ', 'remainingPieces': 16, 'checkmate': False, 'captures': []}

pieces = {
            'black': {
                'h7': {'name': 'bpawn-1', 'taken': False, 'symbol': 'BP1'},
                'g7': {'name': 'bpawn-2', 'taken': False, 'symbol': 'BP2'},
                'f7': {'name': 'bpawn-3', 'taken': False, 'symbol': 'BP3'},
                'e7': {'name': 'bpawn-4', 'taken': False, 'symbol': 'BP4'},
                'd7': {'name': 'bpawn-5', 'taken': False, 'symbol': 'BP5'},
                'c7': {'name': 'bpawn-6', 'taken': False, 'symbol': 'BP6'},
                'b7': {'name': 'bpawn-7', 'taken': False, 'symbol': 'BP7'},
                'a7': {'name': 'bpawn-8', 'taken': False, 'symbol': 'BP8'},
                'h8': {'name': 'brook-1', 'taken': False, 'symbol': 'BR1'}, 
                'a8': {'name': 'brook-2', 'taken': False, 'symbol': 'BR2'},
                'g8': {'name': 'bknight-1', 'taken': False, 'symbol': 'BN1'},
                'b8': {'name': 'bknight-2', 'taken': False, 'symbol': 'BN2'},
                'f8': {'name': 'bbishop-1', 'taken': False, 'symbol': 'BB1'}, 
                'c8': {'name': 'bbishop-2', 'taken': False, 'symbol': 'BB2'},
                'd8': {'name': 'bqueen', 'taken': False, 'symbol': 'BQ '},
                'e8': {'name': 'bking', 'taken': False, 'symbol': 'BK '}
            },
            'white': {
                'a2': {'name': 'wpawn-1', 'taken': False, 'symbol': 'WP1'}, 
                'b2': {'name': 'wpawn-2', 'taken': False, 'symbol': 'WP2'},
                'c2': {'name': 'wpawn-3', 'taken': False, 'symbol': 'WP3'},
                'd2': {'name': 'wpawn-4', 'taken': False, 'symbol': 'WP4'},
                'e2': {'name': 'wpawn-5', 'taken': False, 'symbol': 'WP5'},
                'f2': {'name': 'wpawn-6', 'taken': False, 'symbol': 'WP6'},
                'g2': {'name': 'wpawn-7', 'taken': False, 'symbol': 'WP7'},
                'h2': {'name': 'wpawn-8', 'taken': False, 'symbol': 'WP8'},
                'a1': {'name': 'wrook-1', 'taken': False, 'symbol': 'WR1'},
                'h1': {'name': 'wrook-2', 'taken': False, 'symbol': 'WR2'},
                'b1': {'name': 'wknight-1', 'taken': False, 'symbol': 'WN1'},
                'g1': {'name': 'wknight-2', 'taken': False, 'symbol': 'WN2'},
                'c1': {'name': 'wbishop-1', 'taken': False, 'symbol': 'WB1'},
                'f1': {'name': 'wbishop-2', 'taken': False, 'symbol': 'WB2'},
                'd1': {'name': 'wqueen', 'taken': False, 'symbol': 'WQ '},
                'e1': {'name': 'wking', 'taken': False, 'symbol': 'WK '}
              },
          }
    

theBoard = {'a8': '   ', 'b8': '   ', 'c8': '   ', 'd8': '   ', 'e8': '   ', 'f8': '   ', 'g8': '   ', 'h8': '   ',
            'a7': '   ', 'b7': '   ', 'c7': '   ', 'd7': '   ', 'e7': '   ', 'f7': '   ', 'g7': '   ', 'h7': '   ',
            'a6': '   ', 'b6': '   ', 'c6': '   ', 'd6': '   ', 'e6': '   ', 'f6': '   ', 'g6': '   ', 'h6': '   ',
            'a5': '   ', 'b5': '   ', 'c5': '   ', 'd5': '   ', 'e5': '   ', 'f5': '   ', 'g5': '   ', 'h5': '   ',
            'a4': '   ', 'b4': '   ', 'c4': '   ', 'd4': '   ', 'e4': '   ', 'f4': '   ', 'g4': '   ', 'h4': '   ',
            'a3': '   ', 'b3': '   ', 'c3': '   ', 'd3': '   ', 'e3': '   ', 'f3': '   ', 'g3': '   ', 'h3': '   ',
            'a2': '   ', 'b2': '   ', 'c2': '   ', 'd2': '   ', 'e2': '   ', 'f2': '   ', 'g2': '   ', 'h2': '   ',
            'a1': '   ', 'b1': '   ', 'c1': '   ', 'd1': '   ', 'e1': '   ', 'f1': '   ', 'g1': '   ', 'h1': '   ',  
}


def playerSelect():
    pickASide = False

    while pickASide == False:
        print("Player 1, choose a color (B/W).")
        side = input()
        print()
        if side == 'B':
            player1[side] = 'Black'
            player1['pieces'] = pieces['black']
            player2[side] = 'White'
            player2['pieces'] = pieces['white']
            pickASide = True
        elif side == 'W':
            player1[side] = 'White'
            player1['pieces'] = pieces['white']
            player2[side] = 'Black'
            player2['pieces'] = pieces['black']
            pickASide = True
        else:
            print("Please enter either 'B' or 'W' only.")
            print()

    print("Player 1 you are playing as: " +
          player1[side] + " and Player 2 is playing as " + player2[side] + ".")
    print()

print()
print("Welcome to Primitive")
print('<--------------------')
for list in cheesers:
    i = 0
    print(list[i])
    i += 1
print('                                     -------------------->')
print()
playerSelect()


def printBoard(board):
    print()
    print(board['a8'] + ' | ' + board['b8'] + ' | ' + board['c8'] + ' | ' +  board['d8'] + 
          ' | ' +  board['e8'] + ' | ' +  board['f8'] + ' | ' +  board['g8'] + ' | ' +  board['h8'] + ' |8 ')
    print(' -  +  -  +  -  +  -  +  -  +  -  +  -  +  -  |')
    print(board['a7'] + ' | ' + board['b7'] + ' | ' + board['c7'] + ' | ' + board['d7'] +
          ' | ' + board['e7'] + ' | '  + board['f7'] + ' | '   + board['g7'] + ' | '  +  board['h7'] + ' |7 ')
    print(' -  +  -  +  -  +  -  +  -  +  -  +  -  +  -  |             Player 1 Captures:')
    print(board['a6'] + ' | ' + board['b6'] + ' | ' + board['c6'] + ' | ' + board['d6'] +
          ' | ' + board['e6'] + ' | '  + board['f6'] + ' | '   + board['g6'] + ' | '  +  board['h6'] + ' |6 ')
    print(' -  +  -  +  -  +  -  +  -  +  -  +  -  +  -  |            ' + str(player1['captures']))
    print(board['a5'] + ' | ' + board['b5'] + ' | ' + board['c5'] + ' | ' + board['d5'] +
          ' | ' + board['e5'] + ' | '  + board['f5'] + ' | '   + board['g5'] + ' | '  +  board['h5'] + ' |5 ')
    print(' -  +  -  +  -  +  -  +  -  +  -  +  -  +  -  |')
    print(board['a4'] + ' | ' + board['b4'] + ' | ' + board['c4'] + ' | ' + board['d4'] +
          ' | ' + board['e4'] + ' | '  + board['f4'] + ' | '   + board['g4'] + ' | '  +  board['h4'] + ' |4 ')
    print(' -  +  -  +  -  +  -  +  -  +  -  +  -  +  -  |             Player 1 Captures:')
    print(board['a3'] + ' | ' + board['b3'] + ' | ' + board['c3'] + ' | ' + board['d3'] +
          ' | ' + board['e3'] + ' | '  + board['f3'] + ' | '   + board['g3'] + ' | '  +  board['h3'] + ' |3 ')
    print(' -  +  -  +  -  +  -  +  -  +  -  +  -  +  -  |            ' + str(player2['captures']))
    print(board['a2'] + ' | ' + board['b2'] + ' | ' + board['c2'] + ' | ' + board['d2'] +
          ' | ' + board['e2'] + ' | '  + board['f2'] + ' | '   + board['g2'] + ' | '  +  board['h2'] + ' |2 ')
    print(' -  +  -  +  -  +  -  +  -  +  -  +  -  +  -  |')
    print(board['a1'] + ' | ' + board['b1'] + ' | ' + board['c1'] + ' | ' + board['d1'] +
          ' | ' + board['e1'] + ' | '  + board['f1'] + ' | '   + board['g1'] + ' | '  +  board['h1'] + ' |1 ')
    print('_____________________________________________ |')
    print(' A     B     C     D     E     F     G     H')

def populatePieces(board, pieces):
    
    blackPieces = pieces['black']
    whitePieces = pieces['white']

    blackStartPosition = blackPieces.keys()
    whiteStartPosition = whitePieces.keys()

    
    for key in blackStartPosition:
        board[key] = blackPieces[key]['symbol']

    for key in whiteStartPosition:
        board[key] = whitePieces[key]['symbol']
    
    printBoard(board)

populatePieces(theBoard, pieces)

#==============================#
def validMoveChecker():
    print()
    # determine if a move is legal - might need to set rules in the pieces dictionary
    # for example for pawns: if the number is the same it is not legal
    #                        if the number is lesser or greater (depending on which side) it is not legal
    #                        if the number or letter increases by more than 1 (except on first turn) it is not legal

def checkChecker():
    print()
    # determine if there is a checkmate (for the purpose of this, checkmate occurs when a player only has a king
    # left or the king is taken)

def captureTallier():
    print()
    # if a piece is captured, add it to the capturing player's capture list and decrement the captured players piece count

def turnCaller():
    print()
    # this should run until checkmate is true, a player quits, or the game is reset (while loop)
    # print who's turn it is
    # run logic for player's turn (ask for move, check if valid, check checkmate, captur talley)




# def isValidChessBoard(board):
#     print(board)