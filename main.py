import PySimpleGUI as sg
import os
import time
import pandas as pd
import numpy as np
import matplotlib


class MainWindow:

    def __init__(self):
        self.filename = None

    def first_window(self):
        layout1 = [[sg.Text("Welcome to DataGenie, your Data Analyst!")], [sg.Button("Continue")]]

        first_window = sg.Window(title="DataGenie", layout=layout1, size=(400, 250))
        while True:
            event, values = first_window.read()
            if event == "Continue" or event == sg.WIN_CLOSED:
                break
        first_window.close()

    def get_filename(self):
        filename = sg.popup_get_file(
            'filename to open', no_window=True, file_types=(("CSV Files", "*.csv"),))
        # --- populate table with file contents --- #
        return filename

    def file_window(self):
        sg.theme("DarkTeal")
        layout = [[sg.T("")], [sg.Text("Choose a file (.xlsx or .csv)> "), sg.Input(), sg.FileBrowse(key="-IN-")],
                  [sg.Button("Ok")]]
        file_window = sg.Window('File Browser', layout, size=(600, 150))

        while True:
            event, values = file_window.read()
            if event == sg.WIN_CLOSED or event == "Exit":
                exit()
            elif event == "Browse":
                self.get_filename
            if event == "Ok":
                break
        file_window.close()

    def dataframe_window(self):
        data = []
        header_list = []
        colnames_prompt = sg.popup_yes_no('Does this file have column names already?')
        fname = self.filename
        if fname is not None:
            fn = fname.split('/')[-1]
            try:
                if colnames_prompt == 'Yes':
                    df = pd.read_csv(fname, sep=',', engine='python')
                    # Uses the first row (which should be column names) as columns names
                    header_list = list(df.columns)
                    # Drops the first row in the table (otherwise the header names and the first row will be the same)
                    data = df[1:].values.tolist()
                else:
                    df = pd.read_csv(fname, sep=',', engine='python', header=None)
                    # Creates columns names for each column ('column0', 'column1', etc)
                    header_list = ['column' + str(x) for x in range(len(df.iloc[0]))]
                    df.columns = header_list
                    # read everything else into a list of rows
                    data = df.values.tolist()
            except:
                sg.popup_error('Error reading file')

        layout = [
            [sg.Table(values=data,
                      headings=header_list,
                      display_row_numbers=True,
                      auto_size_columns=False,
                      num_rows=min(25, len(data)))]
        ]


main_wd = MainWindow()

main_wd.first_window()
time.sleep(1.0)
main_wd.file_window()
time.sleep(1.0)
main_wd.dataframe_window()
