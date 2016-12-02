import othello_model
import tkinter

class SettingsWindow:
    def __init__(self):
        self._settings_window = tkinter.Toplevel()
        self._settings_window.wm_title('Othello Settings')
        self._settings = othello_model.OthelloSettings()

        instruction_label = tkinter.Label(self._settings_window,
                                           text = 'Please specify the game settings')
        instruction_label.grid(row = 0, column = 0, columnspan = 2,
                                     sticky = tkinter.S, pady = 10)

        
        row_label = tkinter.Label(self._settings_window,
                                  text = 'Number of rows:', width = 25,
                                  anchor = tkinter.W)
        row_label.grid(row = 1, column = 0, sticky = tkinter.E + tkinter.S,
                       padx = 10, pady = 5)


        column_label = tkinter.Label(self._settings_window,
                                     text = 'Number of columns:', width = 25,
                                     anchor = tkinter.W)
        column_label.grid(row = 2, column = 0,
                          sticky = tkinter.E + tkinter.S,
                          padx = 10, pady = 5)


        first_move_label = tkinter.Label(self._settings_window,
                                         text = 'First move:', width = 25,
                                         anchor = tkinter.W)
        first_move_label.grid(row = 3, column = 0,
                              sticky = tkinter.E + tkinter.S,
                              padx = 10, pady = 5)


        top_left_label = tkinter.Label(self._settings_window,
                                       text = 'Color of top left disc:', width = 25,
                                       anchor = tkinter.W)
        top_left_label.grid(row = 4, column = 0,
                            sticky = tkinter.E + tkinter.S,
                            padx = 10, pady = 5)
        

        more_or_less_label = tkinter.Label(self._settings_window,
                                           text = 'More or less to win:', width = 25,
                                           anchor = tkinter.W)
        more_or_less_label.grid(row = 5, column = 0,
                                sticky = tkinter.E + tkinter.S,
                                padx = 10, pady = 5)



        '''ROW DROPDOWN'''
        self._row_variable = tkinter.IntVar(self._settings_window)
        self._row_variable.set(4)

        row_option_menu = tkinter.OptionMenu(self._settings_window,
                                             self._row_variable,
                                             4, 6, 8, 10, 12, 14, 16)

        row_option_menu.grid(row = 1, column = 1,
                             sticky = tkinter.W + tkinter.S,
                             padx = 10)



        '''COLUMN DROPDOWN'''
        self._column_variable = tkinter.IntVar(self._settings_window)
        self._column_variable.set(4)

        column_option_menu = tkinter.OptionMenu(self._settings_window,
                                                self._column_variable,
                                                4, 6, 8, 10, 12, 14, 16)

        column_option_menu.grid(row = 2, column = 1,
                                sticky = tkinter.W + tkinter.S,
                                padx = 10)



        '''FIRST MOVE DROPDOWN'''
        self._first_move_variable = tkinter.StringVar(self._settings_window)
        self._first_move_variable.set('B')

        first_move_option_menu = tkinter.OptionMenu(self._settings_window,
                                                    self._first_move_variable,
                                                    'B', 'W')

        first_move_option_menu.grid(row = 3, column = 1,
                                    sticky = tkinter.W + tkinter.S,
                                    padx = 10)



        '''TOP LEFT DROPDOWN'''
        self._top_left_variable = tkinter.StringVar(self._settings_window)
        self._top_left_variable.set('B')

        top_left_option_menu = tkinter.OptionMenu(self._settings_window,
                                                  self._top_left_variable,
                                                  'B', 'W')

        top_left_option_menu.grid(row = 4, column = 1,
                                  sticky = tkinter.W + tkinter.S,
                                  padx = 10)




        '''MORE OR LESS DROPDOWN'''
        self._more_or_less_variable = tkinter.StringVar(self._settings_window)
        self._more_or_less_variable.set('>')

        more_or_less_option_menu = tkinter.OptionMenu(self._settings_window,
                                                      self._more_or_less_variable,
                                                      '>', '<')

        more_or_less_option_menu.grid(row = 5, column = 1,
                                      sticky = tkinter.W + tkinter.S,
                                      padx = 10)


        

        '''Start Game Button'''
        start_button = tkinter.Button(master = self._settings_window,
                                   text = 'Start game with these settings',
                                   font = ('Arial', 10),
                                   command = self.on_start)

        start_button.grid(row = 6, column = 0, sticky = tkinter.N,
                       columnspan = 3, padx = 10, pady = 10)


        self._settings_window.rowconfigure(0, weight = 1)
        self._settings_window.rowconfigure(6, weight = 1)

        self._settings_window.columnconfigure(0, weight = 1)
        self._settings_window.columnconfigure(1, weight = 1)
        
        


    def show(self):
        self._settings_window.grab_set()
        self._settings_window.wait_window()

    def on_start(self):
        self._settings._rows = self._row_variable.get()
        self._settings._columns = self._column_variable.get()
        self._settings._first_move = self._first_move_variable.get()
        self._settings._top_left = self._top_left_variable.get()
        self._settings._more_or_less = self._more_or_less_variable.get()
        
        self._settings_window.destroy()

