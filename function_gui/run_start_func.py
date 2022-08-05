from tkinter import messagebox
# import backtest lib
from backtesting import Backtest, Strategy
# import re
import re



def Run_start():
    # import function that return dataframe from selection
    from function_gui import get_data_frame_func
    from function_gui import get_strategy_func
    from function_gui import get_cash_func,get_commission_func,get_margin_func,get_trade_on_close_func,get_hedging_func,get_exclusive_order_func

    dataframe = get_data_frame_func.get_data_frame()
    strategy = get_strategy_func.get_strategy()
    cash = get_cash_func.get_cash()
    commission = get_commission_func.get_commission()
    margin = get_margin_func.get_margin()
    trade_on_close = get_trade_on_close_func.get_trade_on_close()
    hedging = get_hedging_func.get_hedging()
    exclusive_order = get_exclusive_order_func.get_exclusive_order()
    print(cash,commission,margin,trade_on_close,hedging,exclusive_order)


    if messagebox.askokcancel(title="Confirm Backtesting",message="Confirm Plot Data?"):
        bt = Backtest(dataframe,strategy, cash=cash,commission=commission,
                      margin=margin,trade_on_close=trade_on_close,hedging=hedging,
                      exclusive_orders=exclusive_order)
        stats = bt.run()
        Run_start.stats = stats
        print(stats["_trades"])
        print(stats)
        bt.plot()
    else:
        pass


    '''
    self.bt = Backtest(self.ask_choose_file()[1], selected_strategy, cash=int(cash_entry_box.get()),
                       commission=float(commission_set_spinbox.get()),
                       margin=float(margin_set_spinbox.get()), trade_on_close=trade_on_close_var.get(),
                       hedging=hedging_var.get(),
                       exclusive_orders=True)
    '''
















