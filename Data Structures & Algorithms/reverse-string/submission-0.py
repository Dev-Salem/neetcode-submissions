class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            secondString = s[len(s) - i -1]
            firstString = s[i]
            print(f'going to switch {firstString} and {secondString}')
            s[i],s[len(s) - i -1] = s[len(s) - i -1],s[i]
            
        