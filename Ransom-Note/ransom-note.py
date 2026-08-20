from collections import Counter

def can_construct_v1(ransom_note: str, magazine: str) -> bool:

    magazine = Counter(magazine)
    ransom_note = Counter(ransom_note)

    for character in ransom_note:
        if ransom_note[character] > magazine[character]:
            return False

    return True

def can_construct_v2(ransom_note: str, magazine: str) -> bool:

    ransom_note = Counter(ransom_note)
    magazine = Counter(magazine)

    for key, value in ransom_note.items():
        if magazine[key] < value:
            return False
    return True
if __name__ == "__main__":
    print(can_construct_v1("a", "b"))
    print(can_construct_v2("aa", "ab"))
    print(can_construct_v2("aa", "aab"))