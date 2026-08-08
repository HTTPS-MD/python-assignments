def count_vowel_and_consonant(sentence:  str) -> str:

    vowels = "aeiou"
    vowel_count = 0
    consonant_count = 0
    sentence = "".join([char for char in sentence if char.isalpha()]).lower()

    for char in sentence:
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

    return f"\nVowel Count: {vowel_count}\nConsonant Count: {consonant_count}"


if __name__ == "__main__":

    sentence = input("Enter a sentence: ")

    print(count_vowel_and_consonant(sentence))