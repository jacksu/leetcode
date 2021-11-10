from collections import defaultdict


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = defaultdict()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current = self.words
        for letter in word:
            current = current.setdefault(letter, {})
        current.setdefault("_end")
        return None

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current = self.words
        for letter in word:
            if letter not in current:
                return False
            current = current[letter]
        if "_end" in current:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self.words
        for letter in prefix:
            if letter not in current:
                return False
            current = current[letter]
        return True

if __name__ == '__main__':
    test = Trie()
    test.insert('helloworld')
    test.insert('ilikeapple')
    test.insert('helloz')

    print(test.search('hello'))
    print(test.startsWith('hello'))
    print(test.search('ilikeapple'))
