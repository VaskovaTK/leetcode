class Solution:
    def triangleNumber(self, nums: list) -> int:
       numbersArray = [0]*10
       for i in range(0,len(nums)):
           numbersArray[nums[i]] += 1
       print(numbersArray)

sol = Solution()
sol.triangleNumber([1,2,2,4])