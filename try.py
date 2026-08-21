def isValid(s: str) -> bool:
    stack = []
    dictionary = {"(" : ")", "[" : "]", "{" : "}"}

    for character in s:
        if character in dictionary:
            stack.append(character)

        if dictionary[stack[0]] == character:
            stack_u = stack.pop()
           

    return True
if __name__ == "__main__":
    print(isValid("()"))      # Expected output: True
    print(isValid("()[]{}"))  # Expected output: True
    print(isValid("(]"))      # Expected output: False
    print(isValid("([)]s"))    # Expected output: False