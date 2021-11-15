from typing import List


class ReverseString:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        left = 0
        right = n - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

if __name__ == '__main__':
    re = ReverseString()
    s = ["H","a","n","n","a","h"]
    re.reverseString(s)
    print(s)