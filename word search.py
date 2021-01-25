from _collections import deque

from pip._vendor.msgpack.fallback import xrange


# class Solution:
#     def exist(self, board: list, word: str) -> bool:
#         queue = deque()
#         taken = [0]*len(word)
#         lastLetter = len(word)-1
#         for i in xrange (0, len(board)):
#             for j in xrange (0, len(board[i])):
#                 if board[i][j] == word[0]:
#                     queue.append((i,j, 1))
#         while len(queue)>0:
#             i, j, nextPosition = queue.pop()
#             for t in xrange(nextPosition-1,len(taken)):
#                 taken[t] = 0
#             if nextPosition-1 == lastLetter:
#                 return True
#             if j+1<len(board[i]) and j+1>=0 and (i,j+1) not in taken:
#                 if board[i][j+1] == word[nextPosition]:
#                     taken[nextPosition-1] = (i,j)
#                     if nextPosition+1<=lastLetter:
#                         queue.append((i,j+1, nextPosition+1))
#                     else:
#                         return True
#             if j-1 < len(board[i]) and j-1>=0 and (i,j-1) not in taken:
#                 if board[i][j-1] == word[nextPosition]:
#                     taken[nextPosition - 1] = (i, j)
#                     if nextPosition+1 <= lastLetter:
#                         queue.append((i, j - 1, nextPosition+1))
#                     else:
#                         return True
#             if i+1 < len(board) and i+1>=0 and (i+1,j) not in taken:
#                 if board[i+1][j] == word[nextPosition]:
#                     taken[nextPosition - 1] = (i, j)
#                     if nextPosition+1 <= lastLetter:
#                         queue.append((i+1, j, nextPosition+1))
#                     else:
#                         return True
#             if i - 1 < len(board) and i-1>=0 and (i-1,j) not in taken:
#                 if board[i - 1][j] == word[nextPosition]:
#                     taken[nextPosition - 1] = (i, j)
#                     if nextPosition+1 <= lastLetter:
#                         queue.append((i - 1, j, nextPosition+1))
#                     else:
#                         return True
#         return False

class Solution:
    def exist(self, board: list, word: str) -> bool:
        def preCheck():
            preDict = {}

            for i in word:
                if i in preDict:
                    preDict[i] += 1
                else:
                    preDict[i] = 1

            for i in board:
                for j in i:
                    if j in preDict and preDict[j] > 0: preDict[j] -= 1
            for i in preDict.values():
                if i > 0: return False
            return True

        def helper(wordIdx, x, y):
            if board[x][y] != word[wordIdx]:
                return False
            elif wordIdx == l - 1:
                return True
            else:
                wordIdx += 1
                tempChar = board[x][y]
                board[x][y] = None
                for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    xNext = x + d[0]
                    yNext = y + d[1]
                    if -1 < xNext < m and -1 < yNext < n and board[xNext][yNext]:
                        if helper(wordIdx, xNext, yNext): return True
                board[x][y] = tempChar
                return False

        if not preCheck(): return False

        m = len(board)
        n = len(board[0])
        l = len(word)
        for i in range(m):
            for j in range(n):
                if helper(0, i, j): return True

        return False


sol = Solution()
print(sol.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))
# print(sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"SEE"))
# print(sol.exist([["a"]],"a"))
# print(sol.exist([["a","b"]],"ba"))
# print(sol.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]],"ABCESEEEFS"))
# print(sol.exist( board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"))
# print(sol.exist([["a","b"],["c","d"]],"abcd"))