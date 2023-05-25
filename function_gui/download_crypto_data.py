# import libraries
# Panda Dataframe
import pandas as pd
# tabulate
from tabulate import tabulate
# import filedialog for gui save
from tkinter import filedialog
# import request and API data download
from yahoo_fin.stock_info import *
from yahoo_fin.stock_info import get_analysts_info
import yahoo_fin.stock_info as si
from tkinter import messagebox

def crypto_download_data(self):
    global list_a_copy
    # download data file from API Yahoo Finance
    from function_gui import get_select_data_downloaded_text_func

    data_name = get_select_data_downloaded_text_func.get_data_name()

    data_downloaded = get_data(data_name, start_date=self.from_date_entry.get(), end_date=self.to_date_entry.get(), index_as_date=False,
             interval=self.interval_time_combo_box.get())

    # pass to Data Frame
    df = pd.DataFrame(data_downloaded)
    # set Data Frame Columns
    df.drop(columns='ticker', inplace=True)
    df.rename(columns={'date': 'Date', 'open': 'Open', 'high': 'High', 'low': 'Low', 'close': 'Close',
                       'adjclose': 'Adjclose', 'volume': 'Volume'}, inplace=True)
    df.reset_index(drop=True, inplace=True)

    # open location to save file
    try:
        with filedialog.asksaveasfile(mode='w', defaultextension=".csv") as file:
            df.to_csv(file.name, index=False)

    except:
        print("The user cancelled save")
