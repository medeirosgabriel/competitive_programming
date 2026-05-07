from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        def construct_dict(wordList):
            word_dict = {}
            for word in wordList:
                for i in range(len(word)):
                    w = word[:i] + "_" + word[i + 1:]
                    word_dict[w] = word_dict.get(w, []) + [word]
            return word_dict

        def bfs(beginWord, endWord, wordList, word_dict):
            queue, visited = deque([(beginWord, 1)]), set()
            while (queue):
                word, steps = queue.popleft()
                if (word == endWord): return steps
                if (not word in visited):
                    visited.add(word)
                    for i in range(len(word)):
                        w = word[:i] + "_" + word[i + 1:]
                        neigh_words = word_dict.get(w, [])
                        for nw in neigh_words:
                            queue.append((nw, steps + 1))
            return 0

        word_dict = construct_dict(wordList)
        steps = bfs(beginWord, endWord, wordList, word_dict)
        return steps

