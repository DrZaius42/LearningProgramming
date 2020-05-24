#this program checks if ,given the positions of the pieces, is valid chess board.
#It only considers the number of pieces

testPositions = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop',
                 '5h': 'bqueen', '3e': 'wking' }

def isValidChessBoard(board):

    isValid = False
    countPieces = {}
    for pos in board:
        if pos[0] in range(0,9) and pos[1] in 'abcdefgh':#makes sure the piece is in the board
            isValid = True
        if board[pos][0] == 'w' or board[pos][0] == 'b':#makes sure the piece is either black or white
            isValid = True
        countPieces.setdefault(board[pos], 0)#adds to a dict. all the pieces in the board
        countPieces[board[pos]] = countPieces[board[pos]] + 1#changes the value of the pieces to how many of them are
        for piece in countPieces:
          if countPieces[piece] > 1 and ('king' in piece or  'queen' in piece):#checks if the piece is king or queen, and  checks if it is only one of each
              isValid = False
          elif countPieces[piece] > 2 and ('pawn' not in piece):#checks flase if the piece is not a pawn and there max 2
              isValid = False
          elif countPieces[piece] > 8:#gets here only if the piece is a pawn, checks if they are less than 9
              isValid = False  
                
    return isValid 


print(isValidChessBoard(testPositions))