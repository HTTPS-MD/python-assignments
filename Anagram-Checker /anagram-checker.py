def is_anagram(w1 : str, w2 : str) -> bool:

    w1 = "".join(sorted(w1.lower().replace(" ", "")))
    w2 = "".join(sorted(w2.lower().replace(" ", "")))

    return w1 == w2

if __name__ == "__main__":
    first_word = input("Enter First Word: ")
    second_word = input("Enter Second Word: ")

    print(is_anagram(first_word, second_word))