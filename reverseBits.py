class Solution:
    def reverseBits(self, n: int) -> int:
        return (int(bin(n)[2:].zfill(32)[::-1], 2))
    # def reverseBits(self, n: bin) -> int:
    #     maskOne = 0b1
    #     retStr = "0b"
    #     import math
    #     lenght = int(math.log(n, 2)) + 1
    #     for i in range(lenght):
    #         shiftMask = maskOne << i
    #         # print(bin(shiftMask))
    #         number = shiftMask & n
    #         # print(bin(n))
    #         if number > 0:
    #             retStr+="1"
    #         else:
    #             retStr += "0"
    #     # print(bin(n))
    #     # print(retStr)
    #     # print(int(retStr,2))
    #     return int(retStr,2)
    #
    #


sol = Solution()
sol.reverseBits(0b11111111111111111111111111111101)