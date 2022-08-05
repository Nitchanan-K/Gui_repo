# Import file dialog
from tkinter import filedialog
# Panda Dataframe
import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox
from function_gui import clear_tree

def ask_choose_file_func(self):
    # 1). ask file to open and use in the Run_start
    # import function clear_tree
    clear = clear_tree.clear_tree_func
    global tree_view_show_data

    with filedialog.askopenfile(mode='r', filetypes=[('CSV Files', '*.csv'),("Excel files", ".xlsx .xls")]) as file:
                # make data that openwith askopenfile to Dataframe content
                #df_content = pd.read_csv(file,index_col='Date', parse_dates=True) # may add df.read_xlsx later for xlsx content
                df_content = pd.read_csv(file, index_col='Date',
                                         parse_dates=True)  # may add df.read_xlsx later for xlsx content
                # give function this attribute  .df_content for use as variable in Run_start() function
                ask_choose_file_func.df_content = df_content
                ask_choose_file_func.name = file.name
    # 2). after load file we get file data and put it into the treeview
                # clear tree
                clear(self)
                # add data to treeview
                self.tree_view_show_data['column'] = list(df_content.columns)
                self.tree_view_show_data['show'] = "headings"
                # Loop thru column list for headers
                for column in self.tree_view_show_data["column"]:
                    self.tree_view_show_data.column(column, anchor=CENTER, stretch=NO,minwidth=70,width=100)
                    self.tree_view_show_data.heading(column, text=column)

                # put data in treeview
                df_content_row = df_content.to_numpy().tolist()
                for row in df_content_row:
                    self.tree_view_show_data.insert('','end',values=row)

                return file.name,df_content

