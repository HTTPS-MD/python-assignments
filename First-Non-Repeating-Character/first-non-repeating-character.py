from collections import Counter
def first_non_repeating_character(word: str) -> str:
    dictionary = Counter(word)

    for key, value in dictionary.items():
        if value == 1:
            return key

    return ""

def first_non_repeating_character_v2(text : str) -> str:
    dictionary = {}

    for character in text:
        dictionary[character] = dictionary.get(character, 0) + 1

    for item in dictionary:
        if dictionary[item] == 1:
            return item

    return ""



if __name__ == "__main__":

    print(first_non_repeating_character("swiss")) # Expected: "w"
    print(first_non_repeating_character_v2("programming")) # Expected: "p"
    print(first_non_repeating_character_v2("prropo")) # Expected: Empty String