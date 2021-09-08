class Solution:
    def majorityElement(self, nums: list) -> int:
        mainElement = None
        timesOfElement = 0
        for i in range(0,len(nums)):
            if nums[i] != mainElement:
                if timesOfElement >0:
                    timesOfElement-=1
                else:
                    mainElement = nums[i]
            else:
                timesOfElement+=1
        return mainElement
sol = Solution()
print(sol.majorityElement([3,2,3]))
print(sol.majorityElement([2,2,1,1,1,2,2]))