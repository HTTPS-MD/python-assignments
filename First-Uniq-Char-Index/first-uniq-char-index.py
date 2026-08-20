from collections import Counter
def first_uniq_char_index_v1(word : str) -> int:

    dictionary = {}

    for character in word:
        dictionary[character] = dictionary.get(character, 0) + 1

    for index, value in enumerate(word):
        if dictionary[value] == 1:
            return index

    return -1


def first_uniq_char_index_v2(text : str) -> int:
    counts = Counter(text)

    for index, character in enumerate(text):
        if counts[character] == 1:
            return index

    return -1

if __name__ == "__main__":

    text = input("Enter a word: ")
    print(first_uniq_char_index_v1(text))
    print(first_uniq_char_index_v2(text))