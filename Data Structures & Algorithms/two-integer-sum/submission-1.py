class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #goal: 2 integers in `num` will give us the 2 target
        #way, create a hash map of values as you loop through them
        #calacuate the diff, see if it's in the hash map
        values = {}
        for i,current in enumerate(nums):
            diff = target - current
            if diff in values:
                return [values[diff],i]
            values[current] = i