class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        vals = []
        for i in nums:
            if i > 0:
                vals.append(i)
        if len(vals) == 0:
            return 1
        minNum = max(vals) +1
        start = 1
        for i in range(1, minNum):
            if start not in vals:
                return start
            else:
                start+=1
        return start

            
