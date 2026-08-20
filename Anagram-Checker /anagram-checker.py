from collections import Counter
def is_anagram_v1(w1: str, w2: str) -> bool:
    w1 = Counter(char.lower() for char in w1 if char.isalnum())
    w2 = Counter(char.lower() for char in w2 if char.isalnum())
    return w1 == w2


def is_anagram_v2(w1 : str, w2 : str) -> bool:

    w1 = "".join(sorted(w1.lower().replace(" ", "")))
    w2 = "".join(sorted(w2.lower().replace(" ", "")))

    return w1 == w2

if __name__ == "__main__":
    first_word = input("Enter First Word: ")
    second_word = input("Enter Second Word: ")

    print(is_anagram_v1(first_word, second_word))
    print(is_anagram_v2(first_word, second_word))