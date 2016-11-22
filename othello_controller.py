#Name: Alfianto Widodo
#Student ID: 69222688


import othello_model

def input_settings():
    '''gets user input for game settings'''
    rows = int(input(''))
    columns = int(input(''))
    first_move = str(input(''))
    top_left = str(input(''))
    more_or_less = str(input(''))

    return rows, columns, first_move, top_left, more_or_less

def print_number_of_discs(othello_game: othello_model.OthelloGame):
    '''prints the number of discs each player has'''
    print('B:', othello_game._black_count,
          'W:', othello_game._white_count)

def print_turn(othello_game: othello_model.OthelloGame):
    '''prints whose turn it is'''
    print('TURN:', othello_game._turn)

def draw_board(othello_game: othello_model.OthelloGame):
    '''draws the board'''
    for row in othello_game._board:
        for column in row:
            print(column, end = ' ')
        print(' ', end = '\n')


def get_valid_move() -> (int, int):
    '''
    asks for a valid move
    prints 'INVALID' when the move isn't valid and asks
    the user for another move again
    '''

    while True:
        row_num, column_num = _read_input()
            
        if othello_game.is_valid(row_num, column_num):
            print('VALID')
            return row_num, column_num

        else:
            print('INVALID')


def _read_input() ->(int, int):
    '''formats the input to a more useable form'''
    row_num, column_num = input('').split(' ')
    return(int(row_num) - 1, int(column_num) - 1)


if __name__ == '__main__':
    print('FULL')

    othello_game = othello_model.OthelloGame()
    rows, columns, first_move, top_left, more_or_less = input_settings()
    othello_game.get_settings(rows, columns, first_move,
                              top_left, more_or_less)
    
    try:
        othello_game.new_game()

        while othello_game.check_game_over():
            print_number_of_discs(othello_game)
            draw_board(othello_game)
            print_turn(othello_game)
            
            row_num, column_num = get_valid_move()
            othello_game.reverse(row_num, column_num)

            othello_game.count_discs()
            othello_game.check_game_over()
            othello_game.next_turn()
        
    
        print_number_of_discs(othello_game)
        draw_board(othello_game)
        othello_game.check_winner()

        print('WINNER:',othello_game._winner)

    except othello_model.InvalidSettingsError:
        print('INVALID SETTINGS')
        
