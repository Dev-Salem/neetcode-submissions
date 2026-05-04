class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        vals = set()
        for i in nums:
            if i > 0:
                vals.add(i)
        if len(vals) == 0:
            return 1
        maxVal = max(vals) +1
        start = 1
        for i in range(1, maxVal):
            if start not in vals:
                return start
            else:
                start+=1
        return start

            
