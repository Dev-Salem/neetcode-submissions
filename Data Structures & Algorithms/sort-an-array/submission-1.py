class Sorting():
    def __init__(self, nums):
        self.nums = nums
    def mergeSort(self,arr: List[int]):
        if len(arr) <= 1:
            return arr
        middleIndex = len(arr) //2
        leftSide = arr[:middleIndex]
        rightSide = arr[middleIndex:]
        leftSorted = self.mergeSort(leftSide)
        rightSorted = self.mergeSort(rightSide)
        return self.combineArray(leftSorted,rightSorted)
    def combineArray(self, left: List[int], right: List[int]):
        #left and right pointers show which item in the list we sorted
        merged = []
        leftPointer = 0
        rightPointer = 0
        while leftPointer < len(left) and rightPointer < len(right):
            currentLeft = left[leftPointer]
            currentRight = right[rightPointer]
            if currentLeft < currentRight:
                merged.append(currentLeft)
                leftPointer+=1
            else:
                merged.append(currentRight)
                rightPointer+=1
        merged.extend(left[leftPointer:])
        merged.extend(right[rightPointer:])
        return merged

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #let' work on binary sort, basically split in half, swap. and recursion 
        sorting = Sorting(nums)
        return sorting.mergeSort(nums)
