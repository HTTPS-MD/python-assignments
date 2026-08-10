def count_items(items : list[str]) -> dict :

    dictionary = {}

    for item in items:
        dictionary[item] = dictionary.get(item, 0) + 1


    return dictionary

if __name__ == "__main__" :
    fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
    print(count_items(fruits))

