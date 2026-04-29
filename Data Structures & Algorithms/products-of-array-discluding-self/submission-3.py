class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #comptue prefix and suffix, basically the product from start to end
        #and from end to start
        #the product of the item is prefix i-1 * suffix i+1
        matLen = (len(nums) +1)
        prefixes, suffixes = [1] * matLen,[1] * matLen
        prefix = 1
        suffix = 1
        res = []
        for i in range(len(nums)):
            prefix*=nums[i]
            prefixes[i] = prefix
        for j in range(len(nums) -1, -1, -1):
            suffix*=nums[j]
            suffixes[j] = suffix
        print(f'prefixes {prefixes} and suffiexes {suffixes}')
        for z in range(len(nums)):
            res.append(prefixes[z-1] * suffixes[z+1])
        return res