class Solution:
    def isValidSudoku(self, board: list) -> bool:
        lenght = 9
        square0 = {(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), }
        square1 = {(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2), }
        square2 = {(6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2), }
        square3 = {(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), }
        square4 = {(0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8), }
        square5 = {(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5), }
        square6 = {(3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8), }
        square7 = {(6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5), }
        square8 = {(6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8), }
        squares = [square0, square1, square2, square3, square4, square5, square6, square7, square8]

        from pip._vendor.msgpack.fallback import xrange
        for i in xrange (0, lenght):
            for j in xrange (0, lenght):
                if board[i][j] != ".":
                    for square in xrange (0, lenght):
                        if (i, j) in squares[square]:
                            if not self.check (i, j, {}, board, squares[square]):
                                return False
        return True

    def check (self, i, j,numbersDict, board, square):
        for s in square:
            sI = s[0]
            sJ = s[1]
            if board[sI][sJ] != ".":
                if board[sI][sJ] not in numbersDict.keys():
                    numbersDict[board[sI][sJ]] = 1
                else:
                    return False
        numbersDict = {}
        tempJ = 0
        while tempJ<=8:
            if board[i][tempJ] != ".":
                if board[i][tempJ] not in numbersDict.keys():
                    numbersDict[board[i][tempJ]] = 1
                else:
                    return False
            tempJ+=1
        numbersDict ={}
        tempI = 0
        while tempI<=8:
            if board[tempI][j] != ".":
                if board[tempI][j] not in numbersDict.keys():
                    numbersDict[board[tempI][j]] = 1
                else:
                    return False
            tempI+=1
        return True



sol = Solution()
print(sol.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
print(sol.isValidSudoku([[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]))
