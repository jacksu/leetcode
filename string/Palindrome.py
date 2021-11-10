import re

class Palindrome:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s1 = re.findall(r'[a-z0-9]', s)
        s2 = "".join(s1)
        # 使用字符串切片反转
        return s2[::-1] == s2

if __name__ == '__main__':
    k = "A man, a plan, a canal: Panama"
    pal = Palindrome()
    num = pal.isPalindrome(k)
    print(num)