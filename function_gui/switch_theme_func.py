# Panda Dataframe
# tabulate
# Matplotlib
import matplotlib
matplotlib.use('TKAgg')
# import GUI
import tkinter as tk
from tkinter import ttk
# import filedialog for gui save
# import backtest lib
# get list data name
from crypto_data_list_top100.crypto_list_api_ticker_name import list_a
list_a_copy = list_a

def change_theme(self):
    print(self.on_and_off_var.get())
    if self.on_and_off_var.get() == True and self.tk.call("ttk::style", "theme", "use") == "azure-dark":
        # Set light theme
        self.tk.call("set_theme", "light")
    else:
        # Set dark theme
        self.tk.call("set_theme", "dark")