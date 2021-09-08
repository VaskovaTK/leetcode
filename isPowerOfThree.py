class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n >0:
            if n == 1:
                return True
            n = n/3
        return False



sol = Solution()
print(sol.isPowerOfThree(45))
print(sol.isPowerOfThree(27))
print(sol.isPowerOfThree(0))
print(sol.isPowerOfThree(9))
print(sol.isPowerOfThree(1))
print(sol.isPowerOfThree(243))