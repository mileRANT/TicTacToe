# Implementation of Two Player Tic-Tac-Toe game in Python.

''' We will make the board using dictionary
    in which keys will be the location(i.e : top-left,mid-right,etc.)
    and initiallly it's values will be empty space and then after every move
    we will change the value according to player's choice of move. '''

theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

# board keys kept as an array to make it easier to reset
board_keys = []

for key in theBoard:
    board_keys.append(key)

''' We will have to print the updated board after every move in the game and 
    thus we will make a function in which we'll define the printBoard function
    so that we can easily print the board everytime by calling this function. '''


def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


# Now we'll write the main function which has all the gameplay functionality.
def game():
    turn = 'X'
    count = 0
    print("Tic Tac Toe! Let's Go!!")
    print("Movement is based on the number Keypad. Please enter a number to go.")
    for i in range(10):
        printBoard(theBoard)
        print("It's your turn," + turn + ".Move to which place?")

        move = input()

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        # Now we will check if player X or O has won,for every move after 5 moves.
        if count >= 5:
            if checkWin(theBoard):
                print("\nGame Has Ended.")
                print(" **** " + turn + " won. ****")
                # break out of the loop
                break

        # board has filled and checkwin is false
        if count == 9:
            print("\nGame Has Ended.")
            print("It's a Draw!")

        # Change symbol/whose turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

            # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        # resetting board keys selection and the board
        for key in board_keys:
            theBoard[key] = " "
        game()

def checkWin(theBoard):
    if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':  # across the top
        return True
    elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':  # across the middle
        return True
    elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':  # across the bottom
        return True
    elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':  # down the left side
        return True
    elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':  # down the middle
        return True
    elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':  # down the right side
        return True
    elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':  # diagonal
        return True
    elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':  # diagonal
        return True
    # if all else is false, noone has won
    return False

if __name__ == "__main__":
    game()