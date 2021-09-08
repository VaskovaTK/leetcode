class Solution:
    def trailingZeroes(self, n: int) -> int:
        import math
        nFactorial = math.factorial(n)
        count = 0
        strFactorial = str(nFactorial)
        for i in range(-1,-len(strFactorial)-1,-1):
            if strFactorial[i] =="0":
                count +=1
            else:
                break
        return count






sol = Solution()
print(sol.trailingZeroes(5))
print(sol.trailingZeroes(0))
print(sol.trailingZeroes(3))
print(sol.trailingZeroes(7))
print(sol.trailingZeroes(10))