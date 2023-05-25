# Panda Dataframe
# tabulate
# Matplotlib
import matplotlib
matplotlib.use('TKAgg')
# import GUI
from tkinter import ttk
# import filedialog for gui save
# import backtest lib
# get list data name
from crypto_data_list_top100.crypto_list_api_ticker_name import list_a
list_a_copy = list_a


# import functions
from function_gui import label_change_combobox_func


class Strategy_frame_widget(ttk.Frame):

    # setup functions
    label_change_combobox = label_change_combobox_func.label_change_combobox

    def __init__(self):
        ttk.Frame.__init__(self)


        import strategy_class.SmaCross_class
        import strategy_class.Sma4Cross_class

        SmaCross = strategy_class.SmaCross_class.SmaCross
        Sma4Cross = strategy_class.Sma4Cross_class.Sma4Cross

        self.strategies = {
            'SmaCross': SmaCross,
            'Sma4Cross': Sma4Cross
        }

        self.combo_list_strategy = ["Sma4Cross", "SmaCross", "Bollinger Band"]

        # Create a Frame for the Strategy
        self.Strategy_frame = ttk.LabelFrame(master=self, text="Choose Strategy", padding=(20, 10))
        self.Strategy_frame.grid(row=0, column=0, rowspan=1,
                                 padx=(20, 10), pady=(20, 10), sticky="nsew"
                                 )

        # Text label
        self.label = ttk.Label(master=self.Strategy_frame, text="Strategy", justify="center",
                               font=("-size", 15, "-weight", "bold"))
        self.label.grid(row=0, column=0, columnspan=2,
                        padx=5, pady=10, sticky="nsew"
                        )

        # Combobox
        self.combobox = ttk.Combobox(master=self.Strategy_frame, values=self.combo_list_strategy,
                                     )#textvariable=self.selected_name_strategy)
        self.combobox.current(0)
        self.combobox['state'] = 'readonly'
        self.combobox.grid(row=1, column=0, padx=5, pady=10, sticky="ew")
        self.combobox.bind('<<ComboboxSelected>>'
                           )

        # Accentbutton_select_strategy
        self.accent_button_select_strategy = ttk.Button(master=self.Strategy_frame, text="Select Strategy",
                                                        style="Accent.TButton")

        self.accent_button_select_strategy['command'] = self.label_change_combobox
        self.accent_button_select_strategy.grid(row=2, column=0, columnspan=2, padx=5, pady=10, sticky="nsew"
                                                )