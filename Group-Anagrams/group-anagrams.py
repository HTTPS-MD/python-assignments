def group_anagrams(list_of_words: list[str]) -> list[list[str]]:

    dictionary = {}

    for word in list_of_words:

        key = "".join(sorted(word))

        if key not in dictionary:
            dictionary[key] = []

        dictionary[key].append(word)

    return list(dictionary.values())


if __name__ == "__main__":
    list_of_words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(group_anagrams(list_of_words))