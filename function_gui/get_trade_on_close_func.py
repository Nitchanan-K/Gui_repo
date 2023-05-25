from function_gui import confirm_setup_func
function = confirm_setup_func.confirm_setup

def get_trade_on_close():
    trade_on_close = function.trade_on_close
    return bool(trade_on_close)