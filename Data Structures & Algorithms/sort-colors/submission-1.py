class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i in range(1, len(nums)):
        #     j = i-1
        #     while (j>=0 and nums[j+1] < nums[j]):
        #         nums[j+1],nums[j] = nums[j],nums[j+1]
        #         j-=1
        hashMap = {0:0,1:0,2:0}
        for i in nums:
            hashMap[i] = hashMap.get(i) +1
        print(f'Hash map is {hashMap}')
        index = 0
        for i in range(3):
            while hashMap[i]:
                hashMap[i] -=1
                nums[index] = i
                index+=1
        print(f'nums is {nums}')
