import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        for i in range(len(nums)):
            vals = nums[:i] + nums[i+1:]
            prods = math.prod(vals)
            products.append(int(prods))
        return products
        