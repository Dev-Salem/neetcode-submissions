from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #brute force approach:
        #iterate through the rows, check if each row has duplicates
        #iterate through the cols, check if each col has duplicates
        #iterate through the boxes, check if each has duplicates
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        for i in range(9):
            for j in range(9):
                item = board[i][j]
                if item =='.':
                    continue
                if item in rows[i] or item in cols[j] or item in boxes[i//3,j//3]:
                    return False
                rows[i].add(item)
                cols[j].add(item)
                boxes[i//3,j//3].add(item)
            
        return True