from collections import Counter

def can_construct(ransomNote: str, magazine: str) -> bool:

    ransomNote = Counter(ransomNote)
    magazine = Counter(magazine)

    for key, value in ransomNote.items():
        if magazine[key] < value:
            return False

    return True

if __name__ == "__main__":
    print(can_construct("a", "b"))
    print(can_construct("aa", "ab"))
    print(can_construct("aa", "aab"))