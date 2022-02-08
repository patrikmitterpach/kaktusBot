def evaluateRows(gameBoard):
    for i in range(6):
        for ii in range(4):
            if len(set(gameBoard[i][ii:ii+4])) == 1 and gameBoard[i][ii] != 0:
                return gameBoard[i][ii]
    return 0
    
def evaluateColumns(gameBoard):
    for i in range(7):
        currColumn = []
        for ii in range(6):
            currColumn.append(gameBoard[ii][i])
            if len(currColumn) > 4:
                currColumn.pop(0)
                
            if len(set(currColumn)) == 1 and currColumn[0] != 0 and len(currColumn) == 4:
                return gameBoard[ii][i]

    return 0

def evaluateDiagonal(gameBoard):
    for i in range(3):
        for ii in range(7):
            if gameBoard[i][ii] != 0 and ii < 4:
                gameBoardList = [gameBoard[i][ii], gameBoard[i+1][ii+1],
                                 gameBoard[i+2][ii+2], gameBoard[i+3][ii+3] ]
                if len(set(gameBoardList)) == 1:
                    return gameBoard[i][ii]

            if gameBoard[i][ii] != 0 and ii > 2:
                gameBoardList = [gameBoard[i][ii], gameBoard[i+1][ii-1],
                                 gameBoard[i+2][ii-2], gameBoard[i+3][ii-3] ]
                if len(set(gameBoardList)) == 1:
                    return gameBoard[i][ii]
    return 0
                     
def findWinner(gameBoard):
    Winner = (evaluateRows(gameBoard) or 
              evaluateColumns(gameBoard) or
              evaluateDiagonal(gameBoard) )

    return Winner

if __name__ == "__main__":
    gameBoard =    [ [ 0,   0,   0,   0,   0,   0,   0 ], # Scoring on the board:
                  [ 0,   0,   0,   0,   0,   0,   1 ], #    0 if Empty
                  [ 0,   0,   0,   0,   0,   1,   0 ], #    1 if Yellow
                  [ 0,   0,   0,   0,   1,   0,   0 ], #   -1 if Red
                  [ 0,   0,   0,   1,   0,   0,   0 ],
                  [ 0,   0,   0,   0,   0,   0,   0 ] ]
    print(findWinner(gameBoard, 2,3))