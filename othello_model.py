#Name: Alfianto Widodo
#Student ID: 69222688


EMPTY = '.'
BLACK = 'B'
WHITE = 'W'


class EndDiscError(Exception):
    '''
    raised when the attribute check_direction
    finds an empty grid when searching for a disc of
    the same color as the starting disc when
    building a list of discs to be reversed
    '''
    pass

class EndOfBoardError(Exception):
    '''
    raised when the attribute check_direction
    reaches the end of board when searching a disc of
    the same color as the starting disc when
    building a list of discs to be reversed
    '''
    pass

class InvalidSettingsError(Exception):
    '''
    raised when the settings the user input is invalid
    '''
    pass


class OthelloSettings:
    '''settings used to initialize the game'''
    def __init__(self):
        self._rows = int()
        self._columns = int()
        self._first_move = str()
        self._top_left = str()
        self._more_or_less = str()


class OthelloGame:
    '''
    the game object itself, containing
    the board, turn, settings, a bool variable containing
    the state of the game(over or not), the count of
    each color of discs, and the winner
    '''
    def __init__(self):
        self._board = []
        self._turn = str()
        self._settings = OthelloSettings()
        self._game_not_over = bool()
        self._black_count = int()
        self._white_count = int()
        self._winner = str()

    def get_settings(self, rows: int, columns: int, first_move: str,
                       top_left: str, more_or_less: str):
        '''
        stores the input variables into the appropriate attributes
        of the game object
        '''
        self._settings._rows = rows
        self._settings._columns = columns
        self._settings._first_move = first_move
        self._settings._top_left = top_left
        self._settings._more_or_less = more_or_less
        

    def new_game(self):
        '''
        this method starts a new game of othello, using
        the settings the user input to create a board of the
        desired size, and populating the middle 4 grids with
        the appropriate discs according to the settings
        '''
        self._check_settings()
        self._turn = self._settings._first_move
        self._game_not_over = True
        
        for rows in range(self._settings._rows):
            self._board.append([])

        for columns in range(self._settings._columns):
            for rows in self._board:
                rows.append(EMPTY)
                
        self._arrange_starting_discs()
        self.count_discs()


    def _check_settings(self):
        '''
        checks the settings input by the user
        if the settings is invalid, it raises the InvalidSettingsError
        '''
        discs_dict = {'B':'Black', 'W':'White'}
        more_or_less_dict = {'<':'Less', '>':'More'}

        if self._settings._rows < 4 or \
           self._settings._rows > 16 or \
           self._settings._rows % 2 != 0:
            raise InvalidSettingsError

        elif self._settings._columns < 4 or \
             self._settings._columns > 16 or \
             self._settings._columns % 2 != 0:
            raise InvalidSettingsError

        elif self._settings._first_move not in discs_dict or \
             self._settings._top_left not in discs_dict or \
             self._settings._more_or_less not in more_or_less_dict:
            raise InvalidSettingsError

       

    def count_discs(self):
        '''
        counts the number of discs of each color
        and stores the values in the appropriate
        attributes of the OthelloGame object
        '''
        black = 0
        white = 0
        
        for rows in self._board:
            for disc in rows:
                if disc == BLACK:
                    black += 1
                elif disc == WHITE:
                    white += 1

        self._black_count = black
        self._white_count = white
    

    def _arrange_starting_discs(self):
        '''
        called by the new_game() method to populate
        the middle 4 boxes with discs of the appropriate
        colors according to the settings
        '''
        if self._settings._top_left == BLACK:
            top_right = WHITE

        elif self._settings._top_left == WHITE:
            top_right = BLACK

        self._board[self._settings._rows // 2 - 1][self._settings._columns // 2 - 1] \
                                             = self._settings._top_left
        self._board[self._settings._rows     // 2][self._settings._columns // 2] \
                                             = self._settings._top_left

        self._board[self._settings._rows // 2 - 1][self._settings._columns // 2] \
                                             = top_right
        self._board[self._settings._rows // 2][self._settings._columns // 2 - 1] \
                                             = top_right


    def next_turn(self):
        '''
        moves the game on to the next turn by updating
        the attribute ._turn
        '''
        if self._turn == BLACK:
            self._turn = WHITE
        elif self._turn == WHITE:
            self._turn = BLACK


    def _opposite_color(self):
        '''
        returns the color that's opposite
        of whose turn it is
        '''
        if self._turn == BLACK:
            return WHITE
        elif self._turn == WHITE:
            return BLACK
    

    def _any_valid_move(self) -> bool:
        '''
        a method used to check if there is any valid move
        that the player can make when it's their turn
        '''
        for row_num in range(self._settings._rows):
            for column_num in range(self._settings._columns):
                if self.is_valid(row_num, column_num):
                    return True

        return False
                    

    def is_valid(self, row_num, column_num) -> bool:
        '''decides if a move is valid'''
        if self._check_end_of_board(row_num, column_num):
        
            if self._board[row_num][column_num] != EMPTY:
                return False

            elif len(self.find_reverse(row_num, column_num)) > 1:
                return True

            else:
                return False

        else:
            return False


    def _check_end_of_board(self, row_num: int, column_num: int) -> bool:
        '''
        used to check whether the row and column number passed to it
        is outside the board's range
        '''
        if row_num < 0 or row_num >= self._settings._rows:
            return False
                
        elif column_num < 0 or column_num >= self._settings._columns:
            return False

        else:
            return True


    def find_reverse(self, row_num: int, column_num: int) -> []:
        '''
        calls the _check_direction method and passes a row and column
        number and a row and column delta to that method
        returns a list of discs that should be reversed if a player
        makes a move on the row and column number that is passed to
        the method
        '''
        row_column_delta = [[-1, 0],
                            [-1, 1],
                            [0, 1],
                            [1, 1],
                            [1, 0],
                            [1, -1],
                            [0, -1],
                            [-1, -1]]

        reverse_list = [[row_num, column_num]]
        
        for delta_set in row_column_delta:
            try:
                reverse_list += self._check_direction(row_num + delta_set[0],
                                                    column_num + delta_set[1],
                                                    delta_set,
                                                    list())

            except(EndOfBoardError, EndDiscError):
                pass

        return reverse_list


    def _check_direction(self, row_num: int, column_num: int,
                         delta_set: list, discs_to_reverse: list)-> []:
        '''
        takes a row and column number, and a direction in the form of a list
        containing the row and column delta
        returns a list of the row and column number of discs that should be reversed
        in that direction
        if it can't find an ending disc to reverse to, it raises an EndDiscError
        or if it goes off the board finding the disc to reverse to, it raises an
        EndOfBoardError
        '''
        if self._check_end_of_board(row_num, column_num):
    
            if self._board[row_num][column_num] == self._opposite_color():
                discs_to_reverse.append([row_num, column_num])
                return self._check_direction(row_num + delta_set[0],
                                             column_num + delta_set[1],
                                             delta_set, discs_to_reverse)

            elif self._board[row_num][column_num] == self._turn:
                return discs_to_reverse
    
            elif self._board[row_num][column_num] == EMPTY:
                raise EndDiscError

        else:
            raise EndOfBoardError


    def reverse(self, row_num, column_num):
        '''
        calls the find_reverse method and reverses the discs in the row and column
        number that it returns
        '''
        discs_to_reverse = self.find_reverse(row_num, column_num)
        
        for disc in discs_to_reverse:
            self._board[disc[0]][disc[1]] = self._turn


    def check_game_over(self) -> bool:
        '''
        checks if a player can make any valid move
        if not, it moves on to the next player and checks
        if they could make any
        if both players can't make any valid move, it
        returns False which ends the game loop
        '''
        if self._any_valid_move():
            return True

        else:
            self.next_turn()
            if self._any_valid_move():
                return True

            else:
                return False


    def check_winner(self):
        '''
        checks who is the winner based on the settings
        of the game and the count of discs of each color
        '''
        if self._black_count == self._white_count:
                self._winner = 'NONE'
                
        elif self._settings._more_or_less == '>':
            if self._black_count > self._white_count:
                self._winner = BLACK

            elif self._black_count < self._white_count:
                self._winner = WHITE

        elif self._settings._more_or_less == '<':
            if self._black_count < self._white_count:
                self._winner = BLACK

            elif self._black_count > self._white_count:
                self._winner = WHITE
