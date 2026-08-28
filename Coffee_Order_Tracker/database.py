import json

def save_order(name, coffee):
    try:
        with open('orders.json', 'r') as file:
            order_list = json.load(file)

    except FileNotFoundError:
        order_list = []

    order_list.append({"name" : name, "coffee" : coffee})

    with open('orders.json', 'w') as file:
        json.dump(order_list, file, indent=4)