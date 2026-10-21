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


def search_build(target_hero):
    try:
        with open('details.json', 'r') as file:
            details = json.load(file)
    except FileNotFoundError:
        return "Wala pang naka-save na builds."

    for build in details:
        if build["Hero"].lower() == target_hero.lower():
            return f"Ang core item ni {build['Hero']} ay {build['Core Item']}."

    return "Hindi nahanap ang hero na ito."