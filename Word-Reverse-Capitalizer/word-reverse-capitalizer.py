sentence = input("Enter a sentence: ").split()[::-1]
print(" ".join([word.title() for word in sentence]))