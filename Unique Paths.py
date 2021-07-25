class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cells = [[]]*m
        lenght = 0
        number = 0
        while lenght<m:
            width = [0] * n
            for i in range(n):
                number+=1
                width[i] = number
            cells[lenght] = width
            lenght+=1
        print(cells)
        ways = [0]
        lenght = m*n
        self.recursion(n, 1, lenght, ways)

    def recursion (self, n, currCell: int, endCell: int, ways:list):
        print('here')
        if currCell >= endCell:
            ways[0] +=1
            return ways
        cellCount2 = currCell + n
        if (cellCount2) <= endCell:
            print('in ihe cellcount2 ')
            currCell = currCell+n
            self.recursion(n, currCell, endCell, ways)
        cellCount = currCell + 1 // n
        if (cellCount) <=1:
            currCell = currCell+1
            self.recursion(n,currCell,endCell,ways)
        print(ways[0])

sol = Solution()
sol.uniquePaths(3,2)


