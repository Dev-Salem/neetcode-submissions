class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #have 3 pointers, one at the end of nums1, one at the end of nums2, and one at the end of real values of 
        #nums1
        lastActual = m+n -1
        last1 = m -1
        last2 = n -1
        #start filling backwardley, stop only when we no longer have values (e.g reached 0)
        #fill lareger first
        while last1 >= 0 and last2 >= 0:
            if nums1[last1] > nums2[last2]:
                nums1[lastActual] = nums1[last1]
                last1-=1
            else:
                nums1[lastActual] = nums2[last2]
                last2-=1
            lastActual-=1
        
        while last2 >=0:
            nums1[lastActual] = nums2[last2]
            last2-=1
            lastActual-=1


        

        