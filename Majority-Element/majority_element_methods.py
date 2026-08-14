# 1. MANUAL WAY (Gamit ang pure if-else at basic dict)
def majority_manual(nums: list[int]) -> int:
    dictionary = {}

    for item in nums:

        if item not in dictionary:
            dictionary[item] = 0

        dictionary[item] += 1

    for item, value in dictionary.items():
        if value > len(nums) / 2:
            return item

    return -1
# 2. BUILT-IN METHOD WAY (Gamit ang .get())
def majority_builtin(nums: list[int]) -> int:
    dictionary = {}

    for item in nums:
        dictionary[item] = dictionary.get(item, 0) + 1

    for item, value in dictionary.items():
        if value > len(nums) / 2:
            return item

    return -1

# 3. EXTERNAL LIBRARY WAY (Gamit ang collections.Counter)
from collections import Counter
def majority_library(nums: list[int]) -> int:
    dictionary = Counter(nums)

    for item, value in dictionary.items():
        if value > len(nums) / 2:
            return item

    return -1

if __name__ == "__main__":
    print(majority_manual([3, 2, 3]))        # Output: 3
    print(majority_builtin([2, 2, 1, 1, 1, 2, 2])) # Output: 2
    print(majority_library([1]))             # Output: 1