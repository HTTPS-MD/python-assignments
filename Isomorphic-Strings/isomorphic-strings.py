def is_isomorphic(s: str, t: str) -> bool:
    map_1 = {}
    map_2 = {}

    for a, b in zip(s,t):
        if (a in map_1 and map_1[a] != b) or (b in map_2 and map_2[b] != a):
            return False

        map_1[a] = b
        map_2[b] = a

    return True

if __name__ == "__main__":
    print(is_isomorphic("egg", "add"))    # Output: True
    print(is_isomorphic("foo", "bar"))    # Output: False
    print(is_isomorphic("paper", "title")) # Output: True