class Solution:
    class Solution:
        def climbStairsHelper(self, n, dp):
            if n == 2:
                return 2
            if n == 0 or n == 1:
                return 1

            if dp[n - 1] == -1:
                step1 = self.climbStairsHelper(n - 1, dp)
                dp[n - 1] = step1
            else:
                step1 = dp[n - 1]

            if dp[n - 2] == -1:
                step2 = self.climbStairsHelper(n - 2, dp)
                dp[n - 2] = step2
            else:
                step2 = dp[n - 2]

            return step1 + step2

        def climbStairs(self, n):
            dp = [-1 for i in range(n)]
            return self.climbStairsHelper(n, dp)

    # def climbStairs(self, n: int) -> int:
    #     ways = [0]*1
    #     ways = self.recursion(n,ways)
    #     return ways[0]
    #
    # def recursion (self, n:int, ways:list):
    #     if n > 0:
    #         self.recursion(n-1,ways)
    #         self.recursion(n-2,ways)
    #     elif n == 0 or n == 1 or n ==2:
    #         ways[0]+=1
    #     return ways
    #




# class Solution:
#     def climbStairs(self, n: int) -> int:
#         ways ={"top": 0}
#         ways = self.recursion(n,0,ways)
#         return ways["top"]
#
#     def recursion (self, n:int, nowCell:int, ways:dict):
#         if nowCell == n:
#             ways["top"]+=1
#             return ways
#         elif nowCell>n:
#             return ways
#         else:
#             self.recursion(n,nowCell+1,ways)
#             self.recursion(n,nowCell+2,ways)
#         return ways


sol = Solution()
print(sol.climbStairs(3))
print(sol.climbStairs(2))
print(sol.climbStairs(1))
print(sol.climbStairs(0))