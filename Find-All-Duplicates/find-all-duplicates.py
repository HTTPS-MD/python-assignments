def find_all_duplicates(text: str) -> list:
    dictionary = {}
    for char in text:
        dictionary[char] = dictionary.get(char, 0) + 1
        
    return [key for key, value in dictionary.items() if value > 1]


if __name__ == "__main__":

    word = input("Enter a word: ")
    print(find_all_duplicates(word))