# import libraries


# Matplotlib
import matplotlib
matplotlib.use('TKAgg')
# import GUI
from tkinter import ttk

# import backtest lib
# get list data name
from crypto_data_list_top100.crypto_list_api_ticker_name import list_a
list_a_copy = list_a
# import request and API data download

# Import functions
import function_gui.run_start_func
import function_gui.save_file_xlsx
import function_gui.save_file_allstats_xlsx

plot_data = function_gui.run_start_func.Run_start
save_file_xlsx = function_gui.save_file_xlsx.save_file_xlsx
save_file_all_stats_xlsx = function_gui.save_file_allstats_xlsx.save_file_all_stats_xlsx

class Plot_save_data(ttk.Frame):

    # setup functions

    def __init__(self):
        ttk.Frame.__init__(self)

        # Create a Frame for Plot_save_frame
        self.Plot_save_frame = ttk.LabelFrame(master=self, text="Plot and Save The Data", padding=(20, 10))
        self.Plot_save_frame.grid(row=1, column=2, rowspan=1,
                                  padx=(20, 10), pady=(20, 10), sticky="nsew"
                                  )

        # Create a label Plot Data
        self.label_plot = ttk.Label(master=self.Plot_save_frame, text="Plot Data", justify="center",
                                    font=("-size", 15, "-weight", "bold"))
        self.label_plot.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky="nsew"
                             )

        # Create a label Save Data
        self.label_save = ttk.Label(master=self.Plot_save_frame, text="Save Data", justify="center",
                                    font=("-size", 15, "-weight", "bold"))
        self.label_save.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="nsew"
                             )

        # Create Notebook for Tab plot
        self.notebook_plot = ttk.Notebook(master=self.Plot_save_frame)
        self.notebook_plot.grid(row=1, column=0, columnspan=2, padx=15, pady=10, sticky="nsew"
                                )

        # Tab plot
        self.tab_plot = ttk.Frame(master=self.notebook_plot)
        for index in [0, 1]:
            self.tab_plot.columnconfigure(index=index, weight=1)
            self.tab_plot.rowconfigure(index=index, weight=1)
        self.notebook_plot.add(child=self.tab_plot, text="Data"
                               )

        self.tab_plot_2 = ttk.Frame(master=self.notebook_plot)
        for index in [0, 1]:
            self.tab_plot.columnconfigure(index=index, weight=1)
            self.tab_plot.rowconfigure(index=index, weight=1)
        self.notebook_plot.add(child=self.tab_plot_2, text="Optimize"
                               )

        self.tab_plot_3 = ttk.Frame(master=self.notebook_plot)
        for index in [0, 1]:
            self.tab_plot.columnconfigure(index=index, weight=1)
            self.tab_plot.rowconfigure(index=index, weight=1)
        self.notebook_plot.add(child=self.tab_plot_3, text="Pyfolio"
                               )

        # Create Notebook for Tab save
        self.notebook_save = ttk.Notebook(master=self.Plot_save_frame)
        self.notebook_save.grid(row=1, column=2, columnspan=2, padx=15, pady=10, sticky="nsew"
                                )

        # Tab Save Trade data
        self.tab_save = ttk.Frame(master=self.notebook_save)
        for index in [0, 1]:
            self.tab_save.columnconfigure(index=index, weight=1)
            self.tab_save.rowconfigure(index=index, weight=1)
        self.notebook_save.add(child=self.tab_save, text="Trade Data"
                               )
        # Tab Save overall stats
        self.tab_save_2 = ttk.Frame(master=self.notebook_save)
        for index in [0, 1]:
            self.tab_save_2.columnconfigure(index=index, weight=1)
            self.tab_save_2.rowconfigure(index=index, weight=1)
        self.notebook_save.add(child=self.tab_save_2, text="Overall Stats"
                               )
        # Tab Save tbd
        self.tab_save_3 = ttk.Frame(master=self.notebook_save)
        for index in [0, 1]:
            self.tab_save_3.columnconfigure(index=index, weight=1)
            self.tab_save_3.rowconfigure(index=index, weight=1)
        self.notebook_save.add(child=self.tab_save_3, text="tbd"
                               )

        # Accentbutton_run_plot_data
        self.accent_button_run_plot_data = ttk.Button(master=self.tab_plot, text="Back-testing",
                                                      style="Accent.TButton")
        self.accent_button_run_plot_data['command'] = plot_data
        self.accent_button_run_plot_data.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew"
                                              )

        # Accentbutton_save_plot_data
        self.accent_button_save_plot_data = ttk.Button(master=self.tab_save, text="Trade list",
                                                       style="Accent.TButton")
        self.accent_button_save_plot_data['command'] = save_file_xlsx
        self.accent_button_save_plot_data.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew"
                                               )

        # Accentbutton_save_overall_stats
        self.accent_button_save_overall_stats = ttk.Button(master=self.tab_save_2,text="All stats",
                                                           style="Accent.TButton")
        self.accent_button_save_overall_stats['command'] = save_file_all_stats_xlsx
        self.accent_button_save_overall_stats.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew"
                                                  )

