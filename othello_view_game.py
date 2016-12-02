#Name: Alfianto Widodo
#Student ID: 69222688

import tkinter
import othello_view_settings
import othello_model

_DEFAULT_FONT = ('Calibri', 14, 'bold')
_BOARD_COLOR = '#006622'
_BOARD_EDGES = 20


class OthelloDisc:
    '''
    A class that creates an othello_disc object containing
    the following information: its color and its bounding box
    coordinates
    '''
    def __init__(self, row_num: int, column_num: int,
                 total_row: int, total_column: int, color: str,
                 canvas_width: int, canvas_height: int):
        if color == 'B':
            self._color = '#000000'

        elif color == 'W':
            self._color = '#ffffff'

        grid_width = (canvas_width - 2 * _BOARD_EDGES) / total_column
        grid_height = (canvas_height - 2 * _BOARD_EDGES) / total_row
        
        center_x = _BOARD_EDGES + 1/2 * grid_width + (column_num * grid_width)
        center_y = _BOARD_EDGES + 1/2 * grid_height + (row_num * grid_height)
        
        self._x0 = center_x - 0.45 * grid_width
        self._y0 = center_y - 0.45 * grid_height
        self._x1 = center_x + 0.45 * grid_width
        self._y1 = center_y + 0.45 * grid_height


class InvalidDialog:
    '''
    creates a tkinter.Toplevel object centered on the game_window
    that tells the user they made an invalid move
    '''
    def __init__(self, parent_x: int, parent_y: int,
                 parent_width: int, parent_height: int):
        self._invalid_dialog = tkinter.Toplevel()
        self._invalid_dialog.wm_title('Invalid Move')

        self._invalid_dialog.geometry(('%dx%d+%d+%d' % (300, 80,
                                                        parent_x + parent_width / 2 - 150,
                                                        parent_y + parent_height / 2 - 40)))

        invalid_label = tkinter.Label(self._invalid_dialog,
                                      text = "That's an invalid move!")
        invalid_label.grid(row = 0, column = 0, pady = 5,
                           sticky = tkinter.S)

        resume_button = tkinter.Button(self._invalid_dialog,
                                       text = 'Resume Game',
                                       command = self.on_resume)
        resume_button.grid(row = 1, column = 0, pady = 5, sticky = tkinter.N)

        self._invalid_dialog.rowconfigure(0, weight = 1)
        self._invalid_dialog.rowconfigure(1, weight = 1)
        self._invalid_dialog.columnconfigure(0, weight = 1)

    def on_resume(self):
        '''
        destroys the dialog when the resume button is pressed
        '''
        self._invalid_dialog.destroy()
        
    def show(self):
        self._invalid_dialog.grab_set()
        self._invalid_dialog.wait_window()


