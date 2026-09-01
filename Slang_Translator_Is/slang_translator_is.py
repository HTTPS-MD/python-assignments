def translate_is_sentences(sentence : str) -> str:

    clean = sentence.replace("is", "")
    return clean


if __name__ == "__main__":

    text = input("Enter 'is' slang tagalog sentences: ")


    print(translate_is_sentences(text))