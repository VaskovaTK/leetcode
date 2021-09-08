class Solution:
    def maxSubArray(self, nums: list) -> int:
        # maxSum = -9999999999999999999
        # for i in range(len(nums)):
        #     endEl = len(nums)
        #     nowEl = i+1
        #     while nowEl <=endEl:
        #         sumNow = nums[i]
        #         for j in range(i+1,nowEl):
        #             sumNow+=nums[j]
        #         nowEl+=1
        #         if maxSum<sumNow:
        #             maxSum = sumNow
        #
        # return maxSum
        import itertools
        return max(itertools.accumulate(nums, lambda a, b: max(b, a + b)))



sol = Solution()

print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))




