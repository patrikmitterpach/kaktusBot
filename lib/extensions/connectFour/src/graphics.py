from os import system

def drawBoard(board, currTurn, winner):
    # The board is assumed to have dimensions 7x6, 
    assert (len(board[0]) == 7)
    assert (len(board)    == 6)

    # visual representation of elements
    columnNames = ['A', 'B', 'C', 
                   'D', 'E', 'F', 'G']
    positions = { -1: " \u001b[33m●\u001b[0m ",
                   0: "   ",
                   1: " \u001b[31m●\u001b[0m " }
    
    separators = ['', '|']

    
    # print("\r")
    for row in range(6):
        print("\t", end="")
        for column in range(6):
            print('{}|'.format(positions[board[row][column]]), end="")
        print(f'{positions[board[row][6]]}', end="")
        if row == 2:
            if winner:
                print("    WINNER:")
            else:
                print("  CURRENT TURN:")

        elif row == 3:
            print("     \u001b[33mYELLOW\u001b[0m" if currTurn % 2 else "      \u001b[31mRED\u001b[0m")
        else:
            print("")
    print("\t▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
    print("\t", end="")
    for column in columnNames:
        print(f' {column} ', end=" ")
    print("")
