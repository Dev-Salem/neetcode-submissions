class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        for i in range(len(numbers)):
            diff = target - numbers[i]
            for j in range(len(numbers)):
                print(f'comparing {i},{j}, and diff {diff}. element at i is {numbers[i]}, element at js is {numbers[j]}')
                if numbers[j] == diff:
                    return [i+1,j+1]