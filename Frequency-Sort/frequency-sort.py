def frequency_sort(word: str) -> str:
    webster = {}
    counter = 0
    updated_list = []

    for character in word:
        webster[character] = webster.get(character, 0) + 1

    sorted_chars = sorted(webster.keys(), key=lambda x: webster[x], reverse=True)

    return "".join(char * webster[char] for char in sorted_chars)

if __name__ == "__main__":

    print(frequency_sort("tree"))
    print(frequency_sort("cccaaa"))
    print(frequency_sort("Aabb"))