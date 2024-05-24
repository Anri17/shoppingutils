# shoppingutils

Esta biblioteca foi criada no âmbito da frequência nº2 da cadeira de Programação Avançada do TeSP de Informática. 

### Instalação

Para instalar, use o seguinte comando:
```
pip install git+https://github.com/Anri17/shoppintutils.git
```

Depois basta importar a biblioteca:
```
from * import shoppingutils
```

### cart.py

``calculate_total_price(cart)``  
Recebe uma lista de itens do cart de compras.  
Devolve o preço total da compra.

### discount.py

``apply_discount(cart, discount)``  
Recebe uma lista de itens do cart de compras e um disconto percentual.  
Devolve um novo cart de compras com o disconto aplicado a todos os produtos

### iventory.py

``check_availability(cart, inventory)``  
Recebe uma lista de itens do cart de compras e um inventários da quantidade dos produtos.  
Devolve True ou False, se os produtos contidos no cart de compras estão disponíves, tendo em atenção o stock no inventário.

### Exemplos

A baixo estão exemplos de um ``cart`` e de um ``inventory``:

```
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

```

Exemplo de uso das funções:
```
print(calculate_total_price(my_cart))

print(apply_discount(my_cart, 10))

print(check_availability(my_cart, my_inventory))
```

