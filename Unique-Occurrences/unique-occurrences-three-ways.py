# 1. MANUAL WAY (Pure if-else at basic dict)
def unique_occurrences_manual(arr: list[int]) -> bool:

    dictionary = {}
    freq_tracker = []

    for item in arr:
        if item not in dictionary:
            dictionary[item] = 0

        dictionary[item] += 1

    for item, value in dictionary.items():
        if value in freq_tracker:
            return False

        freq_tracker.append(value)

    return True
# 2. BUILT-IN METHOD WAY (Gamit ang .get())
def unique_occurrences_builtin(arr: list[int]) -> bool:

    dictionary = {}
    freq_tracker = set()

    for item in arr:
        dictionary[item] = dictionary.get(item, 0) + 1

    freq_tracker = set(dictionary.values())

    print(dictionary, freq_tracker)
    return len(freq_tracker) == len(dictionary)

# 3. EXTERNAL LIBRARY WAY (Gamit ang collections.Counter)
from collections import Counter

def unique_occurrences_library(arr: list[int]) -> bool:

    dictionary = Counter(arr)
    freq_tracker = set(dictionary.values())

    return len(freq_tracker) == len(dictionary)
if __name__ == "__main__":
    print(unique_occurrences_manual([1, 2, 2, 1, 1, 3]))      # Output: True (1: 3x, 2: 2x, 3: 1x -> lahat unique ang frequency)
    print(unique_occurrences_builtin([1, 2]))                  # Output: False (1: 1x, 2: 1x -> pareho silang 1 ang frequency)
    print(unique_occurrences_library([-3, 1, -3, 1, 1, -2]))   # Output: True