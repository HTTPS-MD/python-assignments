def unique_word_counter_and_frequency(sentence: str) -> dict:

    sentence = sentence.split()
    dictionary ={}


    for word in sentence:
        dictionary[word] = dictionary.get(word, 0) + 1

    return dictionary


if __name__ == "__main__":
    sentence = input("Enter a sentence: ").lower()


    print(unique_word_counter_and_frequency(sentence))