# import messagebox
from tkinter import messagebox
# import confirm_set_up
from function_gui import confirm_setup_func
function = confirm_setup_func.confirm_setup

def get_commission():
    try:
        commission = function.commission
        return float(commission)
    except AttributeError:
        messagebox.showinfo(title="Warning!", message="Please setup commission fee")