def sum(a, b, c):
    return a + b + c

def printBoard(xState, zState):
    symbols = ['X' if xState[i] else ('O' if zState[i] else str(i)) for i in range(9)]
    print(f" {symbols[0]} | {symbols[1]} | {symbols[2]} ")
    print("-----------")
    print(f" {symbols[3]} | {symbols[4]} | {symbols[5]} ")
    print("-----------")
    print(f" {symbols[6]} | {symbols[7]} | {symbols[8]} ")

def checkWin(xState, zState):
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for win in wins:
        if sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            print("X won the match")
            return 1
        if sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3:
            print("O won the match")
            return 0
    return -1

if __name__ == "__main__":
    xState = [0] * 9
    zState = [0] * 9
    turn = 1 # 1 for X and 0 for O
    print("...Welcome to Tic Tac Toe...")

    while True:
        printBoard(xState, zState)
        if turn == 1:
            print("X's turn")
        else:
            print("O's turn")

        try:
            value = int(input("Please enter a value (0-8): "))
            if value < 0 or value > 8:
                print("Invalid input. Please enter a number between 0 and 8.")
                continue
            if xState[value] == 1 or zState[value] == 1:
                print("Position already taken. Please choose another one.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if turn == 1:
            xState[value] = 1
        else:
            zState[value] = 1

        cwin = checkWin(xState, zState)
        if cwin != -1:
            printBoard(xState, zState)
            print("Match over")
            break

        turn = 1 - turn