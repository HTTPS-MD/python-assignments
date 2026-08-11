def first_uniq_char_index(word : str) -> int:

    dictionary = {}

    for character in word:
        dictionary[character] = dictionary.get(character, 0) + 1

    for index, value in enumerate(word):
        if dictionary[value] == 1:
            return index

    return -1
if __name__ == "__main__":

    text = input("Enter a word: ")
    print(first_uniq_char_index(text))


