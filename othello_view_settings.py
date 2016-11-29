import othello_model
import tkinter

class SettingsWindow:
    def __init__(self):
        self._settings_window = tkinter.Tk()
        self._settings_window.wm_title('Othello Settings')
        self._settings = othello_model.OthelloSettings()


        row_label = tkinter.Label(self._settings_window,
                                  text = 'Number of rows:')
        row_label.grid(row = 0, column = 0, sticky = tkinter.W)


        column_label = tkinter.Label(self._settings_window,
                                     text = 'Number of columns:')
        column_label.grid(row = 1, column = 0, sticky = tkinter.W)


        first_move_label = tkinter.Label(self._settings_window,
                                         text = 'First move:')
        first_move_label.grid(row = 2, column = 0, sticky = tkinter.W)


        top_left_label = tkinter.Label(self._settings_window,
                                       text = 'Color of top left disc:')
        top_left_label.grid(row = 3, column = 0, sticky = tkinter.W)
        

        more_or_less_label = tkinter.Label(self._settings_window,
                                           text = 'More or less to win:')
        more_or_less_label.grid(row = 4, column = 0, sticky = tkinter.W)



        '''ROW DROPDOWN'''
        self._row_variable = tkinter.IntVar(self._settings_window)
        self._row_variable.set(4)

        row_option_menu = tkinter.OptionMenu(self._settings_window,
                                             self._row_variable,
                                             4, 6, 8, 10, 12, 14, 16)

        row_option_menu.grid(row = 0, column = 1, sticky = tkinter.E)



        '''COLUMN DROPDOWN'''
        self._column_variable = tkinter.IntVar(self._settings_window)
        self._column_variable.set(4)

        column_option_menu = tkinter.OptionMenu(self._settings_window,
                                                self._column_variable,
                                                4, 6, 8, 10, 12, 14, 16)

        column_option_menu.grid(row = 1, column = 1, sticky = tkinter.E)



        '''FIRST MOVE DROPDOWN'''
        self._first_move_variable = tkinter.StringVar(self._settings_window)
        self._first_move_variable.set('B')

        first_move_option_menu = tkinter.OptionMenu(self._settings_window,
                                                    self._first_move_variable,
                                                    'B', 'W')

        first_move_option_menu.grid(row = 2, column = 1, sticky = tkinter.E)



        '''TOP LEFT DROPDOWN'''
        self._top_left_variable = tkinter.StringVar(self._settings_window)
        self._top_left_variable.set('B')

        top_left_option_menu = tkinter.OptionMenu(self._settings_window,
                                                  self._top_left_variable,
                                                  'B', 'W')

        top_left_option_menu.grid(row = 3, column = 1, sticky = tkinter.E)




        '''MORE OR LESS DROPDOWN'''
        self._more_or_less_variable = tkinter.StringVar(self._settings_window)
        self._more_or_less_variable.set('>')

        more_or_less_option_menu = tkinter.OptionMenu(self._settings_window,
                                                      self._more_or_less_variable,
                                                      '>', '<')

        more_or_less_option_menu.grid(row = 4, column = 1, sticky = tkinter.E)


        

        '''OK BUTTON'''
        ok_button = tkinter.Button(master = self._settings_window,
                                   text = 'OK',
                                   font = ('Arial', 14),
                                   command = self._on_ok_button_pressed)

        ok_button.grid(row = 5, column = 1, sticky = tkinter.E)


    def run(self):
        self._settings_window.mainloop()

    def _on_ok_button_pressed(self):
        self._settings._rows = self._row_variable.get()
        self._settings._columns = self._column_variable.get()
        self._settings._first_move = self._first_move_variable.get()
        self._settings._top_left = self._top_left_variable.get()
        self._settings._more_or_less = self._more_or_less_variable.get()
        
        self._settings_window.quit()
        self._settings_window.destroy()
