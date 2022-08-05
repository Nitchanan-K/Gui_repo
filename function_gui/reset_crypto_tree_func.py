from crypto_data_list_top100.crypto_list_api_ticker_name import list_a
list_a_copy = list_a

# Reset function
def Reset(self):
    self.tree_view_crypto_name.delete(*self.tree_view_crypto_name.get_children())
    for item in list_a_copy:
        self.tree_view_crypto_name.insert('', 'end', values=item)
