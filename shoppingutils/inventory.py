def check_availability(cart, inventory):
    for produto in cart:
        if produto["quantidade"] < inventory[produto["produto"]]["quantidade"]:
            return False
    return True
