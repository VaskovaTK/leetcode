class Solution:
    def fizzBuzz(self, n: int) -> list:
        nList = []
        for i in range(1,n+1):
            nList.append(str(i))
        if len(nList)<=2:
            return nList
        else:
            for i in range (2,len(nList)):
                if int(nList[i])%3==0:
                    if int(nList[i])%5==0:
                        nList[i] = 'FizzBuzz'
                        continue
                    else:
                        nList[i] = 'Fizz'
                        continue
                if int(nList[i])%5==0:
                    nList[i] = 'Buzz'
            return nList
sol = Solution()
sol.fizzBuzz(5)
# sol.fizzBuzz(2)