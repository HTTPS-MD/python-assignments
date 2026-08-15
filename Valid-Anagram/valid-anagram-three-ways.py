# 1. MANUAL WAY (Pure if-else at basic dict)
def is_anagram_manual(s: str, t: str) -> bool:

    if len(s) != len(t):
        return False

    dictionary = {}

    for character in s:
        if character not in dictionary:
            dictionary[character] = 0

        dictionary[character] += 1

    for character in t:
        if character not in dictionary or dictionary[character] == 0:
            return False

        dictionary[character] -= 1

    return True

# 2. BUILT-IN METHOD WAY (Gamit ang .get())
def is_anagram_builtin(s: str, t: str) -> bool:

    if len(s) != len(t):
        return False

    dictionary = {}
    for character in s:
        dictionary[character] = dictionary.get(character, 0) + 1

    for character in t:
        if character not in dictionary or dictionary[character] == 0:
            return False

        dictionary[character] -= 1

    return True


# 3. EXTERNAL LIBRARY WAY (Gamit ang collections.Counter)

from collections import Counter
def is_anagram_library(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    dictionary = Counter(s)

    for character in t:
        if character not in dictionary or dictionary[character] == 0:
            return False

        dictionary[character] -= 1

    return True

if __name__ == "__main__":
    print(is_anagram_manual("anagram", "nagaram"))  # Output: True
    print(is_anagram_builtin("rat", "car"))          # Output: False
    print(is_anagram_library("a", "ab"))             # Output: False