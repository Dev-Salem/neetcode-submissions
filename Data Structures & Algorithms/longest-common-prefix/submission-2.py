class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #find the min string in the list
        #find the longest in the string
        #go and do matching between the min and max
        minStr = min(strs)
        maxStr = max(strs)
        res = ''
        for i in range(len(minStr)):
            if minStr[i] == maxStr[i]:
                res+= minStr[i]
            else:
                return res
        return res