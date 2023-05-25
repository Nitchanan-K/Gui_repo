from tkinter import messagebox

def confirm_setup(self):
    # Cash value
    cash = self.cash_entry_box.get()
    confirm_setup.cash = cash
    print(cash)

    # Commission value
    commission = self.commission_set_spinbox.get()
    confirm_setup.commission = commission
    print(commission)

    # Margin value
    margin = self.margin_set_spinbox.get()
    confirm_setup.margin = margin
    print(margin)

    # Trade on close value
    trade_on_close = self.trade_on_close_var.get()
    confirm_setup.trade_on_close = trade_on_close
    print(trade_on_close)

    # Hedging value
    hedging_value = self.hedging_var.get()
    confirm_setup.hedging_value = hedging_value
    print(hedging_value)

    # Exclusive order value
    exclusive_order = self.exclusive_order_var.get()
    confirm_setup.exclusive_order = exclusive_order
    print(exclusive_order)

    messagebox.showinfo(title="Trade Setup information",message=f" Cash: {cash}\n Commission: {commission}\n Margin: {margin}\n "
                                                                f"Trade on close: {trade_on_close}\n Hedging: {hedging_value}\n"
                                                                f" Exclusive order: {exclusive_order}"

                        )
    return cash,commission,margin,trade_on_close,hedging_value,exclusive_order