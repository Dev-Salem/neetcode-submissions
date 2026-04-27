class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        vals = {}
        for i in nums:
            vals[i] = vals.get(i, 0)+1
        #go through the vals, and store them but in inverse. the 
        #count is the key, the values are the values!
        freq = [[] for i in range(len(nums)+1)]
        #final structure should be:
        #{1: [1,2,3], 2:[3,4,5]} etc
        for number,count in vals.items():
            freq[count].append(number)
        res = []
        print(f'frequence is {freq}')
        for i in range(len(freq)-1, 0, -1):
            print(f'res is {res}')
            for num in freq[i]:
                print(f'going to append {num}')
                res.append(num)
                if len(res) == k:
                    print(f'we stop here {res}')
                    return res