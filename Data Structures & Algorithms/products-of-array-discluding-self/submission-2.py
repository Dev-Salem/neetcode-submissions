import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        for i in range(len(nums)):
            prods = math.prod(nums[:i] + nums[i+1:])
            products.append(int(prods))
        return products
        