from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = {}
        for i in nums:
            res[i] =res.get(i, -1) + 1
        print(f' the res is {res}')
        sortedItems = sorted(res.items(), key=lambda x: x[1], reverse=True)
        print(f'sorted items {sortedItems}')
        return sortedItems[0][0]
