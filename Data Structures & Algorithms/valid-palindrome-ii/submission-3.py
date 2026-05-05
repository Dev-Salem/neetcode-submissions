class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(l,r):
            while l<=r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True

        n = len(s) -1
        l,r = 0, n
        
        while l<r:
            if s[l] != s[r]:
                return (is_palindrome(l+1, r) or (is_palindrome(l, r-1)))
            l+=1
            r-=1
        return True
        