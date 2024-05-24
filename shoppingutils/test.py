from shoppingutils import *

my_cart = [
    {
        "produto": "banana",
        "preco": 10,
        "quantidade": 2
    },
    {
        "produto": "laranja",
        "preco": 8,
        "quantidade": 2
    },
    {
        "produto": "limao",
        "preco": 15,
        "quantidade": 2
    }
]

my_inventory = {
    "banana": { "quantidade": 1 },
    "limao": { "quantidade": 3 },
    "couve": { "quantidade": 7 },
    "laranja": { "quantidade": 12 },
    "tomate": { "quantidade": 5 }
}

print(calculate_total_price(my_cart))

print(apply_discount(my_cart, 10))

print(check_availability(my_cart, my_inventory))