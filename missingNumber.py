class Solution:
    def missingNumber(self, nums: list) -> int:
        lenght = len(nums)+1
        newList = [0]*lenght
        for i in range(len(nums)):
            newList[nums[i]] = 1
        for j in range(len(newList)):
            if newList[j] ==0:
                return j
        return len(newList)+1
sol = Solution()
print(sol.missingNumber([3,0,1]))
print(sol.missingNumber([2,0,1]))