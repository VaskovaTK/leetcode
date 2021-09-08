class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range (x +1) :
            num = i*i
            if num == x:
                return i
            elif num  >  x:
                return i-1

sol = Solution()
sol.mySqrt(8)