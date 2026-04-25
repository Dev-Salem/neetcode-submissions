class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}
        #the goal, find the 2 numbers in the arry where the sum is target
        #first,iterate thhrough the nums
        #second, calculate the diff, if diff exists in vals, return
        #if not, ok add them to vals
        #why this works? because the other pair will always work
        for k,v in enumerate(nums):
            diff = target - v
            print(f'k: {k}, v: {v}, diff: {diff}')
            if diff in vals:
                return [vals[diff],k]
            #store here in vals, the key should be the actual value
            #the value should be the index
            vals[v] = k
        print(f'this is {vals}')