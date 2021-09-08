class Solution:
    def generate(self, numRows: int) -> list:
        beginList = [[1],[1,1],[1,2,1]]
        if numRows>len(beginList):
            number = 3
            while number<numRows:
                newNumber = number+1
                newList =[0]*newNumber
                for i in range (len(newList)):
                    if i ==0 or i ==len(newList)-1:
                        newList[i] = 1
                    else:
                        newList[i] = beginList[number-1][i]+beginList[number-1][i-1]
                beginList.append(newList)
                number+=1
        else:
            newList = beginList[:numRows]
            return newList
        return beginList

sol = Solution()
print(sol.generate(5))
print(sol.generate(1))



