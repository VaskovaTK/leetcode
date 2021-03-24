# class Solution:
#     def stoneGame(self, piles: list) -> bool:
#         for i in range (0, len(piles)):
#             if i <len(piles)-1:
#                 while True:
#                     if piles[i+1]>piles[i]:
#                         piles[i],piles[i+1] = piles[i+1], piles[i]
#                         if i-1>=0:
#                             i = i-1
#                     else:
#                         break
#         a = 0
#         l = 0
#         for index in range (0, len(piles)):
#             if index%2 ==0 or index ==0:
#                 a+=piles[index]
#             else:
#                 l+=piles[index]
#         if a>l:
#             return True
#         else:
#             return False

class Solution:
    def stoneGame(self, piles: list) -> bool:
        count = 0
        for i in range (len(piles)):
            count+=piles[i]
        forWin = count/2+1
        alex = 0
        for i in range (0,len(piles),2):
            alex+=piles[i]
        if alex>=forWin:
            return True
        for i in range (1, len(piles),2):
            alex+=piles[i]
        if alex>=forWin:
            return True
        return False

        # pointer1 = 0
        # pointer2 = len(piles)-1
        # alex = 0
        # lee = 0
        # counter = 1
        # while pointer1<pointer2:
        #     if piles[pointer1+1]<piles[pointer2-1]:
        #         if counter %2 !=0:
        #             alex+=piles[pointer1]
        #             pointer1+=1
        #             counter+=1
        #         else:
        #             lee+=piles[pointer1]
        #             pointer1 +=1
        #             counter+=1
        #     elif piles[pointer1+1]>piles[pointer2-1]:
        #         if counter %2 !=0:
        #             alex+=piles[pointer2]
        #             pointer2-=1
        #             counter+=1
        #         else:
        #             lee+=piles[pointer2]
        #             pointer2 -=1
        #             counter+=1
        #     else:
        #         if piles[pointer1]>=piles[pointer2]:
        #             if counter % 2 != 0:
        #                 alex += piles[pointer1]
        #                 pointer1 += 1
        #                 counter += 1
        #             else:
        #                 lee += piles[pointer1]
        #                 pointer1 += 1
        #                 counter += 1
        #         else:
        #             if counter % 2 != 0:
        #                 alex += piles[pointer2]
        #                 pointer2 -= 1
        #                 counter += 1
        #             else:
        #                 lee += piles[pointer2]
        #                 pointer2 -= 1
        #                 counter += 1
        # if alex>lee:
        #     return True
        # else:
        #     return False





def test(sol, inputTest, expect):
    res = sol.stoneGame(inputTest)
    print('output {}, expected {}, result {}'.format(res, expect, res == expect))

sol = Solution()
test(sol, [5,4,3,5], True)
test(sol, [5,4,10,16,136,2,1,0,3,5], True)
test(sol, [18,3,8,1,9,7,11,13,18,11,17,20,14,2,17,20,11,14,8,7], True)