class Solution:
    def rotate(self, nums: list, k: int) -> None:
        if len(nums) == 1:
            return None
        if k>len(nums):
            k = k % len(nums)
        pointerIndex = len(nums)-k
        countIteration = 0
        while pointerIndex<=len(nums)-1:
            point = nums[pointerIndex]
            i = 0+countIteration
            remember = nums[0+countIteration]
            while i<pointerIndex:
                next = nums[i + 1]
                nums[i+1] = remember
                remember = next
                i+=1
            nums[0+countIteration] = point
            pointerIndex+=1
            countIteration+=1
        print(nums)
        # while k >0:
        #     remember = nums[0]
        #     last = nums[len(nums)-1]
        #     i = 0
        #     while i < len(nums)-1:
        #         next = nums[i+1]
        #         nums[i+1] = remember
        #         remember = next
        #         i+=1
        #     nums[0] = last
        #     k-=1
        # print(nums)
sol = Solution()
# sol.rotate([1,2,3,4,5,6,7],3)
sol.rotate([1,2], 3)