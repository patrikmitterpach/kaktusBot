from os import system
def createRow(board, row):
    positions = {  -1: "  🔴  ",
                    0: "          ",
                    1: "  🟡  " }
    
    currRow = ' '
    for i in range(len(board[0]) - 1):
        currRow = f'{currRow} {positions[board[row][i]]} |'
    currRow = f'{currRow} {positions[board[row][6]]}'
    
    return currRow

def drawBoard(board):

    # One item in list represents a row
    message = ["**-------------                 CONNECT 4                 -------------**\n",
               "         *Pre zvolenie stĺpca stlačte príslušnú reakciu.*",
               "       *Ťah možno spraviť len ak je indikovaná ikonka",
               "                                súčasného ťahu*",
               "" ]

    for i in range( len(board) ):
        row = createRow(board, i)
        message.append( row )

    message.append( "▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀" )
    return "\n".join(message)