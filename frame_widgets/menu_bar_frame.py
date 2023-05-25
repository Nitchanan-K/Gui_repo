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


class Menu_bar(ttk.Frame):

    def __init__(self):
        ttk.Frame.__init__(self)

        #

