class Solution(object):
    
    def diffStrings(self, w1, w2):
        diff = 0
        for i in range(len(w1)):
            if (w1[i] != w2[i]): diff += 1
        return diff

    def dfs(self, currWord, currList, endWord, wordsList, deep):
        diff = self.diffStrings(currWord, endWord)
        if (diff != 0):
            for i in range(len(wordsList)):
                i1, i2 = self.dic[currWord], self.dic[wordsList[i]]
                diff = self.matrix[i1][i2]
                if (diff == 1 and deep < self.min_):
                    self.dfs(
                        wordsList[i], 
                        currList + [currWord],
                        endWord, 
                        wordsList[:i] + wordsList[i + 1:],
                        deep + 1
                    )
        else:
            currList.append(endWord)
            length = len(currList)
            if (length < self.min_):
                self.result = []
                self.min_ = length
                self.result.append(currList)
            elif (length == self.min_):
                self.result.append(currList)
    
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordList = list(set(wordList))
        words = [beginWord] + wordList
        self.dic, count = {}, 0
        for w in words:
            self.dic[w] = count
            count += 1
        self.matrix = [[-1 for _ in range(len(words))] for _ in range(len(words))]
        for i in range(len(words)):
            for j in range(i, len(words)):
                w1, w2 = words[i], words[j]
                i1, i2 = self.dic[w1], self.dic[w2]
                diff = self.diffStrings(w1, w2)
                self.matrix[i1][i2] = diff
                self.matrix[i2][i1] = diff

        print(self.matrix)
        self.result = []
        self.min_ = float("inf")
        self.dfs(beginWord, [], endWord, wordList, 0)
        return self.result
        