def two_sums(numbers: list[int], target: int) -> list[int]:
    dictionary = {}

    for index, value in enumerate(numbers):
        complement = target - value

        if complement in dictionary:
            return [dictionary[complement], index]

        dictionary[value] = index

    return []

if __name__ == "__main__":
    num_list = [5, 7, 2, 15]
    num_target = 9
    print(two_sums(num_list, num_target))