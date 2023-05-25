# import messagebox
from tkinter import messagebox
# import confirm_set_up
from function_gui import confirm_setup_func
function = confirm_setup_func.confirm_setup

def get_cash():
    try:
        cash = function.cash
        return int(cash)
    except AttributeError:
        messagebox.showinfo(title="Warning!", message="Please setup your Cash amount")
