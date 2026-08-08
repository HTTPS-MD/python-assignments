def is_palindrome(word : str) -> bool:

    reversedWord = word[::-1]

    if word == reversedWord:
        print("it's a Palindrome")

    else:
        print("it's not a Palindrome")





if __name__ == "__main__":
    word = "".join([char for char in input("Enter a word: ") if char.isalnum()]).lower()
    print(word)
    is_palindrome(word)