def calculate_total_price(cart):
    return sum([produto["preco"] for produto in cart])