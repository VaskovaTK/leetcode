class Solution:
    def coinChange(self, coins: list, amount: int) -> int:
        from _collections import deque
        if amount == 0:
            return 0
        maxNumber = 99999999999999999999
        queue = deque()
        queue.append((amount,0))
        minCount = maxNumber
        while len(queue)>0:
            amountFromQueue, countFromQueue = queue.pop()
            for i in range (0, len(coins)):
                newAmount = amountFromQueue-coins[i]
                if newAmount>0:
                    newCount = countFromQueue + 1
                    queue.append((newAmount, newCount))
                elif newAmount== 0:
                    newCount = countFromQueue+1
                    if minCount>newCount:
                        minCount = newCount
        if minCount == maxNumber:
            return -1
        return minCount





        # while amount>0:
        #     while i >
        #     for i in range (0, len(coins)):
        #         amount-= coins[i]
        #

        # coins = sorted(coins)
        # count = 0
        # i = len(coins)-1
        # while i != -1:
        #     if amount==0:
        #         return count
        #     if amount>0:
        #         amount-=coins[i]
        #         count+=1
        #     else:
        #         count-=1
        #         amount+=coins[i]
        #         i-=1
        # return -1


    #     rem =99999999999999
    #     rem = self.recursion(0, rem, amount, coins)
    #     return rem
    #
    # def recursion (self, count: int, rem: int, amount: int, coins: list):
    #     if amount == 0:
    #         if rem > count:
    #             rem = count
    #             return rem
    #         elif amount < 0:
    #             return rem
    #     for i in range (0, len(coins)):
    #         amount-= coins[i]
    #         if amount>=0:
    #             count+=1
    #             rem = self.recursion(count, rem, amount, coins)
    #         else:
    #             return rem





        # if firstAmount in remDict:
        #     count+=remDict[firstAmount]
        # for i in range (0, len(coins)):
        #     amount-= coins[i]
        #     count +=1
        #     if amount > 0:
        #         self.recursion(firstAmount, count, remDict, amount, coins)
        #     elif amount<0:
        #         return remDict
        #     else:
        #         if firstAmount in remDict:
        #             if count<remDict[firstAmount]:
        #                 remDict[firstAmount] = count
        #             else:
        #                 return remDict


sol = Solution()
# print(sol.coinChange(coins = [1,5,2], amount = 11))
# print(sol.coinChange(coins=[1,4,5], amount=12))
print(sol.coinChange([186,419,83,408], 6249))
