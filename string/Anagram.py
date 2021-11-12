class Anagram:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        return Counter(s) == Counter(t)


if __name__ == '__main__':
    an = Anagram()
    s = "anagram"
    t = "nagaram"
    print(an.isAnagram(s, t))
