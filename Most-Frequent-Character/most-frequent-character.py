from collections import Counter
def most_frequent_character_v2(word: str) -> str:
    dictionary = Counter(word.lower().replace(" ", ""))
    dictionary = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    return dictionary[0][0]

def most_frequent_character(text : str) -> str :
    dictionary = {}
    for character in text:
        dictionary[character] = dictionary.get(character, 0) + 1
    max_char = ""
    max_count = 0
    for item in dictionary:
        if dictionary[item] > max_count:
            max_char = item
            max_count = dictionary[item]
    return max_char

if __name__ == "__main__":
    print(most_frequent_character("Hello World"))
    print(most_frequent_character_v2("Mark Daniel"))