class GameWindow:
    '''
    creates a tkinter.Tk object that acts as a GUI through
    which a user(s) can play a game of othello
    '''
    def __init__(self):
        self._game_window = tkinter.Tk()    
        self._game_window.wm_title('Othello')

        '''places window in the middle of the screen'''
        screen_width = self._game_window.winfo_screenwidth()
        screen_height = self._game_window.winfo_screenheight()
        
        self._game_window.geometry(('%dx%d+%d+%d' % (750, 820,
                                                     screen_width / 2 - 375,
                                                     screen_height / 2 - 410)))

                         
        self._othello_game = othello_model.OthelloGame()


        '''settings up variable objects for the game window'''
        self._black_count_variable = tkinter.IntVar()
        self._white_count_variable = tkinter.IntVar()
        self._status_variable = tkinter.StringVar()



        '''scoreboard components'''
        score_frame = tkinter.Frame(self._game_window)
        score_frame.grid(row = 0, column = 0)

        score_label = tkinter.Label(score_frame, text = 'Scoreboard',
                                    font = _DEFAULT_FONT)
        score_label.grid(row = 0, column = 0, columnspan = 4, pady = 5)

        black_label = tkinter.Label(score_frame, text = 'Black: ',
                                    font = _DEFAULT_FONT)
        black_label.grid(row = 1, column = 0)


        self._black_count_label = tkinter.Label(score_frame, textvariable = self._black_count_variable,
                                                font = _DEFAULT_FONT)
        self._black_count_label.grid(row = 1, column = 1)


        white_label = tkinter.Label(score_frame,text = 'White: ',
                                    font = _DEFAULT_FONT)
        white_label.grid(row = 1, column = 2)
        

        self._white_count_label = tkinter.Label(score_frame, textvariable = self._white_count_variable,
                                                font = _DEFAULT_FONT)
        self._white_count_label.grid(row = 1, column = 3)
        



        '''the canvas to simulate the game board and the start game button'''
        self._board_canvas = tkinter.Canvas(master = self._game_window,
                                            background = _BOARD_COLOR)
        self._board_canvas.grid(row = 1, column = 0,columnspan = 4, padx = 10,
                                sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)


        self._start_game_button = tkinter.Button(master = self._board_canvas,background = _BOARD_COLOR,
                                                 activeforeground = _BOARD_COLOR,
                                                 activebackground = _BOARD_COLOR,
                                                 bd = 0, width = 50, height = 27,
                                                 text = 'Click here to start a game',
                                                 font = _DEFAULT_FONT,
                                                 command = self.start_game_clicked)

        self._start_game_button.pack(fill = tkinter.BOTH, expand = 1)
                                           

        '''game status label'''
        self._status_label = tkinter.Label(self._game_window,
                                           textvariable = self._status_variable,
                                           font = _DEFAULT_FONT)
        self._status_label.grid(row = 2, column = 0, columnspan = 4, pady = 5)



        self._game_window.rowconfigure(1, weight = 1)
        self._game_window.columnconfigure(0, weight = 1)



    def on_canvas_resized(self, event: tkinter.Event) -> None:
        self._board_canvas.delete(tkinter.ALL)
        self.update_widgets()

    def on_canvas_clicked(self, event: tkinter.Event) -> None:
        '''response to a canvas click(user making a move)'''
        canvas_width = self._board_canvas.winfo_width()
        canvas_height = self._board_canvas.winfo_height()

        grid_width = (canvas_width - 2 * _BOARD_EDGES) / len(self._othello_game._board[0])
        grid_height = (canvas_height - 2 * _BOARD_EDGES) / len(self._othello_game._board)
        
        row_num = int((event.y - _BOARD_EDGES) // grid_height)
        column_num = int((event.x - _BOARD_EDGES) // grid_width)

        window_x = self._game_window.winfo_x()
        window_y = self._game_window.winfo_y()

        window_width = self._game_window.winfo_width()
        window_height = self._game_window.winfo_height()

        try:
            if self._othello_game.is_valid(row_num, column_num):
                self._othello_game.reverse(row_num, column_num)
                self._othello_game.count_discs()
                self._othello_game.next_turn()
                self.update_widgets()
                
            else:
                invalid_dialog = InvalidDialog(window_x, window_y, window_width, window_height)
                invalid_dialog.show()

        except othello_model.GameOverError:
            pass
            

    def start_game_clicked(self) -> None:
        '''
        Shows the settings window dialog when the
        game window's start button is clicked and
        then removing the button if the game was
        started with proper settings
        '''
        try:
            window_x = self._game_window.winfo_x()
            window_y = self._game_window.winfo_y()

            window_width = self._game_window.winfo_width()
            window_height = self._game_window.winfo_height()
            
            settings_window = othello_view_settings.SettingsWindow(window_x,
                                                                   window_y,
                                                                   window_width,
                                                                   window_height)
            settings_window.show()

            self._othello_game._settings = settings_window._settings
            self._othello_game.new_game()
        
            self._board_canvas.bind('<Configure>', self.on_canvas_resized)
            self._board_canvas.bind('<Button-1>', self.on_canvas_clicked)
        
            self._start_game_button.pack_forget()
            self.update_widgets()

        except othello_model.InvalidSettingsError:
            pass

    def update_widgets(self) -> None:
        '''
        makes a call to other attributes that updates
        the window
        '''
        self._update_count()
        self._draw_lines()
        self._draw_discs()
        self._update_status()


    def _update_count(self) -> None:
        '''Updates the discs count on the scoreboard'''
        self._black_count_variable.set(self._othello_game._black_count)
        self._white_count_variable.set(self._othello_game._white_count)

    def _update_status(self) -> None:
        '''
        Updates the label that shows the status
        of the game, printing out whether someone
        has won or whose turn it is
        '''
        if self._othello_game.game_not_over():
            if self._othello_game._turn == 'B':
                self._status_variable.set("Black's turn")

            elif self._othello_game._turn == 'W':
                self._status_variable.set("White's turn")

        else:
            self._othello_game.check_winner()
            if self._othello_game._winner == 'B':
                self._status_variable.set('Black wins!')

            elif self._othello_game._winner == 'W':
                self._status_variable.set('White wins!')

            elif self._othello_game._winner == 'NONE':
                self._status_variable.set("It's a draw!")


    def _draw_lines(self) -> None:
        '''
        draws the lines on the canvas to simulate an othello
        board according to the settings that were input
        '''
        canvas_width = self._board_canvas.winfo_width()
        canvas_height = self._board_canvas.winfo_height()
        
        for row_num in range(len(self._othello_game._board) + 1):
            self._board_canvas.create_line(_BOARD_EDGES - 2,
                                           row_num / len(self._othello_game._board) * (canvas_height - 2 * _BOARD_EDGES) + _BOARD_EDGES,
                                           canvas_width - _BOARD_EDGES + 2,
                                           row_num / len(self._othello_game._board) * (canvas_height - 2 * _BOARD_EDGES) + _BOARD_EDGES,
                                           width = 4)

        for column_num in range(len(self._othello_game._board[0]) +  1):
            self._board_canvas.create_line(column_num / len(self._othello_game._board[0]) * (canvas_width - 2 * _BOARD_EDGES) + _BOARD_EDGES,
                                           _BOARD_EDGES - 2,
                                           column_num / len(self._othello_game._board[0]) * (canvas_width - 2 * _BOARD_EDGES) + _BOARD_EDGES,
                                           canvas_height - _BOARD_EDGES + 2,
                                           width = 4)
                                           
    

    def _draw_discs(self) -> None:
        '''
        draws the discs according to how the board in
        othello_game object looks like
        '''
        canvas_width = self._board_canvas.winfo_width()
        canvas_height = self._board_canvas.winfo_height()
        
        for row_num in range(len(self._othello_game._board)):
            for column_num in range(len(self._othello_game._board[0])):
                if self._othello_game._board[row_num][column_num] == 'B' or \
                   self._othello_game._board[row_num][column_num] == 'W':
                    
                    disc_to_draw = OthelloDisc(row_num, column_num,
                                               len(self._othello_game._board),
                                               len(self._othello_game._board[0]),
                                               self._othello_game._board[row_num][column_num],
                                               canvas_width, canvas_height)
                    
                    self._board_canvas.create_oval(disc_to_draw._x0,
                                                   disc_to_draw._y0,
                                                   disc_to_draw._x1,
                                                   disc_to_draw._y1,
                                                   fill = disc_to_draw._color)

    def run(self) -> None:
        self._game_window.mainloop()

