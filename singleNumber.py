class Solution:
    def singleNumber(self, nums: list) -> int:
        dict ={}
        for i in range (len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = nums[i]
            else:
                del dict[nums[i]]
        for k in dict.keys():
            return dict[k]

sol = Solution()
print(sol.singleNumber([1,2,3,2,1]))