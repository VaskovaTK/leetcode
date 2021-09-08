class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        dictionary = {}
        for i in range(0,len(nums)):
            if nums[i] not in dictionary.keys():
                dictionary[nums[i]] = 1
            else:
                return True
        return False


sol = Solution()
sol.containsDuplicate([1,2,3,4])
sol.containsDuplicate([1,2,3,4,5,5])
sol.containsDuplicate([1,2,3,1])