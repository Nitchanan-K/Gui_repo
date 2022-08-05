from function_gui import confirm_setup_func
function = confirm_setup_func.confirm_setup

def get_hedging():
    hedging_value = function.hedging_value
    return bool(hedging_value)