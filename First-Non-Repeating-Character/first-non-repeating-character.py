def first_non_repeating_character(word : str) -> chr:

    dictionary = {}

    for character in word:
        dictionary[character] = dictionary.get(character, 0) + 1

    for letter in word:
        if dictionary[letter] == 1:
            return letter


if __name__ == "__main__":
    word = input("Enter a word: ")

    print(first_non_repeating_character(word))