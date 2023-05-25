# import libraries
# Panda Dataframe
# tabulate
# import GUI
# import filedialog for gui save
# import backtest lib
# get list data name
from crypto_data_list_top100.crypto_list_api_ticker_name import list_a
list_a_copy = list_a
# import request and API data download


# label change from select button
def select_data_name(self):
    # get cursor position
    curItem = self.tree_view_crypto_name.focus()
    text = self.tree_view_crypto_name.item(curItem)
    self.label_tree_view.config(text=text['values'])
    # set a = list contain name of crypto that selected
    a = text['values']
    # convert list into string
    a_str = str(a)
    # get rid of string that don't need
    tp = a_str.replace("[","")
    tp2 = tp.replace("]","")
    tp3 = tp2.replace("'","")
    # set attribute select_data_name.text = tp3
    select_data_name.text = tp3
    return select_data_name.text



