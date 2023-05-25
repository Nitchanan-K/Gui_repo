# have base class


def label_change_combobox(self):

    global selected_strategy
    self.label.config(text=self.combobox.get())
    # strategies[combobox.get()] need to be value from the combobox as str
    # and str need to be the same in strategies (dict) that point to the class of that strategy
    # combobox.get() = name of strategy in dict that refer to the strategy Class
    selected_strategy = self.strategies[self.combobox.get()]
    label_change_combobox.strategy = selected_strategy
    print(self.strategies[self.combobox.get()])
    return selected_strategy
