import json

def save_build(hero, core_item):

    try:
        with open('details.json', 'r') as file:
            details = json.load(file)

    except FileNotFoundError:
        details = []

    details.append({"Hero" : hero, "Core Item" : core_item})


    with open('details.json', 'w') as file:
        json.dump(details, file, indent = 3)


