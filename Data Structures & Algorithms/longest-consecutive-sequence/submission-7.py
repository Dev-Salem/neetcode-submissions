
        
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for i in numSet:
            #is the start of a sequance (doesn't have left items)
            if (i-1) not in numSet:
                counter = 0
                #check forward items
                while (counter+i) in numSet:
                    counter+=1
                longest = max(longest,counter)
        return longest

        