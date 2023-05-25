from crypto_data_list_top100.crypto_list_api_ticker_name import list_a
list_a_copy = list_a

# Update function
def Update_crypto_tree(self,data):
    self.tree_view_crypto_name.delete(*self.tree_view_crypto_name.get_children())

    # put new data
    for item in data:
        self.tree_view_crypto_name.insert('','end', values=item)
        self.tree_view_crypto_name.update()