class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1), len(word2))
        res = []
        l = 0
        print(f' the min is {n}')
        while l<n:
            res.append(word1[l])
            res.append(word2[l])
            l+=1
            print(f'res after append: {res}')
        res.extend(word1[l:])
        print(f'add remnaing of word1 {res}')
        res.extend(word2[l:])
        print(f'add remnaing of word2 {res}')
        res = "".join(res)
        print(f'final result is {res}')
        return res

