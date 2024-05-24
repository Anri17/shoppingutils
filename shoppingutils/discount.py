def apply_discount(cart, discount):
    return [{"preco": produto["preco"]-(produto["preco"]* (discount/100)), "produto": produto["produto"]} for produto in cart]
