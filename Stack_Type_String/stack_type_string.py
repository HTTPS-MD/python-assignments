def type_string(s: str) -> str:
    stack = []

    for char in s:

        if char.isalpha():
            stack.append(char)

        else:
            stack.pop()


    return "".join(stack)


if __name__ == "__main__":
    # 'a', 'b', backspace (tanggal 'b'), 'c' -> "ac"
    print(type_string("ab#c"))  # Expected Output: "ac"

    # 'a', 'b', backspace, backspace, 'c' -> "c"
    print(type_string("ab##c"))  # Expected Output: "c"

    # paano kung puro backspace sa simula?
    print(type_string("a#c"))  # Expected Output: "c"