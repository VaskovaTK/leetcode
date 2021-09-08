class Solution:
    def removeDuplicates(self, nums: list) -> int:
        recIndex = 0
        remNumber = -9999999
        for i in range(0,len(nums)):
            if nums[i]>remNumber:
                nums[recIndex] = nums[i]
                recIndex+=1
                remNumber = nums[i]
        # print(recIndex)
        return recIndex

sol = Solution()
sol.removeDuplicates([1,1,2,3,5,5,6,6,6,7,7,7])

