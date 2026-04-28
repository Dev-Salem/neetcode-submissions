class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.vals = matrix
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for i in range(len(self.vals)):
            for j in range(len(self.vals[0])):
                if(i>=row1 and i<=row2 and j>=col1 and j<=col2):
                    res+= self.vals[i][j]
        return res
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)