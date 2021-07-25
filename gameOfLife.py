class Solution:
    def gameOfLife(self, board: list) -> None:
        lenght = len(board)
        zeroArray = []
        oneArray = []
        for i in range (0, lenght):
            endCell = len(board[i])
            for j in range(0,endCell):
                population = 0
                if i-1>=0 and i-1<lenght:
                    population+= board[i-1][j]
                if i+1>=0 and i+1<lenght:
                    population+= board[i+1][j]
                if j-1>=0 and j-1<endCell:
                    population+= board[i][j-1]
                if j+1>=0 and j+1<endCell:
                    population+= board[i][j+1]
                if i-1>=0 and j-1>=0 and i-1<lenght and j-1<endCell:
                    population+= board[i-1][j-1]
                if i-1 >=0 and j+1>=0 and i-1<lenght and j+1<endCell:
                    population+= board[i-1][j+1]
                if i+1>=0 and j-1>=0 and i+1<lenght and j-1<endCell:
                    population+= board[i+1][j-1]
                if i+1>=0 and j+1>=0 and i+1<lenght and j+1<endCell:
                    population+= board[i+1][j+1]
                # print("i = {}, j = {}, population = {}".format(i,j,population))
                if population <2:
                    zeroArray.append((i,j))
                elif population >3:
                    zeroArray.append((i,j))
                elif population ==3:
                    oneArray.append((i,j))
        # print(oneArray,zeroArray)
        # print(board)
        for m in range(0,len(oneArray)):
            i = oneArray[m][0]
            j = oneArray[m][1]
            board[i][j] = 1
        for l in range(0,len(zeroArray)):
            i = zeroArray[l][0]
            j = zeroArray[l][1]
            board[i][j] = 0
        # print(board)

sol = Solution()
sol.gameOfLife(board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]])
sol.gameOfLife(board=[[1,1], [1,0]])