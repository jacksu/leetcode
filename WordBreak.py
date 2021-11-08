from locale import str
from typing import List


class WordBreak:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        import functools
        @functools.lru_cache(None)
        def back_track(s):
            if (not s):
                return True
            res = False
            for i in range(1, len(s) + 1):
                if (s[:i] in wordDict):
                    res = back_track(s[i:]) or res
            return res

        return back_track(s)

    def wordBreak2(self, s: str, wordDict: List[str]) -> List[str]:
        import functools
        @functools.lru_cache(None)
        def backtrack(index: int) -> List[List[str]]:
            if index == len(s):
                return [[]]
            ans = list()
            for i in range(index + 1, len(s) + 1):
                word = s[index:i]
                if word in wordSet:
                    nextWordBreaks = backtrack(i)
                    for nextWordBreak in nextWordBreaks:
                        ans.append(nextWordBreak.copy() + [word])
            return ans

        wordSet = set(wordDict)
        breakList = backtrack(0)
        return [" ".join(words[::-1]) for words in breakList]


if __name__ == '__main__':
    s = "catsanddog"
    print(s[::-1])
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    print([" ".join(words[::-1]) for  words in wordDict])
    egg = WordBreak()
    str = egg.wordBreak2(s, wordDict)
    print(str)
