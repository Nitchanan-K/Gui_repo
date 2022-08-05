# import lib
# import dataframe
# Panda Dataframe
import pandas as pd
# tabulate
from tabulate import tabulate
# import filedialog for gui save
from tkinter import filedialog


# make func for button to save file to xlsx
def save_file_all_stats_xlsx():
    from function_gui import get_start_func
    start = get_start_func.get_start()

    ##########################################################
    # make DataFrame to pass data from console to DataFrame
    df = pd.DataFrame(start)
    df.drop(labels=['_equity_curve','_trades'],inplace=True)
    # pop up to ask user to save file use filedialog.asksaveasfile and pass data with panda DataFrame
    try:
        with filedialog.asksaveasfile(mode='w', defaultextension=".xlsx") as file:
            df.to_excel(file.name)
    except AttributeError:
        print("The user cancelled save")
'''
    for data from backtader lib
    # this is to make ref set number according to the number of data rows (set colum ref number 1 - n)
    # because when we run plot and save plot data ref is adding itself so we need to set it according to data rows
    # use for loop to check how many row and then add number to ref from 1 to n accordingly to the rows
    for i in range(len(df.loc[:,'ref'])):
        df.loc[i:i, 'ref'] = i+1
    # set ref as index
    df.set_index('ref',inplace=True)
'''