def frequency_sort(word: str) -> str:
    webster = {}
    counter = 0
    updated_list = []

    for character in word:
        webster[character] = webster.get(character, 0) + 1

    sorted_chars = sorted(webster.keys(), key=lambda x: webster[x], reverse=True)

    return "".join(char * webster[char] for char in sorted_chars)





from collections import Counter
def frequency_sort_v2(word: str) -> str:
    dictionary = Counter(word)
    list_char = sorted(dictionary.items(), key=lambda x : x[1], reverse=True)
    final_str = []

    for character, count in list_char:
        final_str.append(character * count)


    return "".join(final_str)


def frequency_sort_v3(word: str) -> str:

    return "".join(char * count for char, count in Counter(word).most_common())

if __name__ == "__main__":

    print(frequency_sort("tree"))
    print(frequency_sort_v2("cccaaa"))
    print(frequency_sort_v3("Aabb"))


