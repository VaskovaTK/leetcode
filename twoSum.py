class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        retList = list()
        for i in range(0,len(nums)):
            for j in range(0, len(nums)):
                if i !=j:
                    if nums[i]+nums[j] == target:
                        retList.append(i)
                        retList.append(j)
                        return retList
sol = Solution()
sol.twoSum(nums = [2,7,11,15], target = 9)
sol.twoSum(nums = [3,2,4], target = 6)
sol.twoSum(nums = [3,3], target = 6)
sol.twoSum([-5,4,5],-1)
sol.twoSum([0,4,3,0],0)