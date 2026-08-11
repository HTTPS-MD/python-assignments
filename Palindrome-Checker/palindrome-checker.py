def is_palindrome(word: str) -> bool:

    clean_sentence = "".join([char for char in word if char.isalpha()]).lower()

    return clean_sentence == clean_sentence[::-1]


if __name__ == "__main__":

    word = input("Enter a word or sentence: ")
    print(is_palindrome(word))