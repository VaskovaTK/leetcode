class Solution:
    def majorityElement(self, nums: list) -> list:
        # counter = 0
        # retList =[]
        # majorI = 0
        # for i in range (0, len(nums)):
        #     if counter == 0:
        #         counter+=1
        #         majorI = i
        #         continue
        #     if nums[majorI] == nums[i]:
        #         counter+=1
        #     else:
        #         counter-=1
        # if counter == 0 and len(nums)<3:
        #     return nums
        # else:
        #     retList.append(nums[majorI])
        #     return retList


sol = Solution()
print(sol.majorityElement([3,2,3]))
# print(sol.majorityElement([1,2,3]))