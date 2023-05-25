

# maybe use pop up box to give detail
# get valure from confrim function
def trade_setup_details(self):
    from function_gui import get_cash_func, get_commission_func, get_margin_func, get_trade_on_close_func, \
        get_hedging_func, get_exclusive_order_func

    cash = get_cash_func.get_cash()
    commission = get_commission_func.get_commission()
    margin = get_margin_func.get_margin()
    trade_on_close = get_trade_on_close_func.get_trade_on_close()
    hedging = get_hedging_func.get_hedging()
    exclusive_order = get_exclusive_order_func.get_exclusive_order()

    self.label_trade_setup.config(text=f" Cash: {cash}, Commission: {commission}, Margin: {margin},\n Trade on close:{trade_on_close} \n Hedging:{hedging} \n Exclusive Order:{exclusive_order} ",
                                  font=("-size", 8, "-weight", "bold"),justify="left")