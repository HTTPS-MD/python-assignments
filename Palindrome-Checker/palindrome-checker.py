def is_palindrome(word : str) -> bool:

    list_num = []

    for character in word.lower():
        list_num.insert(0, character)

    return "".join(list_num) == word.lower()


def is_palindrome_v2(word: str) -> bool:

    clean_sentence = "".join([char for char in word if char.isalpha()]).lower()

    return clean_sentence == clean_sentence[::-1]


def is_palindrome_v3(word: str) -> bool:
    clean = "".join(char for char in word.lower() if char.isalnum())

    return clean[::-1] == clean

if __name__ == "__main__":

    print(is_palindrome("Python")) # False
    print(is_palindrome_v2("Racecar"))  # True
    print(is_palindrome_v3("Mark::::';k;raM"))  # True

