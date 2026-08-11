def top_k_frequent(nums : list[int], k : int) -> list[int]:

    dictionary = {}
    list_num = []

    for item in nums:
        dictionary[item] = dictionary.get(item, 0) + 1


    dictionary = dict(sorted(dictionary.items(), key=lambda item:item[1])[::-1])


    for key, value in dictionary.items():
        if k > 0:
            list_num.append(key)
            k -= 1
        else:
            break

    return list_num



if __name__ == "__main__":
    print(top_k_frequent([1, 1, 1, 2, 3, 3, 3, 3, 3], 2))
    print(top_k_frequent([1], 1))