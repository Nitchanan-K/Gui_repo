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
from tkinter import filedialog

from function_gui import ask_choose_file
dataframe = ask_choose_file.ask_choose_file_func
def get_data_frame():

    try:
        df_content = dataframe.df_content
        return df_content
    except AttributeError:
        messagebox.showerror(title="Error!",message="Please select your data")

