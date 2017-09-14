def print_board(list_of_symbols):
    """
    This is the function that will print the board for tic tac toe game
    :return: 
    """
    print('this is the tic tac toe board')
    print('   |   |   ')
    print(' ' + list_of_symbols[0] + ' | ' + list_of_symbols[1] + ' | ' + list_of_symbols[2] + ' ')
    print('   |   |   ')
    print('---|---|---')
    print('   |   |   ')
    print(' ' + list_of_symbols[3] + ' | ' + list_of_symbols[4] + ' | ' + list_of_symbols[5] + ' ')
    print('   |   |   ')
    print('---|---|---')
    print('   |   |   ')
    print(' ' + list_of_symbols[6] + ' | ' + list_of_symbols[7] + ' | ' + list_of_symbols[8] + ' ')
    print('   |   |   ')


def instruction():
    """
    This function prints instruction of my tic tac toe game.
    :return: 
    """
    print('- - - - - - - - - - - - - - - - - - - - -')
    print("this is instruction for tic tac toe game".upper())
    print('- - - - - - - - - - - - - - - - - - - - -')
    print('This is game for two players')
    print('Each player can choose a number between 1 and 9')
    print('Numbers represent the fields on the board')
    print('You can choose only numbers that are not taken by any player')
    list_of_symbols = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    print_board(list_of_symbols)
    print('You win the game if you have 3 symbols in column, row or diagonally')
    print('- - - - - - - - - - - - - - - - - - - - -')

    begin_game()


def begin_game():
    """
    This function begins the new game of tic tac toe.
    :return: 
    """
    print('welcome to the game')
    print('To learn the rules, write "instruction", if you want to play, write "play"')
    decision = input('What do you want to do?')
    if decision == 'instruction':
        instruction()
    elif decision == 'play':
        play_tic_tac_toe()
    else:
        print('please write "instruction" or "play"')
        begin_game()


def play_tic_tac_toe():
    list_of_symbols = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    print_board(list_of_symbols)
    process_movement(("one", "o"), list_of_symbols)
    begin_game()


def check_not_win(list_of_symbols):
    """
    This function checks if one of the player is winner or not
    :return: 
    """
    count_elements = 0
    for element in range(0, 9):
        if list_of_symbols[element] != ' ':
            count_elements += 1

    if list_of_symbols[0] == list_of_symbols[1] == list_of_symbols[2] == ('o' or 'x'):
        if list_of_symbols[0] == 'o':
            print("Player one won")
        else:
            print("Player two won")
    elif list_of_symbols[3] == list_of_symbols[4] == list_of_symbols[5] == ('o' or 'x'):
        if list_of_symbols[3] == 'o':
            print("Player one won")
        else:
            print("Player two won")
    elif list_of_symbols[6] == list_of_symbols[7] == list_of_symbols[8] == ('o' or 'x'):
        if list_of_symbols[6] == 'o':
            print("Player one won")
        else:
            print("Player two won")
    elif list_of_symbols[0] == list_of_symbols[3] == list_of_symbols[6] == ('o' or 'x'):
        if list_of_symbols[6] == 'o':
            print("Player one won")
        else:
            print("Player two won")
    elif list_of_symbols[1] == list_of_symbols[4] == list_of_symbols[7] == ('o' or 'x'):
        if list_of_symbols[1] == 'o':
            print("Player one won")
        else:
            print("Player two won")
    elif list_of_symbols[2] == list_of_symbols[5] == list_of_symbols[8] == ('o' or 'x'):
        if list_of_symbols[2] == 'o':
            print("Player one won")
        else:
            print("Player two won")
    elif list_of_symbols[0] == list_of_symbols[4] == list_of_symbols[8] == ('o' or 'x'):
        if list_of_symbols[0] == 'o':
            print("Player one won")
        else:
            print("Player two won")
    elif list_of_symbols[2] == list_of_symbols[4] == list_of_symbols[6] == ('o' or 'x'):
        if list_of_symbols[6] == 'o':
            print("Player one won")
        else:
            print("Player two won")
    elif count_elements == 9:
        print("Nobody won")
    else:
        return True


def process_movement(player_info, list_of_symbols):
    chosen_number = input('player {}, please choose the free number from 1 to 9'
                          .format(player_info[0]))
    while int(chosen_number) not in range(1, 10):
        chosen_number = input('you have to write the free number from 1 to 9')
    for number in range(1, 10):
        if chosen_number == str(number):
            if list_of_symbols[number - 1] == ' ':
                list_of_symbols[number - 1] = player_info[1]
            else:
                print('This place is already taken, you have to choose another one')
                process_movement(player_info, list_of_symbols)
    print_board(list_of_symbols)
    if check_not_win(list_of_symbols):
        next_player = get_next_player(player_info)
        process_movement(next_player, list_of_symbols)


def get_next_player(player_info):
    if player_info[0] == "one":
        return "two", "x"
    elif player_info[0] == "two":
        return "one", "o"
    else:
        raise Exception("Unexpected player_name value. Correct is 'one' or 'two'")


begin_game()
