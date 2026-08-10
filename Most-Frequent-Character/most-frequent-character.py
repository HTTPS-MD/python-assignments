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

    word = input("Enter a word: ")
    print(most_frequent_character(word))

