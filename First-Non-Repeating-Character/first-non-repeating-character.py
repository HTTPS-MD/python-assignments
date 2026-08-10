def first_non_repeating_character(text : str) -> str :
    dictionary = {}

    for character in text:
        dictionary[character] = dictionary.get(character, 0) + 1

    for item in dictionary:
        if dictionary[item] == 1:
            return item

    return ""

if __name__ == "__main__":
    word = input("Enter a word: ")

    print(first_non_repeating_character(word))