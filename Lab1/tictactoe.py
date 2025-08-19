import random
board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
count = 0
def isFull():
    return count == 9
def showBoard():
    b = []
    for i in range(0, 9):
        if board[i] == 0:
            b.append(" ")
        elif board[i] == 1:
            b.append("X")
        elif board[i] == 2:
            b.append("O")
    print(f"{b[0]}\t{b[1]}\t{b[2]}")
    print(f"{b[3]}\t{b[4]}\t{b[5]}")
    print(f"{b[6]}\t{b[7]}\t{b[8]}")
def didWin():
    win = False
    winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8],[0, 4, 8], [2, 4, 6]]
    for combo in winning_combinations:
        if board[combo[0]] != 0 and board[combo[0]] == board[combo[1]] == board[combo[2]]:
            win = True
            break
    return win
def userMove():
    global count
    while True:
        try:
            a = int(input("Enter the cell number (0-8) to insert: "))
            if board[a] == 0:
                board[a] = 1
                count += 1
                break
            else:
                print("Cell is already occupied, try again.")
        except (ValueError, IndexError):
            print("Invalid input, please enter a number between 0 and 8.")
def compMove():
    global count
    flag = False
    while not flag:
        compM = random.randint(0, 8)
        if board[compM] == 0:
            board[compM] = 2
            count += 1
            flag = True
def tictactoeUser():
    global count
    print("Board cells (0-8): \n")
    print("0\t1\t2\n3\t4\t5\n6\t7\t8")
    while not isFull():
        showBoard()
        userMove()
        if didWin():
            showBoard()
            print("Congratulations! You win!")
            return

        if isFull():
            break
        compMove()
        if didWin():
            showBoard()
            print("Computer wins!")
            return
    showBoard()
    print("It's a draw!")

def tictactoeBot():
    global count
    print("Board cells (0-8): \n")
    print("0\t1\t2\n3\t4\t5\n6\t7\t8")
    while not isFull():
        compMove()
        showBoard()
        if didWin():
            showBoard()
            print("Computer wins!")
            return

        if isFull():
            break
        userMove()
        if didWin():
            showBoard()
            print("You win!")
            return
    showBoard()
    print("It's a draw!")

a=int(input("1 for X and 2 for O"))
if a == 1:
  tictactoeUser()
else:
  tictactoeBot()
