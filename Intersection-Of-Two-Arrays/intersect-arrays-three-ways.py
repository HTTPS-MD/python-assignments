# 1. MANUAL WAY (Pure if-else at basic dict)
def intersect_manual(nums1: list[int], nums2: list[int]) -> list[int]:
    dictionary = {}
    list_num = []

    for item in nums1:
        if item not in dictionary:
            dictionary[item] = 0
        dictionary[item] += 1

    for item in nums2:
        if item in dictionary:
            while dictionary[item] > 0:
                list_num.append(item)
                dictionary[item] -= 1

    return list_num



# 2. BUILT-IN METHOD WAY (Gamit ang .get())
def intersect_builtin(nums1: list[int], nums2: list[int]) -> list[int]:

    dictionary = {}
    list_num = []

    for item in nums1:
        dictionary[item] = dictionary.get(item, 0) + 1

    for item in nums2:
        if item in dictionary and dictionary[item] > 0:
            list_num.append(item)
            dictionary[item] -= 1

    return list_num

# 3. EXTERNAL LIBRARY WAY (Gamit ang collections.Counter)

from collections import Counter
def intersect_library(nums1: list[int], nums2: list[int]) -> list[int]:
    dictionary = Counter(nums1)
    list_num = []

    for item in nums2:
        if item in dictionary and dictionary[item] > 0:
            list_num.append(item)
            dictionary[item] -= 1

    return list_num

if __name__ == "__main__":
    print(intersect_manual([1, 2, 2, 1], [2, 2]))         # Output: [2, 2]
    print(intersect_builtin([4, 9, 5], [9, 4, 9, 8, 4]))  # Output: [4, 9] (o [9, 4])
    print(intersect_library([1, 2], [1, 1]))              # Output: [1]