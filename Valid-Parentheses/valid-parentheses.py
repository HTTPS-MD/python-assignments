
# balikan mo to [0mark
def valid_parentheses(characters: str) -> bool:
    stack = []
    # Mapping ng closing bracket patungo sa opening bracket
    mapping = {")": "(", "}": "{", "]": "["}

    for char in characters:
        if char in mapping:
            # Kung closing bracket, kunin ang huling nilagay sa stack
            top_element = stack.pop() if stack else '#'

            # I-check kung tumutugma sa katapat niya
            if mapping[char] != top_element:
                return False
        else:
            # Kung opening bracket, i-push sa stack
            stack.append(char)

    # Babalik ng True kung walang natira sa stack (ibig sabihin lapat lahat)
    return not stack


if __name__ == "__main__":
    symbol = input("Enter : ")
    print(valid_parentheses(symbol))