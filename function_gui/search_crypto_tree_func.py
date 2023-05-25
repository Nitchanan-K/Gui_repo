from crypto_data_list_top100.crypto_list_api_ticker_name import list_a
list_a_copy = list_a
import function_gui.update_crypto_tree_func

def search_crypto_tree(self):
    update_function = function_gui.update_crypto_tree_func.Update_crypto_tree
    value = self.search_entry_box_text.get()

    if value.lower() and value.upper() == '':
        data = list
    else:
        data = []
        for item in list_a_copy:
            if value.lower() in item.lower():
                data.append(item)

    update_function(self,data)