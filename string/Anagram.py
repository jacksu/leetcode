class Anagram:
    #给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        return Counter(s) == Counter(t)

    ##字符串中的第一个唯一字符
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        frequency = Counter(s)
        for i, ch in enumerate(s):
            if frequency[ch] == 1:
                return i
        return -1

if __name__ == '__main__':
    an = Anagram()
    s = "anagram"
    t = "nagaram"
    print(an.isAnagram(s, t))

    print(an.firstUniqChar(s))
