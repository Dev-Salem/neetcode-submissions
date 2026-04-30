class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        #there was that algo, where you store counts as keys and values
        #as lists, in that case i could do it all and get lists of vals with counter > n/3
        for i in nums:
            freq[i] = freq.get(i, 0) +1
        print(freq)
        res = []
        for v,f in freq.items():
            if f > len(nums)//3:
                res.append(v)
        return res