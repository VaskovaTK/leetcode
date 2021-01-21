from _collections import deque
class Solution:
    def exist(self, board: list, word: str) -> bool:
        queue = deque()
        taken = [0]*len(word)
        lastLetter = len(word)-1
        for i in range (0, len(board)):
            for j in range (0, len(board[i])):
                if board[i][j] == word[0]:
                    queue.append((i,j, 1))
        while len(queue)>0:
            i, j, nextPosition = queue.pop()
            for t in range(nextPosition-1,len(taken)):
                taken[t] = 0
            if nextPosition-1 == lastLetter:
                return True
            if j+1<len(board[i]) and j+1>=0 and (i,j+1) not in taken:
                if board[i][j+1] == word[nextPosition]:
                    taken[nextPosition-1] = (i,j)
                    if nextPosition+1<=lastLetter:
                        queue.append((i,j+1, nextPosition+1))
                    else:
                        return True
            if j-1 < len(board[i]) and j-1>=0 and (i,j-1) not in taken:
                if board[i][j-1] == word[nextPosition]:
                    taken[nextPosition - 1] = (i, j)
                    if nextPosition+1 <= lastLetter:
                        queue.append((i, j - 1, nextPosition+1))
                    else:
                        return True
            if i+1 < len(board) and i+1>=0 and (i+1,j) not in taken:
                if board[i+1][j] == word[nextPosition]:
                    taken[nextPosition - 1] = (i, j)
                    if nextPosition+1 <= lastLetter:
                        queue.append((i+1, j, nextPosition+1))
                    else:
                        return True
            if i - 1 < len(board) and i-1>=0 and (i-1,j) not in taken:
                if board[i - 1][j] == word[nextPosition]:
                    taken[nextPosition - 1] = (i, j)
                    if nextPosition+1 <= lastLetter:
                        queue.append((i - 1, j, nextPosition+1))
                    else:
                        return True
        return False






sol = Solution()
print(sol.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))
print(sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"SEE"))
print(sol.exist([["a"]],"a"))
print(sol.exist([["a","b"]],"ba"))
print(sol.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]],"ABCESEEEFS"))
print(sol.exist( board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"))
print(sol.exist([["a","b"],["c","d"]],"abcd"))