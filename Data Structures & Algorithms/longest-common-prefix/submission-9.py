class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #find the min/max string
        minString = min(strs)
        maxString = max(strs)
        res = ''
        #do matching, the min and max will share a common prefix
        #the longest string will have the longest prefix if compared correctly
        for i in range(len(minString)):
            print(f'i is {i}')
            if minString[i] == maxString[i]:
                print(f'adding to {res}')
                res+= minString[i]
            else:
                print(f'found it, returing {res}')
                #this to prevent non prefix
                return res
        return res