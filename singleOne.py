class Solution:
    def singleNumber(self, nums: list) -> int:
        numbersDict = {}
        for i in range(len(nums)):
            if nums[i] in numbersDict:
                del numbersDict[nums[i]]
            else:
                numbersDict[nums[i]] = 1
        for key in numbersDict.keys():
            return key



solution = Solution()
print(solution.singleNumber([1,1,3,5,3]))
