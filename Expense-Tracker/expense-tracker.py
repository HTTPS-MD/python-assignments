transactions = [
    {"category": "Food", "amount": 150},
    {"category": "Transport", "amount": 60},
    {"category": "Food", "amount": 200},
    {"category": "Utilities", "amount": 500},
    {"category": "Transport", "amount": 40}
]

dictionary = {}


for item in transactions:
    category = item["category"]
    amount = item["amount"]

    if category not in dictionary:
        dictionary[category] = 0

    dictionary[category] += amount

sorted_dict = dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))

print(sorted_dict)