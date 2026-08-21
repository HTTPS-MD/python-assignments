def get_evens(numbers : list[int]) -> list[int]:

    return [num for num in numbers if num % 2 == 0]

if __name__ == "__main__":

    print(get_evens([1, 2, 3, 4, 5, 6]))  # Expected output: [2, 4, 6]
    print(get_evens([7, 9, 11]))           # Expected output: []