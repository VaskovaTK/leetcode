class Solution:
    def hammingWeight(self, n: bin) -> int:
        maskOne = 0b1
        count = 0
        if n == 0:
            return 0
        import math
        lenght = int(math.log(n, 2)) + 1
        for i in range(lenght):
            shiftMask = maskOne << i
            # print(bin(shiftMask))
            number = shiftMask & n
            if number > 0:
                count+=1
        # print(count)
        return count

sol = Solution()
sol.hammingWeight(0b001111111111111111111111111110111)