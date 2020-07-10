def disp_board():  # Define the definition to display the board.
    """
    Shows player how board will look.
    """
    print("""""
    ------------
    | {}|{}|{} |
    |----------|
    | {}|{}|{} | 
    |----------|
    | {}|{}|{} |
    ------------
     """"".format('  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '))


userdict = {1: '.', 2: '..', 3: ':', 4: ';', 5: '%', 6: '.:', 7: ':.', 8: '*',
            9: '.;'}  # Storing the user input in this dictionary
playerpos = None
game_on = False


def full_board():
    """
    Checks if the board is full.
    """
    if icount == 9:
        return True
    else:
        return False

def game_board():  # The board used for in the game.
    """
    Prints board used for gameplay.
    """
    print("""""
    -------------
    | {} | {} | {} |
    |-----------|
    | {} | {} | {} | 
    |-----------|
    | {} | {} | {} |
    -------------
     """"".format(userdict[7], userdict[8], userdict[9], userdict[4], userdict[5], userdict[6], userdict[1],
                  userdict[2], userdict[3]))


def check_taken1(player1pos=None):  # Checks if the input that player 1 gave is already taken.
    """
    Checks if the value that player 1 entered is valid and if that spot is available.
    """
    if userdict[player1pos] == 'X' or userdict[player1pos] == 'O' or check_input():
        print('That spot is already taken or you have not entered a value!!')
        player1pos = int(input('Enter position using 1-9 on numpad. '))
        userdict[player1pos] = player1
    else:
        userdict[player1pos] = player1


def check_taken2(player2pos=None):  # Checks if the input that player 2 gave is already taken.
    """
    Checks if the value that player 2 entered is valid and if that spot is available.
    """
    if userdict[player2pos] == 'X' or userdict[player2pos] == 'O' or check_input():
        print('That spot is already taken or you have not entered a value!!')
        player2pos = int(input('Enter position using 1-9 on numpad. '))
        userdict[player2pos] = player2
    else:
        userdict[player2pos] = player2


def check_input():  # Checks if user entered a valid value.
    """
    Checks if the input that the player entered is valid
    """
    if playerpos == 0 or playerpos == 1 or playerpos == 2 or playerpos == 3 or playerpos == 4 or playerpos == 5 or playerpos == 6 or playerpos == 7 or playerpos == 8 or playerpos == 9:
        return False
    else:
        return True


