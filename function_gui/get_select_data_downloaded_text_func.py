from function_gui import select_download_data_name_func
function = select_download_data_name_func.select_data_name
from tkinter import messagebox
def get_data_name():
    try:
        data_name = function.text
        return data_name
    except AttributeError:
        messagebox.showinfo(title="missing crypto name!",message="Please select Crypto Name")