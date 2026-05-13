class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1), len(word2))
        res = []
        l = 0
        while l<n:
            res.append(word1[l])
            res.append(word2[l])
            l+=1
        res.extend(word1[l:])
        res.extend(word2[l:])
        res = "".join(res)
        return res

