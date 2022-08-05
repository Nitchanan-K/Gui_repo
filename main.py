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
# import request and API data download
# import widgets file
from frame_widgets import strategy_frame,trade_setup_frame,data_select_frame,\
    plot_save_data_frame,data_download_from_API_frame

class MainApp(ttk.Frame):

    # setup frame variable
    strategy_frame = strategy_frame.Strategy_frame_widget
    trade_setup_frame = trade_setup_frame.Trade_setup_frame
    data_select_frame = data_select_frame.Data_select_frame
    plot_save_data_frame = plot_save_data_frame.Plot_save_data
    data_download_from_api = data_download_from_API_frame.Data_download_API

    def __init__(self,parent,*args,**kwargs):
        ttk.Frame.__init__(self,parent, *args, **kwargs)
        self.parent = parent


        for index in [0, 1, 2, 3, 4]:
            self.columnconfigure(index=index, weight=1)
            self.rowconfigure(index=index, weight=1)

        # Create frame and widgets
        self.strategy_frame().grid(row=0, column=0, rowspan=1,
                                   padx=(20, 10), pady=(20, 10), sticky="nsew"
        )

        self.trade_setup_frame().grid(row=1, column=0, rowspan=1,
                                      padx=(20, 10), pady=(20, 10), sticky="n"
        )

        self.data_select_frame().grid(row=0, column=1, rowspan=1,
                                      padx=(20, 10), pady=(20, 10), sticky="n"
        )

        self.plot_save_data_frame().grid(row=1, column=1,
                                         padx=(20, 10), pady=(20, 10), sticky="n"
        )

        self.data_download_from_api().grid(row=0, column=4, rowspan=2, columnspan=2,
                                           padx=(20, 10), pady=(20, 10), sticky="nsew"
        )


if __name__ == "__main__":

    root = tk.Tk()
    MainApp(root)

# Call Theme azure
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "dark")
# set Title
    root.title("BackTesting GUI")


    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate - 20))

    root.mainloop()






















