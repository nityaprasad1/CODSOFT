import random

print("Welcome to Tic Tac Toe")
print("----------------------")

possibleNumbers = [1,2,3,4,5,6,7,8,9]
gameBoard = [[None, None, None], [None, None, None], [None, None, None]]
rows = 3
cols = 3

def printGameBoard():
    for x in range(rows):
        print("\n+---+---+---+")
        print("|", end="")
        for y in range(cols):
            cell = gameBoard[x][y]
            print("", cell if cell is not None else ' ', end=" |")
    print("\n+---+---+---+")

def modifyArray(num, turn):
    num -= 1
    gameBoard[num // 3][num % 3] = turn

def isMovesLeft(board):
    for row in board:
        if None in row:
            return True
    return False

def evaluate(board):
    for row in board:
        if row[0] == row[1] == row[2]:
            if row[0] == 'X':
                return 10
            elif row[0] == 'O':
                return -10
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == 'X':
                return 10
            elif board[0][col] == 'O':
                return -10
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'X':
            return 10
        elif board[0][0] == 'O':
            return -10
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            return 10
        elif board[0][2] == 'O':
            return -10
    return 0

def minimax(board, depth, isMax):
    score = evaluate(board)
    if score == 10 or score == -10:
        return score
    if not isMovesLeft(board):
        return 0
    if isMax:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] is None:
                    board[i][j] = 'X'
                    best = max(best, minimax(board, depth + 1, not isMax))
                    board[i][j] = None
        return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] is None:
                    board[i][j] = 'O'
                    best = min(best, minimax(board, depth + 1, not isMax))
                    board[i][j] = None
        return best

def findBestMove(board):
    bestVal = -1000
    bestMove = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                board[i][j] = 'X'
                moveVal = minimax(board, 0, False)
                board[i][j] = None
                if moveVal > bestVal:
                    bestMove = (i, j)
                    bestVal = moveVal
    return bestMove

def checkForWinner(board):
    lines = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    for line in lines:
        if line[0] == line[1] == line[2] and line[0] is not None:
            return line[0]
    return "N"

leaveLoop = False
turnCounter = 0

while not leaveLoop:
    printGameBoard()
    if turnCounter % 2 == 0:
        numberPicked = int(input("\nChoose a number [1-9]: "))
        if 1 <= numberPicked <= 9 and possibleNumbers[numberPicked-1]:
            modifyArray(numberPicked, 'X')
            possibleNumbers[numberPicked-1] = None
        else:
            print("Invalid input. Please try again.")
        turnCounter += 1
    else:
        print("CPU's turn")
        bestMove = findBestMove(gameBoard)
        if bestMove != (-1, -1):
            modifyArray(bestMove[0] * 3 + bestMove[1] + 1, 'O')
            possibleNumbers[bestMove[0] * 3 + bestMove[1]] = None
        turnCounter += 1

    winner = checkForWinner(gameBoard)
    if winner != "N":
        printGameBoard()
        print(f"\nGame over! {winner} has won! Thank you for playing :)")
        break
    elif not isMovesLeft(gameBoard):
        printGameBoard()
        print("\nGame over! It's a tie! Thank you for playing :)")
        break
