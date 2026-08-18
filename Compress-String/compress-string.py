def compress_string(text: str) -> str:
    if not text:
        return text

    compressed = []
    current_char = text[0]
    count = 0

    for character in text:
        if character == current_char:
            count += 1

        else:
            compressed.append(current_char + str(count))
            current_char = character
            count = 1

    compressed.append(current_char + str(count))
    str_compressed = "".join(compressed)

    return str_compressed if len(str_compressed) < len(text) else text

if __name__ == "__main__":
    print(compress_string("aabcccccaaa"))  # Returns "a2b1c5a3"
    print(compress_string("abcdef"))       # Returns "abcdef"
    print(compress_string("aabbcc"))       # Returns "aabbcc"