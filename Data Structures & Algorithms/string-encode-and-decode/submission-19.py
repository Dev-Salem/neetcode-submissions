def to_int(value, default=0):
    try:
        return int(value)
    except (ValueError, TypeError):
        return default


class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ["0"]
        key = 'seperator'
        for i in strs:
            res.append(str(len(i)))
            res.append(i)
        val = 'seperator'.join(res)
        return val

    def decode(self, s: str) -> List[str]:
        res = []
        for i in s.split('seperator'):
            res.append(i)
        vals = []
        for count in range(1,len(res),2):
            string = ''
            nextElement = count+1
            
            for i in range(int(res[count])):
                string+=res[nextElement][i]
            vals.append(string)
        return vals


