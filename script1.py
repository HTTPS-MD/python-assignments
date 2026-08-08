def is_palindrome(word):

    reversed_word = word[::-1]


    if word == reversed_word:
        return True


    return False





if __name__ == "__main__":

    word = input("Enter a word: ").r

eplace(" ", "").lower()
    print(f"Is it a palindrome? {is_palindrome(word)}")