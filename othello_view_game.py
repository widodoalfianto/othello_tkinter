import tkinter
import othello_view_settings
import othello_model


class OthelloDisc:
    def __init__(self, row_num: int, column_num: int,
                 total_row: int, total_column: int,
                 color: str):
        if color == 'B':
            self._color = '#000000'

        elif color == 'W':
            self._color = '#ffffff'


        self._center = [1 /(2 * total_column) + column_num / total_column,
                        1 /(2 * total_row) + row_num / total_row]
        
        self._x0 = self._center[0] - 1 / (2 * total_column)
        self._y0 = self._center[1] - 1 / (2 * total_row)
        self._x1 = self._center[0] + 1 / (2 * total_column)
        self._y1 = self._center[1] + 1 / (2 * total_row)
    

class GameWindow:
    def __init__(self, s: othello_model.OthelloSettings):
        self._game_window = tkinter.Tk()
        
        self._othello_game = othello_model.OthelloGame()
        self._othello_game._settings = s

        self._count_variable = tkinter.StringVar()
        self._turn_variable = tkinter.StringVar()

        
        self._othello_game.new_game()
        

        self._count_label = tkinter.Label(self._game_window,
                                        textvariable = self._count_variable)
        
        self._count_label.grid(row = 0, column = 0,
                             sticky = tkinter.N + tkinter.E + tkinter.W)


        
        self._canvas_board = tkinter.Canvas(master = self._game_window,
                                            width = 600, height = 600,
                                            background = '#179443')

        self._canvas_board.grid(row = 1, column = 0,
                         padx = 10, pady = 10,
                         sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)



        self._canvas_board.bind('<Configure>', self.on_canvas_resized)
        self._canvas_board.bind('<Button-1>', self.on_canvas_clicked)



        self._turn_label = tkinter.Label(self._game_window,
                                         textvariable = self._turn_variable)
        self._turn_label.grid(row = 2, column = 0,
                            sticky = tkinter.S + tkinter.E + tkinter.W)



        self._game_window.rowconfigure(1, weight = 1)
        self._game_window.columnconfigure(0, weight = 1)



    def on_canvas_resized(self, event: tkinter.Event) -> None:
        self._canvas_board.delete(tkinter.ALL)
        self.update_window()

    def on_canvas_clicked(self, event: tkinter.Event) -> None:
        width = self._canvas_board.winfo_width()
        height = self._canvas_board.winfo_height()

        row_num = int(event.y / height * len(self._othello_game._board))
        column_num = int(event.x / width * len(self._othello_game._board[0]))

        if self._othello_game.is_valid(row_num, column_num):
            self._othello_game.reverse(row_num, column_num)
            self._othello_game.count_discs()
            self._othello_game.next_turn()
            self.update_window()
            
            if self._othello_game.check_game_over():
                self.update_window()

            else:
                print('GAME OVER')
            


    def run(self) -> None:
        self._game_window.mainloop()


    def update_window(self) -> None:
        self.update_count()
        self.draw_board()
        self.update_turn()


    def update_count(self) -> None:
        self._count_variable.set('Black : ' + str(self._othello_game._black_count) + 10 * ' ' + \
                                 'White : ' + str(self._othello_game._white_count))
        

    def draw_board(self) -> None:
        self.draw_lines()
        self.draw_discs()


    def update_turn(self) -> None:
        self._turn_variable.set('Turn : ' + self._othello_game._turn)


    def draw_lines(self) -> None:
        width = self._canvas_board.winfo_width()
        height = self._canvas_board.winfo_height()

        
        for row_num in range(len(self._othello_game._board)):
            self._canvas_board.create_line(0, row_num / len(self._othello_game._board) * height,
                                           width, row_num / len(self._othello_game._board) * height)

        for column_num in range(len(self._othello_game._board[0])):
            self._canvas_board.create_line(column_num / len(self._othello_game._board[0]) * width, 0,
                                           column_num / len(self._othello_game._board[0]) * width, height)
                                           
    

    def draw_discs(self) -> None:
        width = self._canvas_board.winfo_width()
        height = self._canvas_board.winfo_height()
        
        for row_num in range(len(self._othello_game._board)):
            for column_num in range(len(self._othello_game._board[0])):
                if self._othello_game._board[row_num][column_num] == 'B' or \
                   self._othello_game._board[row_num][column_num] == 'W':
                    
                    disc_to_draw = OthelloDisc(row_num, column_num,
                                               len(self._othello_game._board),
                                               len(self._othello_game._board[0]),
                                               self._othello_game._board[row_num][column_num])
                    
                    self._canvas_board.create_oval(disc_to_draw._x0 * width,
                                                   disc_to_draw._y0 * height,
                                                   disc_to_draw._x1 * width,
                                                   disc_to_draw._y1 * height,
                                                   fill = disc_to_draw._color)


s = othello_view_settings.SettingsWindow()
s.run()
a = GameWindow(s._settings)
a.run()
