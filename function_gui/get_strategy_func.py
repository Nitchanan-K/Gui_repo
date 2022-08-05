# import messagebox
from tkinter import messagebox
# import label_change_combobox
from function_gui import label_change_combobox_func
strategy_var = label_change_combobox_func.label_change_combobox
def get_strategy():
    try:
        strategy_name = strategy_var.strategy
        return strategy_name
    except AttributeError:
        messagebox.showerror(title="Error!", message="Please select your Strategy")























