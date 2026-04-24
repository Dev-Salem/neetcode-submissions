class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = {}
        for i in strs:
            key = ''.join(sorted(i))
            if key in res:
                res[key].append(i)
            else:
                res[key] = [i]
        return list(res.values())