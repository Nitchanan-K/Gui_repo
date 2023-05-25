# import libraries
# Panda Dataframe
# tabulate
# Matplotlib
import matplotlib
matplotlib.use('TKAgg')
# import GUI
from tkinter import *
from tkinter import ttk
# import filedialog for gui save
# import backtest lib
# get list data name
from crypto_data_list_top100.crypto_list_api_ticker_name import list_a
list_a_copy = list_a
# import request and API data download

# Import functions
from function_gui import ask_choose_file
from function_gui import label_change_file_select_func

class Data_select_frame(ttk.Frame):

    # setup functions
    ask_choose_file = ask_choose_file.ask_choose_file_func
    label_data_change_file_select = label_change_file_select_func.label_data_change_from_file_select

    def __init__(self):
        ttk.Frame.__init__(self)

        # Create a Frame for data select frame
        self.data_frame = ttk.LabelFrame(master=self, text="Select Data To Backtesting", padding=(20, 10))
        self.data_frame.grid(row=0, column=2, rowspan=1,
                             padx=(20, 10), pady=(20, 10), sticky="nsew"
                             )

        # Create a label in Frame of select data
        self.label_data = ttk.Label(master=self.data_frame, text="Data File (.CSV)", justify="center",
                                    font=("-size", 15, "-weight", "bold"))
        self.label_data.grid(row=0, column=1, columnspan=2, padx=5, pady=10, sticky="nsew"
                             )

        # Create a Treeview data
        self.paned = ttk.PanedWindow(master=self.data_frame, orient=VERTICAL, width=650)
        self.paned.grid(row=1, column=1, pady=(25, 5), sticky="nsew", rowspan=2
                        )

        # Pane # 1
        self.pane_1 = ttk.Frame(self.paned, padding=5)
        self.paned.add(self.pane_1, weight=1)

        # Pane # 2
        self.pane_1_2 = ttk.Frame(self.paned, padding=5)
        self.paned.add(self.pane_1_2, weight=1)

        # Scrollbar
        self.scrollbar_y = ttk.Scrollbar(self.pane_1)
        self.scrollbar_y.pack(side="right", fill="y")

        # Create Treeview for review data we selected
        self.tree_view_show_data = ttk.Treeview(master=self.pane_1,
                                                selectmode="browse",
                                                yscrollcommand=self.scrollbar_y.set,
                                                columns=("2"),
                                                height=10,
                                                )

        self.tree_view_show_data.pack(expand=True, fill="both")
        self.scrollbar_y.config(command=self.tree_view_show_data.yview)

        # Accentbutton_select_data_file
        self.accent_button_save_plot_data = ttk.Button(master=self.pane_1_2, text="select data file",
                                                       style="Accent.TButton"
                                                       )
        self.accent_button_save_plot_data['command'] = self.ask_choose_file
        self.accent_button_save_plot_data['command'] = self.label_data_change_file_select
        self.accent_button_save_plot_data.pack(expand=False, padx=5, pady=5, fill="both")














