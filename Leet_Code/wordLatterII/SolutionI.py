from collections import defaultdict, deque

class SolutionI(object):

    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if endWord not in wordList: 
            return []

        graph = defaultdict(set)
        words = wordList + [beginWord]
        for word in words:
            for i in range(len(word)):
                new_word = word[:i] + '*' + word[i+1:]
                graph[word].add(new_word)
                graph[new_word].add(word)

        def neighbors(w):
            neighs = set()
            for w1 in graph[w]:
                for w2 in graph[w1]:
                    neighs.add(w2)
            neighs.remove(w)
            return neighs

        res = []
        q = [(beginWord, [beginWord])]
        visited = {beginWord}
        while (len(q) > 0):
            next_level = []
            for w, path in q:
                for neighbor in neighbors(w):
                    if (neighbor == endWord):
                        res.append(path + [neighbor])
                        continue
                    if (neighbor in visited):
                        continue
                    next_level.append((neighbor, path + [neighbor]))

            if len(res) > 0: break
            q = next_level
        return res
