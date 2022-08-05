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

from function_gui import confirm_setup_func,trade_setup_details_config_func

class Trade_setup_frame(ttk.Frame):

    # function
    confirm = confirm_setup_func.confirm_setup
    #trade_setup_detail = trade_setup_details_config_func.trade_setup_details

    def __init__(self):
        ttk.Frame.__init__(self)

        # Create control variables
        self.trade_on_close_var = BooleanVar()
        self.hedging_var = BooleanVar()
        self.exclusive_order_var = BooleanVar()

        # Create Trade_setup_frame
        self.Trade_setup_frame = ttk.LabelFrame(master=self, text="Trade Setup", padding=(20, 10))
        self.Trade_setup_frame.grid(row=1, column=0, rowspan=1,
                                    padx=(20, 10), pady=(20, 10), sticky="nsew"
                                    )

        # Label for info trade setup
        self.label_trade_setup = ttk.Label(master=self.Trade_setup_frame, text="Setup : ", justify="center",
                                           font=("-size", 15, "-weight", "bold")
                                           )
        self.label_trade_setup.grid(row=0, column=0, columnspan=2, padx=5, pady=10, sticky="nsew")

        # Cash Entry box
        self.cash_entry_box = ttk.Entry(master=self.Trade_setup_frame)
        self.cash_entry_box.insert(10000, "Set cash")
        self.cash_entry_box.grid(row=1, column=0, columnspan=2, padx=5, pady=7, sticky="nsew"
                                 )


        # Commission Spin box
        self.commission_set_spinbox = ttk.Spinbox(master=self.Trade_setup_frame, from_=0.00, to=0.09, increment=0.01)
        self.commission_set_spinbox.insert(0, "Set Commission %")
        self.commission_set_spinbox.grid(row=2, column=0, columnspan=2, padx=5, pady=7, sticky="nsew"
                                         )

        # Margin Spin Box
        self.margin_set_spinbox = ttk.Spinbox(master=self.Trade_setup_frame, from_=0, to=1.0, increment=0.01)
        self.margin_set_spinbox.insert(1, "Set Margin")
        self.margin_set_spinbox.grid(row=3, column=0, columnspan=2, padx=5, pady=7, sticky="nsew"
                                     )

        # Trade on close
        self.trade_on_close_checkbox = ttk.Checkbutton(master=self.Trade_setup_frame, text="Trade On Close",
                                                       variable=self.trade_on_close_var, onvalue=True, offvalue=False)
        self.trade_on_close_checkbox.grid(row=4, column=0, columnspan=2, padx=5, pady=7, sticky="nsew"
                                          )

        # Hedging
        self.hedging_checkbox = ttk.Checkbutton(master=self.Trade_setup_frame, text="Hedging Mode",
                                                variable=self.hedging_var, onvalue=True, offvalue=False)
        self.hedging_checkbox.grid(row=5, column=0, columnspan=2, padx=5, pady=7, sticky="nsew"
                                   )

        # Exclusive Order
        self.exclusive_order_checkbox = ttk.Checkbutton(master=self.Trade_setup_frame, text="Exclusive Order",
                                                        variable=self.exclusive_order_var, onvalue=True, offvalue=False)
        self.exclusive_order_checkbox.grid(row=6, column=0, columnspan=2, padx=5, pady=7, sticky="nsew"
                                           )

        # Confirm setup
        self.confirm_setup_button = ttk.Button(master=self.Trade_setup_frame, text="Confirm Trade Setup",
                                               style="Accent.TButton"
                                              )
        self.confirm_setup_button.grid(row=7, column=0, columnspan=2, padx=5, pady=7, sticky="nsew"

        )
        self.confirm_setup_button['command'] = self.confirm
        #self.confirm_setup_button['command'] = self.trade_setup_detail