def check_if_win(userdict1):  # Checks if the game is won
    """
    Checks if the game is won.
    Input : the userdictionary that stores the values.
    """
    import time
    import sys
    import os
    if userdict1[1] == userdict1[2] and userdict1[2] == userdict1[3]:  # Won through bottom row.
        game_on = False
        game_over()
        time.sleep(5)
        replay = input('To you want to play again? Enter Yes or No. ').lower
        if replay == 'yes' or 'y' or 'Yes' or 'Y':
            print('Restarting the game!!')
            time.sleep(5)
            os.system("python %USERPROFILE%\Downloads\TicTacToe.py")
        else:
            if replay == 'no' or 'No' or 'n' or 'N':
                print('Exiting the game!')
                time.sleep(5)
                sys.exit()
    elif userdict1[4] == userdict1[5] and userdict1[5] == userdict1[6]:  # Checks if won via the middle row.
        game_on = False
        game_over()
        time.sleep(5)
        replay = input('To you want to play again? Enter Yes or No. ').lower
        if replay == 'yes' or 'y' or 'Yes' or 'Y':
            print('Restarting the game!!')
            time.sleep(5)
            os.system("python %USERPROFILE%\Downloads\TicTacToe.py")
        else:
            if replay == 'no' or 'No' or 'n' or 'N':
                print('Exiting the game!')
                time.sleep(5)
                sys.exit()
    elif userdict1[7] == userdict1[8] and userdict1[8] == userdict1[9]:  # Checks if won via top row.
        game_on = False
        game_over()
        time.sleep(5)
        replay = input('To you want to play again? Enter Yes or No. ').lower
        if replay == 'yes' or 'y' or 'Yes' or 'Y':
            print('Restarting the game!!')
            time.sleep(5)
            os.system("python %USERPROFILE%\Downloads\TicTacToe.py")
        else:
            if replay == 'no' or 'No' or 'n' or 'N':
                print('Exiting the game!')
                time.sleep(5)
                sys.exit()
    elif userdict1[1] == userdict1[4] and userdict1[4] == userdict1[7]:  # Checks if won via left columb
        game_on = False
        game_over()
        time.sleep(5)
        replay = input('To you want to play again? Enter Yes or No. ').lower
        if replay == 'yes' or 'y' or 'Yes' or 'Y':
            print('Restarting the game!!')
            time.sleep(5)
            os.system("python %USERPROFILE%\Downloads\TicTacToe.py")
        else:
            if replay == 'no' or 'No' or 'n' or 'N':
                print('Exiting the game!')
                time.sleep(5)
                sys.exit()
    elif userdict1[2] == userdict1[5] and userdict1[5] == userdict1[8]:  # Checks if won via middle columb
        game_on = False
        game_over()
        time.sleep(5)
        replay = input('To you want to play again? Enter Yes or No. ').lower
        if replay == 'yes' or 'y' or 'Yes' or 'Y':
            print('Restarting the game!!')
            time.sleep(5)
            os.system("python %USERPROFILE%\Downloads\TicTacToe.py")
        else:
            if replay == 'no' or 'No' or 'n' or 'N':
                print('Exiting the game!')
                time.sleep(5)
                sys.exit()
    elif userdict1[3] == userdict1[6] and userdict1[6] == userdict1[9]:  # Checks if won via right columb
        game_on = False
        game_over()
        time.sleep(5)
        replay = input('To you want to play again? Enter Yes or No. ').lower
        if replay == 'yes' or 'y' or 'Yes' or 'Y':
            print('Restarting the game!!')
            time.sleep(5)
            os.system("python %USERPROFILE%\Downloads\TicTacToe.py")
        else:
            if replay == 'no' or 'No' or 'n' or 'N':
                print('Exiting the game!')
                time.sleep(5)
                sys.exit()
    elif userdict1[3] == userdict1[5] and userdict1[5] == userdict1[7]:  # Checks if won from bottom right to top left
        game_on = False
        game_over()
        time.sleep(5)
        replay = input('To you want to play again? Enter Yes or No. ').lower
        if replay == 'yes' or 'y' or 'Yes' or 'Y':
            print('Restarting the game!!')
            time.sleep(5)
            os.system("python %USERPROFILE%\Downloads\TicTacToe.py")
        else:
            if replay == 'no' or 'No' or 'n' or 'N':
                print('Exiting the game!')
                time.sleep(5)
                sys.exit()
    elif userdict1[1] == userdict1[5] and userdict1[5] == userdict1[9]:  # Checks if won from bottom left to top right
        game_on = False

        game_over()
        time.sleep(5)
        replay = input('To you want to play again? Enter Yes or No. ').lower
        if replay == 'yes' or 'y' or 'Yes' or 'Y':
            print('Restarting the game!!')
            time.sleep(5)
            os.system("python %USERPROFILE%\Downloads\TicTacToe.py")
        else:
            if replay == 'no' or 'No' or 'n' or 'N':
                print('Exiting the game!')
                time.sleep(5)
                sys.exit()
    elif full_board() == True: # Checks if the board is full
        game_on = False

        game_over()
        time.sleep(5)
        replay = input('To you want to play again? Enter Yes or No. ').lower
        if replay == 'yes' or 'y' or 'Yes' or 'Y':
            print('Restarting the game!!')
            time.sleep(5)
            os.system("python %USERPROFILE%\Downloads\TicTacToe.py")
        else:
            if replay == 'no' or 'No' or 'n' or 'N':
                print('Exiting the game!')
                time.sleep(5)
                sys.exit()
    else:
        game_on = True


def game_over():  # Checks who won the game
    """
    Checks who won the game.
    """
    if userdict[1] == userdict[2] == userdict[3]:
        print(userdict[1] + ' won the game!')
    elif userdict[1] == userdict[5] == userdict[9]:
        print(userdict[1] + ' won the game!')
    elif userdict[3] == userdict[6] == userdict == userdict[9]:
        print(userdict[3] + ' won the game!')
    elif userdict[1] == userdict[4] == userdict[7]:
        print(userdict[1] + ' won the game!')
    elif userdict[3] == userdict[5] == userdict[7]:
        print(userdict[3] + ' won the game!')
    elif userdict[4] == userdict[5] == userdict[6]:
        print(userdict[4] + ' won the game!')
    elif userdict[7] == userdict[8] == userdict[9]:
        print(userdict[7] + ' won the game!')
    elif userdict[8] == userdict[5] == userdict[2]:
        print(userdict[8] + ' won the game!')
    else:
        print('It is a tie!')


#Variables needed
player1 = ''
player2 = ''
game_on = bool
icount = 0


print('Welcome to Tic Tac Toe!')  # Begin of game
disp_board()
print('Player 1 choose!')
player1 = input('Please pick a marker X or O : ').upper()
if player1 == 'X':
    player2 = 'O'
else:
    player2 = 'X'
print('')


while game_on:  # Begin Game
    print('Player 1')
    # Player1 input position
    playerpos = int(input('Enter position using 1-9 on numpad. '))
    check_taken1(playerpos)
    game_board()
    icount = icount + 1
    check_if_win(userdict)


    # User 2 Turn
    print('Player 2')
    # Player 2 chooses position
    playerpos = int(input('Enter position using 1-9 on numpad. '))
    check_taken2(playerpos)
    game_board()
    icount =  icount + 1
    check_if_win(userdict)

