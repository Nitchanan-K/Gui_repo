# label_data_change_from_file_select
def label_data_change_from_file_select(self):
    filename = self.ask_choose_file()[0]
    self.label_data.config(text=filename)
