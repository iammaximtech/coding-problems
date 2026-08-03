class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.prefixSumMatrix = [[0]*(COLS+1) for r in range(ROWS+1)]
        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.prefixSumMatrix[r][c+1]
                self.prefixSumMatrix[r+1][c+1]=prefix+above


    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        r1, c1, r2, c2 = r1+1, c1+1, r2+1, c2+1
        prefixSum = self.prefixSumMatrix[r2][c2]
        above = self.prefixSumMatrix[r1-1][c2]
        left = self.prefixSumMatrix[r2][c1-1]
        topCorner = self.prefixSumMatrix[r1-1][c1-1]
        return prefixSum - above - left +topCorner


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)