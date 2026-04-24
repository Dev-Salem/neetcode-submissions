class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # while val in nums:
        #     nums.remove(val)
        # return len(nums)
        swap = 0
        for i in range(len(nums)):
            if nums[i] != val:
                print(f'found the  {val}, going to swap ({nums[i],nums[-1-swap]}) (last elment not val is {-1-swap}) and swap count is {swap} and i is {i}')
                nums[swap] = nums[i]
                swap+=1
            print(f'{nums}')
        return swap