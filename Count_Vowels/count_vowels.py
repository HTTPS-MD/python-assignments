def count_vowels(text : str) -> int :


    return sum(1 for char in text.lower() if char in "aeiou")


def count_vowels_v2(text : str) -> int:

    dictionary = {}
    vowel_count = 0
    vowels = "aeiou"

    for char in text.lower():
        dictionary[char] = dictionary.get(char, 0) + 1


    for key, value in dictionary.items():
        if key in vowels:
            vowel_count += value

    return vowel_count


if __name__ == "__main__":
    print(count_vowels("Software Engineering"))  # Expected output: 8
    print(count_vowels_v2("Software Engineering"))