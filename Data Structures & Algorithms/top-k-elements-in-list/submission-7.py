class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #solution: count frequancy (bucket sort), then return k
        vals = {}
        for i in nums:
            vals[i] = vals.get(i, 0)+1
        vals = sorted(vals.items(), key=lambda x: x[1])
        res = vals[-k:]
        print(res)
        return [k for k, _ in res]
