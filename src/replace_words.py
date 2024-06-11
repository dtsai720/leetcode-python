from typing import List


class Trie:
    """
    A trie is a tree-like data structure whose nodes store the letters of an alphabet.
    By structuring the nodes in a particular way, words and strings can be retrieved
    from the structure by traversing down a branch path of the tree.

    Attributes:
        children: dict -- A dictionary that stores the children of the trie.
        is_end_of_word: bool -- A boolean value to indicate the end of a word.
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}
        self.is_end_of_word = False

    def insert(self, word: str) -> None:
        """
        Insert a word into the trie.

        Args:
            word: str -- A word to be inserted into the trie.
        """
        if not isinstance(word, str):
            raise TypeError("word should be a string.")

        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]
        node.is_end_of_word = True

    def get_root(self, word: str):
        """
        Get the root word of a given word.

        Args:
            word: str -- A word to get the root word.

        Returns:
            str -- The root word of the given word.
        """
        if not isinstance(word, str):
            raise TypeError("word should be a string.")

        node = self
        for size, char in enumerate(word):
            if char not in node.children:
                return word
            node = node.children[char]
            if node.is_end_of_word:
                return word[: size + 1]
        return word


def replace_words(dictionary: List[str], sentence: str) -> str:
    """
    Given a dictionary of words dict and a sentence with all words separated by space,
    replace all the words in the sentence that appear in the dictionary with
    the root word in the dictionary.

    If a root word is replaced, the original word should be replaced with
    the root word in the sentence.

    Args:
        dictionary: List[str] -- A list of words.
        sentence: str -- A sentence with all words separated by space.

    Returns:
        str -- A sentence with all words replaced by the root word.
    """
    if not isinstance(dictionary, list) or not isinstance(sentence, str):
        raise TypeError("dictionary should be a list and sentence should be a string.")

    if not all(isinstance(word, str) for word in dictionary):
        raise ValueError("All elements in dictionary should be a string.")

    trie = Trie()
    for word in dictionary:
        trie.insert(word)

    return " ".join(trie.get_root(word) for word in sentence.split())
