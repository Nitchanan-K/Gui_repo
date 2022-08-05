# import libraries
# Panda Dataframe
# tabulate
# import GUI
from tkinter import *
from tkinter import ttk
# import filedialog for gui save
# import backtest lib
# get list data name
from crypto_data_list_top100.crypto_list_api_ticker_name import list_a
list_a_copy = list_a
# import request and API data download

# import function
from function_gui import search_crypto_tree_func,reset_crypto_tree_func,select_download_data_name_func
from function_gui import download_crypto_data,switch_theme_func

class Data_download_API(ttk.Frame):
    # setup functions
    search_crypto = search_crypto_tree_func.search_crypto_tree
    reset_crypto_tree = reset_crypto_tree_func.Reset
    select_download_data_name = select_download_data_name_func.select_data_name
    download_crypto_data = download_crypto_data.crypto_download_data
    switch_theme_func = switch_theme_func.change_theme

    def __init__(self):
        ttk.Frame.__init__(self)

        # text variable
        self.search_entry_box_text = StringVar()
        self.on_and_off_var = IntVar()
        # make download_data_frame
        self.download_data_frame = ttk.LabelFrame(master=self, text="Download Data From API", padding=(20, 10))
        self.download_data_frame.grid(row=0, column=4, rowspan=2, columnspan=2,
                                      padx=(20, 10), pady=(20, 10), sticky="nsew"
        )

        # Text label download_data_frame
        self.label_tree_view = ttk.Label(master=self.download_data_frame, text="Trading pairs", justify="center",
                                         font=("-size", 15, "-weight", "bold")
        )
        self.label_tree_view.grid(row=0, column=0, columnspan=3, padx=5, pady=10, sticky="nsew")

        # make switch for change theme
        '''
        self.switch_theme = ttk.Checkbutton(master=self.download_data_frame,
                                            text='Theme', style="Switch.TCheckbutton",variable=self.on_and_off_var,
                                            offvalue=False,onvalue=True)
        self.switch_theme.grid(row=0, column=2, padx=1, pady=1, sticky="nsew")
        self.switch_theme['command'] = self.switch_theme_func
        '''

        # Create Panedwindow for treeview
        self.paned_2 = ttk.PanedWindow(master=self.download_data_frame)
        self.paned_2.grid(row=1, column=1, pady=(25, 5), sticky="nsew", rowspan=2)
        # Pane # 1
        self.pane_2_1 = ttk.Frame(self.paned_2, padding=5)
        self.paned_2.add(self.pane_2_1, weight=1)
        # Pane # 2
        self.pane_2_2 = ttk.Frame(self.paned_2, padding=5)
        self.paned_2.add(self.pane_2_2, weight=1)
        # Pane # 3
        self.pane_2_3 = ttk.Frame(self.paned_2, padding=10)
        self.paned_2.add(self.pane_2_3, weight=1)

        # Scrollbar
        self.scrollbar_y = ttk.Scrollbar(self.pane_2_1)
        self.scrollbar_y.pack(side="right", fill="y")

        # Treeview
        self.tree_view_crypto_name = ttk.Treeview(master=self.pane_2_1,
                                                  yscrollcommand=self.scrollbar_y.set,
                                                  height=10,
                                                  selectmode="browse"
                                                  )

        self.tree_view_crypto_name.pack(expand=True, fill="both")
        self.scrollbar_y.config(command=self.tree_view_crypto_name.yview)

        # Columns
        self.tree_view_crypto_name['columns'] = ('Crypto/USD')
        self.tree_view_crypto_name.column('#0', width=0, stretch=NO)
        self.tree_view_crypto_name.column('Crypto/USD')

        self.tree_view_crypto_name.heading('#0', text='', anchor=CENTER)
        self.tree_view_crypto_name.heading('Crypto/USD', text='Crypto/USD', anchor=CENTER)

        # pass data in to treeview
        for item in list_a_copy:
            self.tree_view_crypto_name.insert('', 'end', values=item)

        # Add Buttons into Pane_2 master

        # Add entry box
        self.search_entry = ttk.Entry(master=self.pane_2_2, font=("Helvetica", 10), textvariable=self.search_entry_box_text)
        self.search_entry.pack(expand=True, padx=5, pady=5, fill="both")
        # Search Button
        self.search_button = ttk.Button(master=self.pane_2_2, text="Search")
        self.search_button.pack(expand=True, padx=5, pady=5, fill="both", side=LEFT)
        self.search_button['command'] = self.search_crypto
        # reset Button
        self.reset_button = ttk.Button(master=self.pane_2_2, text="Reset")
        self.reset_button.pack(expand=True, padx=5, pady=5, fill="both", side=RIGHT)
        self.reset_button['command'] = self.reset_crypto_tree

        # select name button
        self.select_button = ttk.Button(master=self.pane_2_3, text="Select")
        self.select_button.pack(expand=True, padx=5, pady=5, fill="both")
        self.select_button['command'] = self.select_download_data_name

        # Create Frame for data download and setting data
        ##############################################################################################################
        # make setting_dataframe
        self.setting_dataframe = ttk.LabelFrame(master=self.download_data_frame , text="Setting Data", padding=(20, 10))
        self.setting_dataframe.grid(row=5, column=1, rowspan=3, columnspan=2,
                               padx=(10, 10), pady=(10, 10), sticky="nsew"
                               )

        # Button and Entry in  data download and setting data

        # From date Entry box
        self.from_date_entry = ttk.Entry(master=self.setting_dataframe, justify=CENTER, font=("-size", 10))
        self.from_date_entry.insert(0, "00/00/0000")
        self.from_date_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

        # Label from date
        self.label_from_date = ttk.Label(master=self.setting_dataframe, text="From Date: MM/DD/YYYY",
                                    font=("-size", 10, "-weight", "bold"), justify=CENTER)
        self.label_from_date.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

        # To date Entry box
        self.to_date_entry = ttk.Entry(master=self.setting_dataframe, justify=CENTER, font=("-size", 10))
        self.to_date_entry.insert(0, "00/00/0000")
        self.to_date_entry.grid(row=1, column=3, columnspan=2, padx=5, pady=5)

        # Label from date
        self.label_to_date = ttk.Label(master=self.setting_dataframe, text="To Date: MM/DD/YYYY",
                                  font=("-size", 10, "-weight", "bold"), justify=CENTER)
        self.label_to_date.grid(row=0, column=3, columnspan=2, padx=5, pady=5)

        # Separator
        self.separator_data_setting = ttk.Separator(master=self.setting_dataframe, orient=VERTICAL)
        self.separator_data_setting.grid(row=0, column=2, columnspan=2, sticky="ns", rowspan=10)

        # download button
        self.download_button = ttk.Button(master=self.setting_dataframe, text="Download Data")
        self.download_button.grid(row=4, column=3, columnspan=2, padx=8, pady=8)
        self.download_button['command'] = self.download_crypto_data

        # Button of interval time info
        self.list_of_interval_time = ["1d", "1wk", "1mo", "1m"]
        self.interval_time_combo_box = ttk.Combobox(master=self.setting_dataframe, values=self.list_of_interval_time)
        self.interval_time_combo_box.current(0)
        self.interval_time_combo_box.grid(row=4, column=1, columnspan=2, padx=5, pady=5)
        #self.interval_time_combo_box.bind('<<ComboBoxSelected>>', crypto_download_data)



